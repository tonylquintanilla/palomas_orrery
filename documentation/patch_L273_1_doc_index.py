"""patch_L273_1_doc_index.py -- L-273. The README's document table
stops being hand-maintained.

RUN COMMAND
-----------
Save into the ORRERY repo root, open in VS Code, click Run.

    python patch_L273_1_doc_index.py

WHAT IT DOES
------------
Ten writes, all-or-nothing:

  1. doc_index.py -- NEW. Regenerates README.md's key-documents table
     from a one-line Doc-Kind tag carried by each document.
  2. README.md -- the hand-maintained table becomes a DOC-INDEX marker
     zone. The documentation/ deep-dive links stay a hand-written table
     beneath it, because doc_index only scans the repo root.
  3-10. A Doc-Kind tag added to eight root documents.

  Plus one row in orrery_maintenance_run.py's GENERATORS list, so the
  table is rewritten on every maintenance run rather than when somebody
  remembers.

THE DESIGN, AND WHOSE IT IS
---------------------------
Tony's, 2026-08-31. Claude had proposed a CHECKER that fails when the
README's table and the root document set disagree, and recommended it
over a generator. Tony proposed the third thing: an INDEXER writing into
the README in place, the way skills_index.py writes the manifest into
PROJECT_INSTRUCTIONS.md. It is better, and it dissolves Claude's own
objection -- the checker left the duplication in place and only made it
loud, which is the opposite of this project's fix-the-producer rule.

The purpose text lives in the document it describes, not in doc_index.py
and not in the README. Copied deliberately from skills_index.py, whose
editorial column lives in each skill's own frontmatter: Tony keeps
control of the wording while the target file stays generated. A
description dict inside the tool would be the shadow store that
module_atlas.py already deleted when ROLE_MAP became a mirror.

THREE KINDS, WHICH IS A CORRECTION TO L-273 AS WRITTEN
------------------------------------------------------
The ledger block says five documents are generated and seven are
hand-written. Measured, it is three kinds, not two:

  generated  MODULE_ATLAS.md, MODULE_INDEX.md, DATA_INVENTORY.md,
             PROVENANCE_AUDIT.md, WORKSHEET_CHECK.md
  zoned      README.md, PROJECT_INSTRUCTIONS.md, LEDGER_CONSOLIDATED.md
             -- hand-written prose around a marker zone a tool rewrites
  hand       PROJECT_ORIGIN.md, ADDING_OBJECTS_GUIDE.md, LICENSE.md,
             RUNNING_A_PATCH_FILE.md, requirements.txt

The zoned kind is the one the two-way split had no room for, and it is
the kind most likely to be mishandled: the prose is yours to edit and
the zone is not.

WHAT IS DELIBERATELY NOT DONE
-----------------------------
The five GENERATED documents are not tagged by this patch, because a tag
written into them by hand is destroyed on the next run of their
generator. They will appear in the table marked untagged, and
doc_index.py will name them every run. Emitting the tag from
module_atlas.py, data_inventory.py, provenance_scanner.py and
worksheet_checker.py is the remaining half of L-273 and is one line in
each.

That is not an oversight left silent -- it is the blind spot announcing
itself, every run, by name.

The GALLERY repo's README is also not touched. Same tool, different
scan root, and it is recorded on L-273.

VERIFIED BEFORE DELIVERY
------------------------
A leading HTML comment in LEDGER_CONSOLIDATED.md and
PROJECT_INSTRUCTIONS.md survives ledger_index.py and skills_index.py --
tested rather than assumed, because both files are tool-written and a
tag destroyed on the next run would be worse than no tag.

WHAT IS PERMANENT
-----------------
doc_index.py, the README zone, the eight tags, the runner row. This
script is one-shot; archive it into documentation/ once it has run.

NO BACKUP FILE
--------------
Per safe-file-editing 1.10.

Role: patch
Domain: dev_tools

Module created: September 1, 2026 with Anthropic's Claude Opus 5.
"""

import base64
import hashlib
import os
import sys

NEWTOOL = "doc_index.py"
README = "README.md"
RUNNER = "orrery_maintenance_run.py"

FINGERPRINTS = {
    "README.md": "a20a51b97f93a484a06cdc58629641d0",
    "orrery_maintenance_run.py": "85872ce034d0edd1fc1c6426be3ab8ad",
    "PROJECT_INSTRUCTIONS.md": "b7344c6d72e1b7aaf25036e9fdf3f3f8",
    "LEDGER_CONSOLIDATED.md": "318bc75ccf8becaf7aaa2a4d7d291f74",
    "PROJECT_ORIGIN.md": "842fc369296dfde74889d3bfea31a0f4",
    "ADDING_OBJECTS_GUIDE.md": "63a46835f0f3bac379f48b3c3e66f2e9",
    "LICENSE.md": "62436092c2af42f67cfc7e754e427538",
    "RUNNING_A_PATCH_FILE.md": "94bec7c688460cc1527982f975e76103",
    "requirements.txt": "495a62e87189409bce27cc741078bc6e",
}

