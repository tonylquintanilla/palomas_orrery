Built on:
- orrery: 745106dc47c61ff2936fb8460fb58ad5b8910dc1 at https://github.com/tonylquintanilla/palomas_orrery
- gallery: 22c947c993a0d3e5f1aa9390288c28bcd2710275 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
- pushed at: 877822db58be485e44b0a2a28c0b3697b043d1ee

Ledger handle: L-163
Phase: 1 of 4 -- Archival and repo hygiene (content, no code)
Session: Opus 5 builder session, July 24-25, 2026
Design: ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md (Sonnet 5), reviewed by
Fable 5 (Section 16), Phase 0 reconciliation recorded in Section 19.

---

# L-163 Phase 1 -- As-Built

## Changed

**Tony (pushed at 745106dc, this session):**
- 7 diagnostic/one-shot modules removed from the orrery repo to local
  archive: `provenance_scanner_color_patch.py`, `smoke_phase4.py`,
  `smoke_dipole_cone.py`, `smoke_rotation_axis.py`, `titan_io_probe.py`,
  `color_map.py`, `barycenter_cache_check.py`.
- `MASTER_PLAN_UPDATE_provenance_and_prep.md` Section 6 entry pasted
  (the Phase 0 gap -- now closed).
- `skills/ledger-and-session-records/SKILL.md` bumped 1.2 -> 1.3, adding
  the Tony-action (do)/(decide) tag convention and the stale-installed-
  skill field note.
- `documentation/ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md` extended with
  Section 19 (Phase 0 reconciliation).

**Claude (delivered this session, pending Tony's commit):**
- `module_atlas.py`: 7 ghost `ROLE_MAP` entries deleted (5 gallery-repo
  module names, `orrery_integration`, `star_visualization_gui_before_
  pyinstaller_refactor`), plus the now-orphaned `# Legacy` section
  comment. Mode 1 targeted snippets, applied bottom-up. No other change
  to the file.

## Verified

Every claim below was checked against live HEAD this session, not
carried from the handoff.

- **SHA round trip.** Orrery HEAD `745106dc` matches Tony's reported
  push. Gallery HEAD moved to `22c947c` unreported; characterized as a
  `Revert "automatic"` commit whose tree is byte-identical to the
  previously-verified `81c2ee1`, so gallery content is unchanged and
  Section 8's `SCAN_PATHS` inventory still holds.
- **All 7 archive candidates gone** from the repo tree. Root module
  count 121 -> 114.
- **Section 19's scope claim confirmed independently:** none of the 7
  archived files had a `ROLE_MAP` entry (all were in the original 19
  fall-through set). No `ROLE_MAP` edit was required for their removal.
- **Ghost deletion verified on a throwaway copy** before delivery:
  `ROLE_MAP` 94 -> 87 entries; `py_compile` clean; module imports and
  `classify_role()` exercised against mapped names, the `_shells`
  heuristic, and an unmapped name -- all correct. ASCII-only and LF
  endings preserved (file was already ASCII/LF at HEAD).
- **Zero ghosts remain:** after the patch, every one of the 87 `ROLE_MAP`
  keys resolves to a file present at HEAD.
- **Vocabulary integrity:** `legacy` remains in `ROLE_ORDER` and
  `ROLE_DESCRIPTIONS` despite having no members; every `ROLE_ORDER`
  value still has a description.
- **Phase 2 scope recomputed from HEAD, not assumed:** 12 modules still
  fall through to `'other'` (down from 19, exactly as Section 19
  predicted) -- `data_inventory`, `earth_system_common`,
  `export_orbit_cache`, `food_insecurity_generator`, `ledger_index`,
  `measure_animation_html`, `measure_perframe_elements`,
  `orrery_rendering`, `scenarios_food_insecurity`, `shell_configs`,
  `skills_index`, `test_reset_completeness`. Accounting closes:
  87 mapped + 12 fall-through + 15 matched by the `_shells` heuristic
  = 114.

## Coverage-gap count change (explained, not silent)

Section 1 recorded 5 of the 19 fall-through modules as carrying
claim-shaped content invisible to citation scanning (PROVENANCE_AUDIT.md,
July 17, 2026). One of those 5 -- `smoke_rotation_axis.py`, 1 string --
leaves the coverage gap by file removal, not by being brought into scan
scope. The remaining 4 stay in Phase 2's scope: `shell_configs.py` (91
strings), `export_orbit_cache.py` (8), `food_insecurity_generator.py`
and `orrery_rendering.py` (1 each). Fable's review (Section 16) flagged
this class of count shift in advance; recorded here so the next
PROVENANCE_AUDIT.md delta reads as accounted for.

