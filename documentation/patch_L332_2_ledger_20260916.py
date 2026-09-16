#!/usr/bin/env python3
"""
patch_L332_2_ledger_20260916.py -- ORRERY repo, LEDGER_CONSOLIDATED.md only.

Run: save this file in the ORRERY repo root (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L332_2_ledger_20260916.py
Then:  python ledger_index.py LEDGER_CONSOLIDATED.md
       FIRST RUN prints "CONSISTENCY PROBLEMS" with twelve [auto-fix]
       lines -- two per closed item -- then "Retagged 6 block(s) ...
       physically moved 6 block(s)". That is the tool filing the six
       closed items into section C, not an error. Run it ONCE MORE:
       "OK: 328 L-blocks parsed, no consistency problems."

Built on orrery d99d8db1d3bac407e1d3891b9c6b016d839898c7
at https://github.com/tonylquintanilla/palomas_orrery
(gallery read at b375cfe1dd9901a133d7a811f6ccba0d48167975
at https://github.com/tonylquintanilla/tonyquintanilla.github.io).

Independent of patch_L332_1: either can run first. The guard hashes the
ledger OUTSIDE its INDEX zone, because ledger_index.py rewrites the zone.

WHAT IT DOES:
  - Header: the three ledger patches of 2026-09-14, -15 and -16 edited
    this file without a "Module updated" stamp. Their stamps are added,
    marked as recorded later, plus this session's stamp.
  - CLOSES five items whose Gap is met, each checked at HEAD d99d8db1:
      L-226  safe-file-editing 1.8 (the skill is 1.11; every session
             since has loaded it)
      L-232  served constants nothing checks (the runner's Store drift
             follows every orrery_constant pointer by name -- built as
             L-236, widened by L-291 and L-305; the residue, that the
             `source` TEXT is unchecked, moves to L-266)
      L-271  patch scripts wrote backups (rule in the skill, both ignore
             rules widened, backups swept; its two Gaps are facts)
      L-277  site store re-anchored (patch archived, README carries the
             three rows, both checkers green at d99d8db1)
      L-278  Plotly re-entry (in gallery-assembler 1.2, as its body says)
  - L-332 records the build (interactive-exhibit 1.3,
    orrery-coding-conventions 1.9, protocol v3.60) and closes; the
    reinstall obligation travels in the handoff.
  - L-331's Gap gains the hover-budget CEILING (17), which was floating
    in L-231's body and two handoffs.
  - L-273 gains a Gap: the orrery's four generators now emit their
    Doc-Kind tag (patch_L332_1); the gallery half is unbuilt.
  - L-219's Gap said the next safe-file-editing would be 1.7; it is 1.12.
  - L-333 OPENED: the master plan's two companion summaries are stale
    (Aug 19 and Aug 29; Earth shipped Sept 10).

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
EXPECTED = '196e08397d3677687fb4ceacc58575e5'   # md5 of LF content with the INDEX zone removed
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

EDITS = [

# ---- header stamps -------------------------------------------------------
(b"""built on bfc0505e.
Review and RICE update Tony 6-21-2026
""",
b"""built on bfc0505e.
Module updated: September 14, 2026 with Anthropic's Claude Opus 5
(L-305 item 7 recorded; L-327, L-328 opened; L-329 opened and closed
with protocol v3.59), built on 773e5c2d. Recorded 2026-09-16 by a later
session: that patch edited this file without stamping it.
Module updated: September 15, 2026 with Anthropic's Claude Opus 5
(L-231 built for Earth's belts; L-305 items 5 and 6b built; L-330
opened), built on 72058200. Recorded 2026-09-16 by a later session:
that patch edited this file without stamping it.
Module updated: September 16, 2026 with Anthropic's Claude Opus 5
(L-316 rounds 3 and 4 and L-318 rounds 3 to 6 on Tony's Mode 5; L-331
and L-332 opened; L-267's G2 amended), built on cce6a933. Recorded
later the same day by a following session: that patch edited this file
without stamping it.
Module updated: September 16, 2026 with Anthropic's Claude Opus 5
(ledger review: L-226, L-232, L-271, L-277 and L-278 closed, each
verified done at HEAD; L-332 built -- interactive-exhibit 1.3,
orrery-coding-conventions 1.9, protocol v3.60 -- and closed; L-273's
orrery generators emit their tag; L-333 opened; the three stamps
above added), built on d99d8db1.
Review and RICE update Tony 6-21-2026
"""),

# ---- L-226 close ---------------------------------------------------------
(b"""<!-- L:226 status:OPEN upd:2026-08-23 section:A flag: rice:3/3/90/1 -->
""",
b"""<!-- L:226 status:DONE upd:2026-09-16 section:A flag: rice:3/3/90/1 -->
"""),
(b"""- **Ref:** `skills/safe-file-editing/SKILL.md` v1.8;""",
b"""- **CLOSED 2026-09-16.** The Gap was the next session confirming its
  loaded copy reads 1.8. The skill has since gone to 1.9, 1.10 and 1.11
  (L-315), each confirmed by the sessions that followed, and the
  2026-09-16 session loaded 1.11 and matched the manifest. Both
  rulings are in the skill's Encoding Gate and The Correction Does Not
  Travel sections. Nothing recorded here as not done remains; the
  entry sat open for three weeks because no session closed a bump
  item after confirming the load. [verified @ `d99d8db1`]
- **Ref:** `skills/safe-file-editing/SKILL.md` v1.8;"""),

# ---- L-232 close, residue to L-266 --------------------------------------
(b"""<!-- L:232 status:OPEN upd:2026-08-24 section:A flag: rice:3/3/85/2 -->
""",
b"""<!-- L:232 status:DONE upd:2026-09-16 section:A flag: rice:3/3/85/2 -->
"""),
(b"""- **Ref:** gallery `data/objects_config.json`;""",
b"""- **CLOSED 2026-09-16, built under another handle.** The second
  candidate shape above -- make the transport verify each
  `orrery_constant` pointer resolves and matches -- is
  `gallery_maintenance_run.py`'s Store drift check: it fetches
  `constants_new.py` at orrery HEAD, follows every pointer in
  `objects_config.json` by name, and reports MATCH, DRIFT or NOT IN
  STORE per pointer (built as L-236 on 2026-08-25, widened by L-291 for
  Earth radii and by L-305 for the magnetosphere's scalars). The
  sentence "nothing reads JSON in the gallery repo" has been false
  since then. The `source` STRING beside each value -- the citation
  itself -- is still checked by nothing; that residue is re-homed to
  L-266, whose link check is the shape that would reach it. The
  duplicated Earth radius is L-322's (the join moves to the assembler).
  [verified @ gallery `b375cfe1`, `check_store_drift`]
- **Ref:** gallery `data/objects_config.json`;"""),

(b"""- **Ref:** L-265 (what makes it urgent);""",
b"""- **From L-232, closed 2026-09-16:** the gallery's
  `data/objects_config.json` carries a `source` string beside each
  measured value. Store drift checks the VALUE against the orrery by
  pointer; nothing checks the source text, and a URL there is in the
  same position as the roughly 470 in the orrery's Python. Whatever
  shape this item takes should read that file as a second corpus.
- **Ref:** L-265 (what makes it urgent);"""),

# ---- L-271 close ---------------------------------------------------------
(b"""<!-- L:271 status:OPEN upd:2026-08-31 section:A flag: rice:4/3/95/1 -->
""",
b"""<!-- L:271 status:DONE upd:2026-09-16 section:A flag: rice:4/3/95/1 -->
"""),
(b"""- **Ref:** L-236 (the runner that first surfaced backup churn);""",
b"""- **CLOSED 2026-09-16.** Everything with a build behind it is built and
  checked at HEAD: Git Is the Backup in safe-file-editing 1.10; both
  ignore rules carry the three shapes (`*.bak`, `*.bak[0-9]`,
  `*.bak_*`) -- orrery `.gitignore` lines 36-38, gallery lines 10-12;
  no tracked `*.bak*` file in either tree. The two Gaps above are
  struck, each for the reason it states: the spent scripts are records
  and are not rewritten; the gallery has no ledger and this block is
  the cross-repo record. Neither is work for anyone.
  [verified @ orrery `d99d8db1`, gallery `b375cfe1`]
- **Ref:** L-236 (the runner that first surfaced backup churn);"""),

# ---- L-277 close ---------------------------------------------------------
(b"""<!-- L:277 status:OPEN upd:2026-09-03 section:A flag: rice:3/3/90/2 -->
""",
b"""<!-- L:277 status:DONE upd:2026-09-16 section:A flag: rice:3/3/90/2 -->
"""),
(b"""**Ref:** worksheet_keys.py `key_for_site`""",
b"""- **CLOSED 2026-09-16, on the Gap's own three conditions.** The patch
  ran (`documentation/patch_L277_reanchor_site_stores.py`, archived);
  README.md's document table carries the three stores at rows 183-185;
  and both checkers are green at `d99d8db1`, run directly:
  `test_worksheet_keys.py` -- 52 sites minted 52 distinct keys, all
  resolved, 52 pinned keys resolve, 1 retired confirmed gone;
  `test_extractor_pins.py` -- 29 string sites carry the pinned 73 claims
  and 14 instruction drops. The forward cost named above -- L-254's
  slices breaking the store -- is dissolved by (b): the store anchors
  by name now, so a docstring insertion moves nothing.
  [verified @ `d99d8db1`]
**Ref:** worksheet_keys.py `key_for_site`"""),

# ---- L-278 close ---------------------------------------------------------
(b"""<!-- L:278 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/90/1 -->
""",
b"""<!-- L:278 status:DONE upd:2026-09-16 section:A flag: rice:3/3/90/1 -->
"""),
(b"""**Ref:** gallery `6fd6baaf` `interactive.html` the `plotly_click`""",
b"""- **CLOSED 2026-09-16.** The fix shipped 2026-09-02 and the lesson is
  in `skills/gallery-assembler/SKILL.md` as a field note (its own
  Tony-action line above says so, marked DONE the same day); the
  interactive-exhibit skill carries it as a [CRITICAL] rule and points
  here. The item had no Gap and no remaining work; it was open because
  nobody closed it. [verified @ `d99d8db1`, skill 1.3 lines 203-214]
**Ref:** gallery `6fd6baaf` `interactive.html` the `plotly_click`"""),

# ---- L-332 record + close -----------------------------------------------
(b"""<!-- L:332 status:OPEN upd:2026-09-16 section:A flag: rice:2/2/90/1 -->
""",
b"""<!-- L:332 status:DONE upd:2026-09-16 section:A flag: rice:2/2/90/1 -->
"""),
(b"""**Gap:** the skill edit, then `skills_index.py`.
  **Tony-action (do):** reinstall the skill after the bump.
""",
b"""- **BUILT 2026-09-16** by `patch_L332_1_skills_protocol_generators_20260916.py`
  in the orrery, taken before L-331's build (v3.55's ordering).
  interactive-exhibit 1.2 -> 1.3: the drawer and nav-cluster rows of
  the anatomy table rewritten to what the code does at gallery
  `b375cfe1` (`crossApart` / `.nav-cross-apart`, `sunPhonePortrait`,
  the 65 px / 44 px row targets, GO ticking an unticked shell, the
  phone's arrowless box and its knobs); the touch-path section gains
  the soft-break rule and the pick-pass rule; the Mode 5 sequence
  names the drawer target, the phone's box and a marker tap; step 4
  gains the hover budget suite with the note that it does not build
  the Sun room; a new rule, Hover text is written for the visitor;
  three field notes. orrery-coding-conventions 1.8 -> 1.9 (L-331's
  rule as a section, Hover Text Is Written for the Visitor), because a
  convention that is not in the skill a hover session loads does not
  travel, and L-321 is that session. Protocol v3.60 names both and
  why; v3.57 moved down to the history file; `skills_index.py`
  reported the manifest stale on both rows and corrected it. The
  L-316 "still to look at" desktop check is untouched by this.
  [verified in the sandbox on a throwaway copy @ `d99d8db1` + this
  patch: both SKILL.md files parse, the manifest reads 1.3 and 1.9,
  three entries resident, the four-step rule met in one commit]
- **CLOSED 2026-09-16.** The reinstall cannot be verified from inside
  the session that made it; the handoff carries it.
  **Tony-action (do):** reinstall interactive-exhibit and
  orrery-coding-conventions at Settings > Skills. The next session
  confirms its loaded copies read 1.3 and 1.9 before exhibit or hover
  work.
"""),

# ---- L-331 Gap gains the ceiling ------------------------------------------
(b"""**Gap:** the build above, then Mode 5 on the phone in both rooms.
""",
b"""- **Re-homed here 2026-09-16, from L-231's body and the 2026-09-15 and
  -16 handoffs' STILL OPEN lists:** `documentation/smoke_hover_budget.js`
  holds `CEILING = 17` lines per hover, a ratchet that only comes down.
  The plain-language pass above is what shortens the tallest hover;
  when it does, lower the ceiling to the new tallest in the same patch.
  It is still 17 at gallery `b375cfe1`.
- **The rule is in the skills now** (2026-09-16): interactive-exhibit
  1.3, Hover text is written for the visitor; orrery-coding-conventions
  1.9, Hover Text Is Written for the Visitor. L-332 records the bump.
- **The mechanical half BUILT 2026-09-16** by
  `patch_L331_1_sun_hovers_to_panel.py` in the gallery, delivered with
  this patch. `renderStreamerBand` and `renderOortShape` now end their
  hovers with the pointer line; their citations reach the i panel
  through a new `withGatheredSource()`, which collects the source strings
  the config keeps on measured fields (`cusp_radius`, `fade_radius`,
  `inner_radius`, `outer_radius`, `typical_radius`) into the top-level
  `source` that `stampLink` reads. Found building it: the torus and
  clump `note` fields were read by nothing, so their caveats had been
  absent from hover AND panel; they reach the panel now. Each of the
  four hovers carries its caveat in plain words -- the Galactic Tide in
  the wording proposed above, the other three in one sentence each,
  all in a VISITOR_WORDING block for Tony to edit before running.
  `smoke_hover_budget.js` builds the Sun room from the served store;
  its pointer leg fails on the tree before the patch, naming the four,
  and passes after. Both info texts corrected: source is in the panel,
  the magnetopause and bow shock are drawn, the drawer sentence says
  what a tap does. Sandbox at gallery `b375cfe1` + the patch: the
  renderers and the page's inline script parse; hover budget (96
  hovers, ceiling still 17), features, Sun shells and framing suites all
  pass. [render-gated: nothing seen on a phone]
- **Not in that patch, still here:** the plain-language pass over the
  remaining hovers ("served" x14, "sourced" x5, "drawing choice" x5,
  capitalised labels on the magnetopause, bow shock and terminator);
  the Galactic Tide's served `source` string in `objects_config.json`,
  which still reads "DECLARED -- ..." and now shows in the panel's
  Source line; the Moon's hover in `render_orbits.py`.
**Gap:** Mode 5 on the phone in the Sun room for the four hovers and the
panel, and in both rooms for the info text; then the plain-language pass
over the remaining hovers, wording to Tony first; the ceiling comes down
with the tallest hover.
  **Tony-action (decide):** the four VISITOR_WORDING sentences, by
  running the patch as written or editing them first.
"""),

# ---- L-273 Gap ------------------------------------------------------------
(b"""- **Ref:** L-270 (the Gap that raised it);""",
b"""- **Orrery half built 2026-09-16** by `patch_L332_1_...` : `module_atlas.py`
  (both outputs), `provenance_scanner.py`, `data_inventory.py` and
  `worksheet_checker.py` each write `<!-- Doc-Kind: generated | ... -->`
  as the first line of the file they produce. Run on a throwaway copy
  at `d99d8db1` + the patch: all five outputs open with the tag, and
  `doc_index.py` reports "generated 5" with no untagged row where
  README.md's table had shown five. The maintenance run carries
  `doc_index.py` as a generator, so the table follows the next run.
- **Gap:** the GALLERY half. The gallery has a README and its own
  runner and no `doc_index.py`; its atlas copy would need the same tag
  emission. Not scheduled; opens when the gallery README is next
  edited.
- **Ref:** L-270 (the Gap that raised it);"""),

# ---- L-219 stale pointer ----------------------------------------------------
(b"""which would be 1.7 -- 1.5 and 1.6 are taken by L-220.
""",
b"""which would be the next version (1.12 as of 2026-09-16; this line said
1.7 when 1.5 and 1.6 were the latest, and the skill moved on without it
-- corrected, not silently, on 2026-09-16).
"""),

# ---- L-333 opened ------------------------------------------------------------
(b"""#### [L-332] interactive-exhibit skill 1.3""",
b"""#### [L-333] The master plan's two companion summaries have not moved since August (planning documents)
<!-- L:333 status:OPEN upd:2026-09-16 section:A flag: rice:2/3/90/2 -->
- **Found 2026-09-16 in the ledger review.** The plan itself is current
  (v32, 2026-09-16). Its two companions are not:
  `documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` is stamped
  August 29, 2026 (orrery `688561ef`, gallery `ac9a5c7b`) and says step
  three is done "for one body"; `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md`
  is stamped August 19 (orrery `9ffb9b40`). Since then: Earth shipped
  as the second room (L-291, 2026-09-10), its magnetosphere landed
  (L-305), the phone chrome settled (L-316, L-318), units became a
  field (L-322) and the orrery's hovers joined the braid (L-321).
  [verified @ `d99d8db1`]
- **Why it matters.** The ledger skill names the three documents as one
  plan at three zooms; a reader who opens the critical-path companion
  for "how far to the end" gets an answer eighteen days old that
  undercounts the bodies through step three. It is The Correction Does
  Not Travel on the plan's own companions -- the same file was the
  founding case for that rule (L-226).
- **What it is not.** The plan restamps once per DESIGN BUILD (L-296),
  and that cadence is not staleness. But the companions restamped with
  v19 and v20 and not with v21 through v32, so the rule that keeps the
  plan honest has no counterpart for them. Proposed (Claude): the
  companions restamp when the plan does, in the same patch, and the
  ledger skill's Document Stack paragraph says so -- a method question,
  which is the skill's to absorb. Both files keep overtaken claims in
  place with a bracketed note rather than deleting them, by their own
  headers; a restamp adds, it does not rewrite.
- **Note:** RICE 2/3/90/2 -> 2.7 is Claude's proposed score. Not on the
  critical path; a documentation session, or the next design build.
**Gap:** restamp both companions to the plan's v32 state, or rule that
one of them is retired (the critical-path companion answers a question
the plan's Section 5a now answers itself); then the skill line.
  **Tony-action (decide):** restamp both, or retire one.
**Ref:** `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` (v32),
`documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`,
`documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md`;
`skills/ledger-and-session-records/SKILL.md` (The Document Stack);
L-221 (the plan as sequencing authority), L-296 (restamp per design
build), L-226 (The Correction Does Not Travel, whose founding case was
the critical-path companion).

#### [L-332] interactive-exhibit skill 1.3"""),
]


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print(f'ERROR: {TARGET} not found next to this script. NOTHING was written.')
        return 1
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    content = raw.replace(b'\r\n', b'\n')
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    actual = hashlib.md5(content[:a] + content[b:]).hexdigest()
    if actual != EXPECTED:
        print(f'ERROR: {TARGET} is not the file this patch was built against')
        print(f'       expected {EXPECTED}, found {actual}{" [CRLF]" if was_crlf else ""}')
        print('       (the INDEX zone is excluded from this comparison)')
        print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
        return 1
    if was_crlf:
        print('[CRLF] the working copy is CRLF; matched after normalising')

    new = content
    for old, repl in EDITS:
        n = new.count(old)
        if n != 1:
            print(f'ANCHOR FAIL: expected 1 match, found {n}: {old[:70]!r}')
            print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        new = new.replace(old, repl)

    if any(c > 127 for c in new):
        print('ERROR: the result would hold non-ASCII bytes. NOTHING was written.')
        return 1

    out = new.replace(b'\n', b'\r\n') if was_crlf else new
    with open(path, 'wb') as f:
        f.write(out)
    print(f'ok  {TARGET}  ({len(out)} bytes{", CRLF preserved" if was_crlf else ""})')
    print('stamped: header (four Module updated lines, three of them retroactive)')
    print('closed: L-226, L-232, L-271, L-277, L-278, L-332;  opened: L-333')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md '
          'TWICE -- the first run prints [auto-fix] lines while it files the '
          'six closed items into section C; the second prints OK: 328 blocks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