DOC_INDEX_B64 = (
    "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoiIiJkb2NfaW5kZXgucHkgLS0gcmVnZW5lcmF0ZSBSRUFE"
    "TUUubWQncyBrZXktZG9jdW1lbnRzIHRhYmxlIGZyb20gdGhlCmRvY3VtZW50cyB0aGVtc2VsdmVz"
    "LgoKT1JSRVJZIHJlcG8gdG9vbC4gUnVuIGl0LCBvciBsZXQgb3JyZXJ5X21haW50ZW5hbmNlX3J1"
    "bi5weSBydW4gaXQuCgogICAgcHl0aG9uIGRvY19pbmRleC5weSAgICAgICAgICAgIHJlZ2VuZXJh"
    "dGUgdGhlIHRhYmxlIGluIFJFQURNRS5tZAogICAgcHl0aG9uIGRvY19pbmRleC5weSAtLWNoZWNr"
    "ICAgIHJlcG9ydCBvbmx5OyBleGl0IDEgb24gYW55IHByb2JsZW0KCldIWSBUSElTIEVYSVNUUyAo"
    "TC0yNzMpCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tClJFQURNRS5tZCdzIGtleS1kb2N1bWVudHMg"
    "dGFibGUgd2FzIGhhbmQtbWFpbnRhaW5lZCwgYW5kIGEKaGFuZC1tYWludGFpbmVkIGxpc3Qgb2Yg"
    "d2hhdCBpcyBpbiBhIGRpcmVjdG9yeSBpcyBhIGNvcHkgdGhhdCBkcmlmdHMKZnJvbSB0aGUgZGly"
    "ZWN0b3J5LiBUaGF0IGRyaWZ0IGlzIEwtMjcwOiB0aGUgUkVBRE1FIGRlc2NyaWJlZCBhIGdhbGxl"
    "cnkKdGhhdCBubyBsb25nZXIgZXhpc3RlZCwgYW5kIG5vYm9keSBjb3VsZCBzZWUgaXQgZnJvbSBp"
    "bnNpZGUgdGhlIFJFQURNRS4KClRvbnkncyBwcm9wb3NhbCwgMjAyNi0wOC0zMSwgYW5kIGl0IGlz"
    "IHRoZSByaWdodCBzaGFwZTogbm90IGEgY2hlY2tlcgp0aGF0IGFsYXJtcyBvbiB0aGUgY29weSwg"
    "YnV0IGFuIElOREVYRVIgdGhhdCByZWdlbmVyYXRlcyBpdCAtLSB0aGUgd2F5CnNraWxsc19pbmRl"
    "eC5weSB3cml0ZXMgdGhlIG1hbmlmZXN0IGludG8gUFJPSkVDVF9JTlNUUlVDVElPTlMubWQgYW5k"
    "CmxlZGdlcl9pbmRleC5weSB3cml0ZXMgdGhlIElOREVYIGludG8gTEVER0VSX0NPTlNPTElEQVRF"
    "RC5tZC4gRml4IHRoZQpwcm9kdWNlciwgbm90IHRoZSBjb25zdW1lci4KClRIRSBERVNJR046IEVB"
    "Q0ggRE9DVU1FTlQgREVDTEFSRVMgSVRTRUxGCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t"
    "LS0tLS0tLS0tLS0tClRoZSBwdXJwb3NlIHRleHQgbGl2ZXMgaW4gdGhlIGRvY3VtZW50IGl0IGRl"
    "c2NyaWJlcywgbm90IGluIHRoaXMgdG9vbAphbmQgbm90IGluIHRoZSBSRUFETUUuIFRoYXQgaXMg"
    "ZGVsaWJlcmF0ZSwgYW5kIGl0IGlzIGNvcGllZCBmcm9tCnNraWxsc19pbmRleC5weTogaXRzIGVk"
    "aXRvcmlhbCBjb2x1bW4gbGl2ZXMgaW4gZWFjaCBza2lsbCdzIG93bgpmcm9udG1hdHRlciwgc28g"
    "VG9ueSBrZWVwcyBjb250cm9sIG9mIHRoZSB3b3JkaW5nIHdoaWxlIHRoZSB0YXJnZXQgZmlsZQpz"
    "dGF5cyBnZW5lcmF0ZWQuIEEgZGljdCBvZiBkZXNjcmlwdGlvbnMgaW5zaWRlIHRoaXMgc2NyaXB0"
    "IHdvdWxkIGJlIHRoZQpzaGFkb3cgc3RvcmUgdGhhdCBtb2R1bGVfYXRsYXMucHkgYWxyZWFkeSBk"
    "ZWxldGVkIHdoZW4gUk9MRV9NQVAgYmVjYW1lIGEKcmVnZW5lcmF0ZWQgbWlycm9yLgoKICAgIE1h"
    "cmtkb3duOiAgPCEtLSBEb2MtS2luZDogPGtpbmQ+IHwgPG9uZS1saW5lIHB1cnBvc2U+IC0tPgog"
    "ICAgVGV4dDogICAgICAjIERvYy1LaW5kOiA8a2luZD4gfCA8b25lLWxpbmUgcHVycG9zZT4KClRo"
    "ZSB0YWcgbWF5IHNpdCBhbnl3aGVyZSBpbiB0aGUgZmlyc3QgNDAgbGluZXMuIEluIG1hcmtkb3du"
    "IGl0IGlzIGFuCkhUTUwgY29tbWVudCwgc28gaXQgaXMgaW52aXNpYmxlIHdoZW4gR2l0SHViIHJl"
    "bmRlcnMgdGhlIHBhZ2UuCgpUSFJFRSBLSU5EUywgQU5EIFRIRSBESVNUSU5DVElPTiBJUyBUSEUg"
    "UE9JTlQKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgICBn"
    "ZW5lcmF0ZWQgICAgICAgd3JpdHRlbiBlbnRpcmVseSBieSBhIHRvb2wuIEhhbmQtZWRpdGluZyBp"
    "dCBpcyBhbgogICAgICAgICAgICAgICAgICAgIGVycm9yOiB0aGUgbmV4dCBydW4gZGVzdHJveXMg"
    "dGhlIGVkaXQuCiAgICB6b25lZCAgICAgICAgICAgaGFuZC13cml0dGVuIHByb3NlIGFyb3VuZCBh"
    "IG1hcmtlciB6b25lIGEgdG9vbAogICAgICAgICAgICAgICAgICAgIHJlZ2VuZXJhdGVzLiBFZGl0"
    "IHRoZSBwcm9zZSwgbmV2ZXIgdGhlIHpvbmUuCiAgICBoYW5kICAgICAgICAgICAgaGFuZC13cml0"
    "dGVuIHRocm91Z2hvdXQuCgpOb3RoaW5nIGluIGVpdGhlciByZXBvc2l0b3J5IHJlY29yZGVkIHRo"
    "YXQgZGlzdGluY3Rpb24gYmVmb3JlLCBhbmQgdGhlCm9ubHkgd2FybmluZyBhZ2FpbnN0IGhhbmQt"
    "ZWRpdGluZyBhIGdlbmVyYXRlZCBmaWxlIGxpdmVkIGluc2lkZSB0aGUgZmlsZS4KCk1BUktFUlMg"
    "TVVTVCBBTFJFQURZIEVYSVNUCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCklmIFJFQURNRS5t"
    "ZCBoYXMgbm8gbWFya2VyIHpvbmUgdGhpcyByZXBvcnRzIGFuZCBleGl0cyBXSVRIT1VUIHdyaXRp"
    "bmcuClRoYXQgaXMgc2tpbGxzX2luZGV4LnB5J3MgYmVoYXZpb3VyIHJhdGhlciB0aGFuIGxlZGdl"
    "cl9pbmRleC5weSdzCmZhbGxiYWNrIGluc2VydCwgYW5kIG9uIHB1cnBvc2U6IGd1ZXNzaW5nIHdo"
    "ZXJlIGEgdGFibGUgYmVsb25ncyBpbiBhCnByb3NlIGRvY3VtZW50IGlzIHdvcnNlIHRoYW4gbm90"
    "IHdyaXRpbmcgb25lLgoKVU5UQUdHRUQgRE9DVU1FTlRTIEFSRSBSRVBPUlRFRCwgTkVWRVIgRFJP"
    "UFBFRAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCkEgZG9j"
    "dW1lbnQgd2l0aCBubyB0YWcgc3RpbGwgYXBwZWFycyBpbiB0aGUgdGFibGUsIG1hcmtlZCB1bnRh"
    "Z2dlZCwgYW5kCmlzIG5hbWVkIGluIHRoZSBzdW1tYXJ5LiBTaWxlbmNlIGFib3V0IHNvbWV0aGlu"
    "ZyB1bmV4YW1pbmVkIGlzIHRoZQpmYWlsdXJlIG1vZGUgdGhpcyBwcm9qZWN0IGhhcyBhIGdhdGUg"
    "Zm9yOyBhIHRpZHkgdGFibGUgdGhhdCBxdWlldGx5Cm9taXRzIHdoYXQgaXQgY291bGQgbm90IHJl"
    "YWQgd291bGQgYmUgZXhhY3RseSB0aGF0LgoKUm9sZTogZGV2dG9vbApEb21haW46IGRldl90b29s"
    "cwoKTW9kdWxlIGNyZWF0ZWQ6IFNlcHRlbWJlciAxLCAyMDI2IHdpdGggQW50aHJvcGljJ3MgQ2xh"
    "dWRlIE9wdXMgNS4KIiIiCgppbXBvcnQgcmUKaW1wb3J0IHN5cwpmcm9tIHBhdGhsaWIgaW1wb3J0"
    "IFBhdGgKClNUQVJUID0gJzwhLS0gRE9DLUlOREVYOlNUQVJUIChnZW5lcmF0ZWQgYnkgZG9jX2lu"
    "ZGV4LnB5IC0tIGRvIG5vdCBlZGl0IHRoaXMgem9uZSBieSBoYW5kKSAtLT4nCkVORCA9ICc8IS0t"
    "IERPQy1JTkRFWDpFTkQgLS0+JwoKVEFHX1JFID0gcmUuY29tcGlsZSgKICAgIHInXlxzKig/Ojwh"
    "LS18IylccypEb2MtS2luZDpccyooW2Etei1dKylccypcfFxzKiguKz8pXHMqKD86LS0+KT9ccyok"
    "JywKICAgIHJlLk1VTFRJTElORSkKCktJTkRfTEFCRUwgPSB7CiAgICAnZ2VuZXJhdGVkJzogJ2dl"
    "bmVyYXRlZCcsCiAgICAnem9uZWQnOiAnaGFuZCArIGdlbmVyYXRlZCB6b25lJywKICAgICdoYW5k"
    "JzogJ2hhbmQtd3JpdHRlbicsCn0KCktJTkRfT1JERVIgPSB7J3pvbmVkJzogMCwgJ2hhbmQnOiAx"
    "LCAnZ2VuZXJhdGVkJzogMiwgJz8nOiAzfQoKU0NBTl9TVUZGSVhFUyA9ICgnLm1kJywgJy50eHQn"
    "KQpUQUdfU0NBTl9MSU5FUyA9IDQwCgoKZGVmIHJlYWRfdGFnKHBhdGgpOgogICAgIiIiUmV0dXJu"
    "IChraW5kLCBwdXJwb3NlKSBvciAoTm9uZSwgTm9uZSkuIFJlYWRzIHRoZSBoZWFkIG9ubHkuIiIi"
    "CiAgICB0cnk6CiAgICAgICAgd2l0aCBvcGVuKHBhdGgsICdyJywgZW5jb2Rpbmc9J3V0Zi04Jywg"
    "ZXJyb3JzPSdyZXBsYWNlJykgYXMgZmg6CiAgICAgICAgICAgIGhlYWQgPSAnJy5qb2luKGZoLnJl"
    "YWRsaW5lKCkgZm9yIF8gaW4gcmFuZ2UoVEFHX1NDQU5fTElORVMpKQogICAgZXhjZXB0IE9TRXJy"
    "b3IgYXMgZToKICAgICAgICByZXR1cm4gTm9uZSwgJ1VOUkVBREFCTEU6ICVzJyAlIGUKICAgIG0g"
    "PSBUQUdfUkUuc2VhcmNoKGhlYWQpCiAgICBpZiBub3QgbToKICAgICAgICByZXR1cm4gTm9uZSwg"
    "Tm9uZQogICAga2luZCA9IG0uZ3JvdXAoMSkuc3RyaXAoKQogICAgcmV0dXJuIChraW5kIGlmIGtp"
    "bmQgaW4gS0lORF9MQUJFTCBlbHNlICc/JyksIG0uZ3JvdXAoMikuc3RyaXAoKQoKCmRlZiBjb2xs"
    "ZWN0KHJvb3QpOgogICAgZG9jcyA9IFtdCiAgICBmb3IgcCBpbiBzb3J0ZWQocm9vdC5pdGVyZGly"
    "KCkpOgogICAgICAgIGlmIG5vdCBwLmlzX2ZpbGUoKSBvciBwLnN1ZmZpeC5sb3dlcigpIG5vdCBp"
    "biBTQ0FOX1NVRkZJWEVTOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIGtpbmQsIHB1cnBv"
    "c2UgPSByZWFkX3RhZyhwKQogICAgICAgIGRvY3MuYXBwZW5kKChwLm5hbWUsIGtpbmQsIHB1cnBv"
    "c2UpKQogICAgcmV0dXJuIGRvY3MKCgpkZWYgcmVuZGVyKGRvY3MpOgogICAgcm93cyA9IFsKICAg"
    "ICAgICAnfCBEb2N1bWVudCB8IEtpbmQgfCBXaGF0IGl0IGlzIGZvciB8JywKICAgICAgICAnfC0t"
    "LXwtLS18LS0tfCcsCiAgICBdCiAgICBmb3IgbmFtZSwga2luZCwgcHVycG9zZSBpbiBzb3J0ZWQo"
    "CiAgICAgICAgICAgIGRvY3MsIGtleT1sYW1iZGEgZDogKEtJTkRfT1JERVIuZ2V0KGRbMV0gb3Ig"
    "Jz8nLCAzKSwgZFswXS5sb3dlcigpKSk6CiAgICAgICAgbGFiZWwgPSBLSU5EX0xBQkVMLmdldChr"
    "aW5kLCAnKip1bnRhZ2dlZCoqJykKICAgICAgICB0ZXh0ID0gcHVycG9zZSBvciAnX25vIERvYy1L"
    "aW5kIHRhZzsgYWRkIG9uZSB0byBkZXNjcmliZSBpdCBoZXJlXycKICAgICAgICByb3dzLmFwcGVu"
    "ZCgnfCBbJXNdKCVzKSB8ICVzIHwgJXMgfCcgJSAobmFtZSwgbmFtZSwgbGFiZWwsIHRleHQpKQog"
    "ICAgcmV0dXJuICdcbicuam9pbihyb3dzKQoKCmRlZiBtYWluKCk6CiAgICBjaGVja19vbmx5ID0g"
    "Jy0tY2hlY2snIGluIHN5cy5hcmd2WzE6XQogICAgcm9vdCA9IFBhdGgoX19maWxlX18pLnJlc29s"
    "dmUoKS5wYXJlbnQKICAgIHJlYWRtZSA9IHJvb3QgLyAnUkVBRE1FLm1kJwoKICAgIGlmIG5vdCBy"
    "ZWFkbWUuaXNfZmlsZSgpOgogICAgICAgIHByaW50KCdDQU5OT1QgUlVOOiBSRUFETUUubWQgbm90"
    "IGZvdW5kIGluICVzJyAlIHJvb3QpCiAgICAgICAgcmV0dXJuIDIKCiAgICBkb2NzID0gY29sbGVj"
    "dChyb290KQogICAgdW50YWdnZWQgPSBbbiBmb3IgbiwgaywgcCBpbiBkb2NzIGlmIGsgaXMgTm9u"
    "ZV0KICAgIHVua25vd24gPSBbKG4sIHApIGZvciBuLCBrLCBwIGluIGRvY3MgaWYgayA9PSAnPydd"
    "CgogICAgdGV4dCA9IHJlYWRtZS5yZWFkX3RleHQoZW5jb2Rpbmc9J3V0Zi04JykKICAgIGlmIFNU"
    "QVJUIG5vdCBpbiB0ZXh0IG9yIEVORCBub3QgaW4gdGV4dDoKICAgICAgICBwcmludCgnQ0FOTk9U"
    "IFJVTjogUkVBRE1FLm1kIGhhcyBubyBET0MtSU5ERVggbWFya2VyIHpvbmUuJykKICAgICAgICBw"
    "cmludCgnICBFeHBlY3RlZCB0aGVzZSB0d28gbGluZXMsIGluIHRoaXMgb3JkZXI6JykKICAgICAg"
    "ICBwcmludCgnICAgICVzJyAlIFNUQVJUKQogICAgICAgIHByaW50KCcgICAgJXMnICUgRU5EKQog"
    "ICAgICAgIHByaW50KCcgIE5vdGhpbmcgd2FzIHdyaXR0ZW4uIEd1ZXNzaW5nIGFuIGluc2VydGlv"
    "biBwb2ludCBpbiBhIHByb3NlJykKICAgICAgICBwcmludCgnICBkb2N1bWVudCBpcyB3b3JzZSB0"
    "aGFuIG5vdCB3cml0aW5nIG9uZS4nKQogICAgICAgIHJldHVybiAyCgogICAgdGFibGUgPSByZW5k"
    "ZXIoZG9jcykKICAgIG5ld196b25lID0gU1RBUlQgKyAnXG4nICsgdGFibGUgKyAnXG4nICsgRU5E"
    "CiAgICBwYXR0ZXJuID0gcmUuY29tcGlsZShyZS5lc2NhcGUoU1RBUlQpICsgcicuKj8nICsgcmUu"
    "ZXNjYXBlKEVORCksIHJlLkRPVEFMTCkKICAgIHVwZGF0ZWQgPSBwYXR0ZXJuLnN1YihsYW1iZGEg"
    "X206IG5ld196b25lLCB0ZXh0LCBjb3VudD0xKQoKICAgIGNoYW5nZWQgPSB1cGRhdGVkICE9IHRl"
    "eHQKICAgIGlmIGNoYW5nZWQgYW5kIG5vdCBjaGVja19vbmx5OgogICAgICAgIHdpdGggb3Blbihy"
    "ZWFkbWUsICd3JywgZW5jb2Rpbmc9J3V0Zi04JywgbmV3bGluZT0nXG4nKSBhcyBmaDoKICAgICAg"
    "ICAgICAgZmgud3JpdGUodXBkYXRlZCkKCiAgICAjIC0tLS0gcmVwb3J0OiBuYW1lcywgbm90IG9u"
    "bHkgY291bnRzIChBIFJlcG9ydCBOYW1lcyBJdHMgSXRlbXMpIC0tLS0KICAgIGJ5X2tpbmQgPSB7"
    "fQogICAgZm9yIG5hbWUsIGtpbmQsIF9wIGluIGRvY3M6CiAgICAgICAgYnlfa2luZC5zZXRkZWZh"
    "dWx0KGtpbmQgb3IgJ3VudGFnZ2VkJywgW10pLmFwcGVuZChuYW1lKQoKICAgIHByaW50KCclZCBy"
    "b290IGRvY3VtZW50KHMpIGluZGV4ZWQ6JyAlIGxlbihkb2NzKSkKICAgIGZvciBraW5kIGluICgn"
    "em9uZWQnLCAnaGFuZCcsICdnZW5lcmF0ZWQnLCAnPycsICd1bnRhZ2dlZCcpOgogICAgICAgIG5h"
    "bWVzID0gYnlfa2luZC5nZXQoa2luZCkKICAgICAgICBpZiBuYW1lczoKICAgICAgICAgICAgcHJp"
    "bnQoJyAgJS0yMnMgJWQgICVzJwogICAgICAgICAgICAgICAgICAlIChLSU5EX0xBQkVMLmdldChr"
    "aW5kLCBraW5kKSwgbGVuKG5hbWVzKSwgJywgJy5qb2luKG5hbWVzKSkpCgogICAgcHJvYmxlbXMg"
    "PSAwCiAgICBpZiB1bmtub3duOgogICAgICAgIHByb2JsZW1zICs9IGxlbih1bmtub3duKQogICAg"
    "ICAgIHByaW50KCcnKQogICAgICAgIHByaW50KCdVTlJFQ09HTklTRUQgRG9jLUtpbmQgdmFsdWUg"
    "KCVkKTonICUgbGVuKHVua25vd24pKQogICAgICAgIGZvciBuLCBfcCBpbiB1bmtub3duOgogICAg"
    "ICAgICAgICBwcmludCgnICAgICVzJyAlIG4pCiAgICAgICAgcHJpbnQoJyAgVmFsaWQga2luZHM6"
    "ICVzJyAlICcsICcuam9pbihzb3J0ZWQoS0lORF9MQUJFTCkpKQoKICAgIGlmIHVudGFnZ2VkOgog"
    "ICAgICAgIHByaW50KCcnKQogICAgICAgIHByaW50KCdOTyBEb2MtS2luZCBUQUcgKCVkKTogJXMn"
    "ICUgKGxlbih1bnRhZ2dlZCksICcsICcuam9pbih1bnRhZ2dlZCkpKQogICAgICAgIHByaW50KCcg"
    "IFRoZXNlIGFwcGVhciBpbiB0aGUgdGFibGUgbWFya2VkIHVudGFnZ2VkIHJhdGhlciB0aGFuIGJl"
    "aW5nJykKICAgICAgICBwcmludCgnICBkcm9wcGVkIGZyb20gaXQuIEEgZG9jdW1lbnQgYSB0b29s"
    "IGNvdWxkIG5vdCByZWFkIGlzIHRoZScpCiAgICAgICAgcHJpbnQoJyAgdGhpbmcgbW9zdCB3b3J0"
    "aCBzYXlpbmcgb3V0IGxvdWQuJykKCiAgICBwcmludCgnJykKICAgIGlmIGNoZWNrX29ubHk6CiAg"
    "ICAgICAgaWYgY2hhbmdlZDoKICAgICAgICAgICAgcHJvYmxlbXMgKz0gMQogICAgICAgICAgICBw"
    "cmludCgnU1RBTEU6IFJFQURNRS5tZFwncyB0YWJsZSBkb2VzIG5vdCBtYXRjaCB0aGUgZG9jdW1l"
    "bnRzLicpCiAgICAgICAgICAgIHByaW50KCcgIFJ1bjogcHl0aG9uIGRvY19pbmRleC5weScpCiAg"
    "ICAgICAgZWxzZToKICAgICAgICAgICAgcHJpbnQoJ09LOiBSRUFETUUubWRcJ3MgdGFibGUgbWF0"
    "Y2hlcyB0aGUgJWQgcm9vdCBkb2N1bWVudChzKS4nCiAgICAgICAgICAgICAgICAgICUgbGVuKGRv"
    "Y3MpKQogICAgICAgIHJldHVybiAxIGlmIHByb2JsZW1zIGVsc2UgMAoKICAgIGlmIGNoYW5nZWQ6"
    "CiAgICAgICAgcHJpbnQoJ0RvY3VtZW50IGluZGV4IHJlZ2VuZXJhdGVkICglZCBkb2N1bWVudHMp"
    "IGluIFJFQURNRS5tZC4nICUgbGVuKGRvY3MpKQogICAgZWxzZToKICAgICAgICBwcmludCgnRG9j"
    "dW1lbnQgaW5kZXggYWxyZWFkeSBtYXRjaGVkIGFsbCAlZCBkb2N1bWVudChzKS4nICUgbGVuKGRv"
    "Y3MpKQogICAgcmV0dXJuIDAKCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgc3lzLmV4"
    "aXQobWFpbigpKQo="
)
DOC_INDEX_MD5 = "dcce3a5b425672ace7e2d12c2020b5bf"