## Closed out

All Phase 1 actions completed and verified at HEAD `877822db`:

- `module_atlas.py` ghost-entry deletion committed at `728361c3`.
  Re-verified independently at HEAD: 87 entries, zero ghosts,
  `py_compile` clean, `classify_role()` correct across mapped names, the
  `_shells` heuristic, and unmapped names. Byte-identical to the version
  verified before delivery apart from one trailing space on line 77
  (cosmetic, left as-is).
- `skills/ledger-and-session-records/SKILL.md` placeholder replaced with
  `728361c3c451e19ce0cc025b2ed29f6ee30054e9`. Verified as a real,
  reachable ancestor of HEAD carrying the 1.3 content -- a true
  provenance claim, not a filled-in-to-clear stamp. Stamping the
  immediately-preceding commit is the correct resolution of the
  chicken-and-egg problem the placeholder named.
- `documentation/ledger-and-session-records_SKILL_v1.3.md` deleted
  (confirmed 404 at HEAD). One authoritative store restored.
- L-163 entry added to `MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 6.
  Note for later readers: the handoff's Section 14 named
  `MASTER_PLAN_UPDATE_provenance_and_prep.md` as the destination, but
  that document holds *proposed edits* to the master plan, not the plan
  itself. The entry landed in the applied plan, which is correct.

**Standing observation:** the `ledger-and-session-records` copy installed
to the account still read 1.1 in this session after two separate
reinstalls by Tony. Both times the repo copy was correct. This is
consistent with the account skill mount not refreshing mid-session
rather than a failed reinstall -- no further action; confirm at the next
session's start. All Phase 1 work used the repo text at HEAD.

**Carried forward:** Phase 4's version bump target for
`ledger-and-session-records` is **1.3 -> 1.4**. The 1.3 bump landed in
Phase 1 and its content (the Tony-action tag convention) is unrelated to
Phase 4's planned Codebase Tooling rewrite, so Phase 4's scope is
unchanged -- only its starting version moved.

**Handed to Phase 2:** `add_docstrings.py` cannot execute the sweep in
its current form. It replaces a module's entire docstring with
hand-authored text from a `DOCSTRINGS` dict; the sweep needs to insert
one or two lines into ~136 mostly-existing docstrings without disturbing
the rest. Section 13's read ("the right existing tool to extend") holds,
but the extension is a new insertion mode, not new dict entries. Its
binary-mode I/O, per-file line-ending detection, and preview/`--write`
split are all worth keeping. Two defects to address while there:
`has_leading_comment()` is defined but never called, so a shebang-first
module such as `ledger_index.py` would have a docstring inserted above
its shebang; and `insert_docstring()` locates the docstring by first
literal triple-quote rather than by parsing, which the Section 3 parser
(`ast.get_docstring`) does correctly.

## Gate

Phase 1 closes when the `module_atlas.py` edit is pushed. Phase 2
(content sweep) is gated on that, and opens with the one design
question the handoff deliberately left unresolved: exact `Role:` /
`Domain:` tag placement relative to the existing credit-line
convention, to be locked with Tony before `add_docstrings.py` runs at
scale.

## Ref

`module_atlas.py`, `ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md` (Sections 1,
4, 16, 17, 19), `PROVENANCE_AUDIT.md` (July 17, 2026),
`LEDGER_CONSOLIDATED.md` (L-163), `MASTER_PLAN_UPDATE_provenance_and_
prep.md` (Section 6), `skills/ledger-and-session-records/SKILL.md`
(v1.3), L-078 (role-driven coverage-widening track), L-152 (prior
skill-version drift precedent).

---

Session written July 2026 with Anthropic's Claude Opus 5.