TAGS = {
    'ADDING_OBJECTS_GUIDE.md': '<!-- Doc-Kind: hand | Step by step for adding a new celestial object. -->',
    'LEDGER_CONSOLIDATED.md': '<!-- Doc-Kind: zoned | The running ledger: every open and closed item under a stable handle, with the decisions behind it. Carries a generated INDEX. -->',
    'LICENSE.md': '<!-- Doc-Kind: hand | MIT license. -->',
    'PROJECT_INSTRUCTIONS.md': '<!-- Doc-Kind: zoned | The protocol. How a session is run, which checks are load-bearing, and why. Carries the generated skill manifest. -->',
    'PROJECT_ORIGIN.md': "<!-- Doc-Kind: hand | How the project started, in Tony's own words. -->",
    'README.md': '<!-- Doc-Kind: zoned | The front door: what the project is, where its pieces are, and how the work is kept correct. -->',
    'RUNNING_A_PATCH_FILE.md': '<!-- Doc-Kind: hand | How to run a delivered patch script, and what its guards mean. -->',
    'requirements.txt': '# Doc-Kind: hand | Annotated dependency spec, including the kaleido 0.2.1 pin and the Plotly 5.x constraint.',
}

OLD_SECTION = "### Key documents\n\n| Document | What it is for |\n|---|---|\n| [MODULE_INDEX.md](MODULE_INDEX.md) | Every module, grouped by role, described from its own docstring. Start here to find where something lives. |\n| [MODULE_ATLAS.md](MODULE_ATLAS.md) | The deep version: dependencies, consumers and public functions per module, written for AI-assisted queries about the codebase. Generated from the same scan as MODULE_INDEX.md by `module_atlas.py`, so the two cannot disagree. Its counts are the project's canonical measure of scale -- trust them over any number written by hand anywhere, including in this file. |\n| [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) | The protocol. How a session is run, which checks are load-bearing, and why. See Part 2. |\n| [LEDGER_CONSOLIDATED.md](LEDGER_CONSOLIDATED.md) | The running ledger: every open and closed item under a stable handle, with the decisions behind it. The project's institutional memory. |\n| [PROVENANCE_AUDIT.md](PROVENANCE_AUDIT.md) | The citation audit of every numeric claim in the codebase, regenerated by the scanner. |\n| [PROJECT_ORIGIN.md](PROJECT_ORIGIN.md) | How the project started, in Tony's own words. |\n| [ADDING_OBJECTS_GUIDE.md](ADDING_OBJECTS_GUIDE.md) | Step by step for adding a new celestial object. |\n| [DATA_INVENTORY.md](DATA_INVENTORY.md) | What a mature local data store looks like. Generated. |\n| [documentation/ORBITAL_MECHANICS_README_v3_3.md](documentation/ORBITAL_MECHANICS_README_v3_3.md) | Orbital mechanics conventions: osculating versus mean elements, solution-level TP, reference frames, epochs. |\n| [documentation/climate_readme.md](documentation/climate_readme.md) | The Earth system and climate data hub. |\n| [documentation/wet_bulb_temperature_readme.md](documentation/wet_bulb_temperature_readme.md) | Forensic heat wave analysis. |\n| [documentation/social_media_readme.md](documentation/social_media_readme.md) | The 9:16 portrait export. |\n\n"

NEW_SECTION = '### Key documents\n\nThe table below is GENERATED by `doc_index.py` from the documents\nthemselves -- each one carries a one-line `Doc-Kind` tag saying what it is\nand what it is for. Do not edit the rows by hand; edit the tag in the\ndocument, and the next maintenance run rewrites the table. The Kind\ncolumn matters: hand-editing a generated document is an error, because\nthe next run of its generator destroys the edit.\n\nDocuments in `documentation/` are not indexed here. Start with\n[MODULE_INDEX.md](MODULE_INDEX.md) for the code and the deep-dive links\nfurther down this file for the rest.\n\n<!-- DOC-INDEX:START (generated by doc_index.py -- do not edit this zone by hand) -->\n| Document | Kind | What it is for |\n|---|---|---|\n<!-- DOC-INDEX:END -->\n\nThe deep-dive documents, which live in `documentation/`:\n\n| Document | What it is for |\n|---|---|\n| [documentation/ORBITAL_MECHANICS_README_v3_3.md](documentation/ORBITAL_MECHANICS_README_v3_3.md) | Orbital mechanics conventions: osculating versus mean elements, solution-level TP, reference frames, epochs. |\n| [documentation/climate_readme.md](documentation/climate_readme.md) | The Earth system and climate data hub. |\n| [documentation/wet_bulb_temperature_readme.md](documentation/wet_bulb_temperature_readme.md) | Forensic heat wave analysis. |\n| [documentation/social_media_readme.md](documentation/social_media_readme.md) | The 9:16 portrait export. |\n\n'

OLD_RUNNER_ROW = """    ('Data inventory',  ['data_inventory.py'],
     ['DATA_INVENTORY.md']),
]"""

NEW_RUNNER_ROW = """    ('Data inventory',  ['data_inventory.py'],
     ['DATA_INVENTORY.md']),
    # L-273: rewrites README.md's key-documents table from the Doc-Kind
    # tag each document carries. A generator rather than a checker on
    # Tony's ruling: a checker would leave the hand-maintained copy in
    # place and only make its drift loud, which is the opposite of
    # fixing the producer.
    ('Document index',  ['doc_index.py'],
     ['README.md']),
]"""


def fail(msg):
    print("")
    print("FAILURE: " + msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def read_norm(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    return raw.replace(b"\r\n", b"\n"), b"\r\n" in raw


def main():
    if not os.path.isfile("PROJECT_INSTRUCTIONS.md"):
        fail("run this from the ORRERY repo root (the folder holding "
             "PROJECT_INSTRUCTIONS.md). Current folder: " + os.getcwd())

    if os.path.exists(NEWTOOL):
        fail(NEWTOOL + " already exists. This patch has already run, or "
             "that name is taken.")

    # ---- all guards verified BEFORE any write ----
    loaded = {}
    for path, want in sorted(FINGERPRINTS.items()):
        if not os.path.isfile(path):
            fail(path + " not found in " + os.getcwd())
        content, was_crlf = read_norm(path)
        got = hashlib.md5(content).hexdigest()
        if got != want:
            fail("BASE MOVED. " + path + " fingerprints " + got +
                 ", expected " + want + ".\n"
                 "  Establish WHAT differs before assuming an edit was made:\n"
                 "  a size delta of about one byte per line means line\n"
                 "  endings, not content.")
        loaded[path] = (content.decode("utf-8", "strict"), was_crlf)
    print("ok  %d/%d base fingerprints match" % (len(FINGERPRINTS),
                                                len(FINGERPRINTS)))

    tool_bytes = base64.b64decode(DOC_INDEX_B64)
    if hashlib.md5(tool_bytes).hexdigest() != DOC_INDEX_MD5:
        fail("the embedded doc_index.py does not match its own fingerprint; "
             "this script is damaged. Do not re-run it.")

    # ---- anchors ----
    if loaded[README][0].count(OLD_SECTION) != 1:
        fail("the key-documents section anchor was not found exactly once "
             "in README.md.")
    if loaded[RUNNER][0].count(OLD_RUNNER_ROW) != 1:
        fail("the GENERATORS anchor was not found exactly once in " + RUNNER)
    for path in TAGS:
        if "Doc-Kind:" in loaded[path][0]:
            fail(path + " already carries a Doc-Kind tag.")
    print("ok  2 section anchors found, and no document is already tagged")

    # ---- build every result in memory first ----
    results = {}

    text, crlf = loaded[README]
    text = text.replace(OLD_SECTION, NEW_SECTION, 1)
    results[README] = (TAGS[README] + "\n" + text, crlf)

    text, crlf = loaded[RUNNER]
    results[RUNNER] = (text.replace(OLD_RUNNER_ROW, NEW_RUNNER_ROW, 1), crlf)

    for path, tag in TAGS.items():
        if path == README:
            continue
        text, crlf = loaded[path]
        results[path] = (tag + "\n" + text, crlf)

    # The ASCII gate governs the text this patch INSERTS, not the
    # documents it inserts into: ADDING_OBJECTS_GUIDE.md,
    # PROJECT_ORIGIN.md and requirements.txt hold em dashes and a curly
    # apostrophe in Tony's own prose, preserved here byte-exactly.
    for chunk in list(TAGS.values()) + [NEW_SECTION, NEW_RUNNER_ROW]:
        bad = [c for c in chunk if ord(c) > 127]
        if bad:
            fail("inserted text holds %d non-ASCII character(s)." % len(bad))
    print("ok  inserted text is ASCII; existing UTF-8 preserved byte-exactly")

    # ---- writes ----
    with open(NEWTOOL, "wb") as fh:
        fh.write(tool_bytes)
    print("ok  wrote %s (%d bytes)" % (NEWTOOL, len(tool_bytes)))

    for path in sorted(results):
        text, crlf = results[path]
        out = text.encode("utf-8")
        if crlf:
            out = out.replace(b"\n", b"\r\n")
        with open(path, "wb") as fh:
            fh.write(out)
        print("ok  wrote %s (%d bytes)" % (path, len(out)))

    # ---- verification: read back from disk ----
    problems = []

    back, _ = read_norm(NEWTOOL)
    if hashlib.md5(back).hexdigest() != DOC_INDEX_MD5:
        problems.append("doc_index.py on disk does not match the intended text")

    back, _ = read_norm(README)
    rt = back.decode("utf-8", "replace")
    if "DOC-INDEX:START" not in rt or "DOC-INDEX:END" not in rt:
        problems.append("README.md has no DOC-INDEX marker zone")
    if "| [MODULE_INDEX.md](MODULE_INDEX.md) | Every module, grouped" in rt:
        problems.append("the old hand-maintained table survived in README.md")

    back, _ = read_norm(RUNNER)
    if "'Document index'" not in back.decode("utf-8", "replace"):
        problems.append("the runner GENERATORS row is missing")

    tagged, missing = [], []
    for path in TAGS:
        back, _ = read_norm(path)
        (tagged if "Doc-Kind:" in back.decode("utf-8", "replace")
         else missing).append(path)
    if missing:
        problems.append("tag missing from: " + ", ".join(sorted(missing)))

    import py_compile
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        for p in (NEWTOOL, RUNNER):
            try:
                py_compile.compile(p, doraise=True,
                                   cfile=os.path.join(td, "x.pyc"))
            except py_compile.PyCompileError as e:
                problems.append("does not compile: %s -- %s" % (p, e))

    if problems:
        print("")
        print("VERIFICATION FAILED after writing:")
        for p in problems:
            print("  - " + p)
        print("Undo is Discard Changes in GitHub Desktop.")
        sys.exit(1)

    print("ok  verified: zone present, old table gone, %d/%d documents "
          "tagged, both scripts compile" % (len(tagged), len(TAGS)))
    print("")
    print("patch applied. The table is still EMPTY -- the marker zone")
    print("exists but nothing has filled it yet. That is the next step.")
    print("")
    print("NEXT STEPS")
    print("  1. Run: python doc_index.py")
    print("     It fills the table and NAMES the five generated documents")
    print("     it could not read a tag from. That naming is intended.")
    print("  2. Read the table in README.md.")
    print("  3. Run: python orrery_maintenance_run.py")
    print("     Document index now appears among the generators and should")
    print("     report no change, because step 1 already wrote it.")
    print("  4. Commit everything plus this script, after moving it into")
    print("     documentation/.")
    print("")
    print("REMAINING HALF OF L-273, and it is one line per file:")
    print("  module_atlas.py, data_inventory.py, provenance_scanner.py and")
    print("  worksheet_checker.py each emit a Doc-Kind tag into what they")
    print("  write. Until then those five documents show as untagged, by")
    print("  name, on every run.")


if __name__ == "__main__":
    main()
