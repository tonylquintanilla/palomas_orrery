<!-- Doc-Kind: hand | Build record for L-421 parts 2 and 3 (the typed facts check, and each served number's citation copied from the orrery), with L-262 closed alongside and two small fixes from Tony's phone look. -->
# Build record: L-421 parts 2 and 3, the typed facts and the citations

Built on orrery 6b975155 ("L421 export citations") at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
2090a8b7 ("patch km radius label") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
The session started at orrery 0d7211ea and gallery 09d92918.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 16, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD. Brief:
  `documentation/HANDOFF_L421_checks_brief_20261016.md`.
- Closes L-421 (the typed facts) and L-262 (the framing test). Opens
  L-450, L-451 and L-452, and records L-453 as done.
- Tony's run record: `documentation/WHERE_WE_ARE_10-16-26_1708_run_record.md`.
  His verdicts are quoted from it on the ledger rather than repeated here.

## 1. The decision

Section 4 of the brief asked which side owns the citation beside a
served number. Tony, at the start: "Yes, A as ruled." The orrery owns
it. The website's own words about a citation keep a field of their
own, `source_note`.

## 2. What was built, in order

1. Orrery, `patch_L421_9_export_citations_20261016.py`, pushed at
   6b97515.
   - The constants export moves to schema 7. Each row carries its
     citation (`source`), the rows it was read from (`source_from`),
     and whether it was inherited (`source_inherited`).
   - Twelve rows cite only "as <another row>." The export follows the
     pointer to that row's citation, so a visitor never reads a store
     name.
   - A derived row with no citation takes its inputs' citations, in the
     order its `inputs` lists them.
   - Counts: 127 rows; 94 cite their own (12 of them through a
     pointer), 22 inherit, 11 have none.
   - `test_constants_export.py` gains check 7. It works out every
     citation again by its own code and holds seven named cases, plus a
     made-up chain of rows for the inheritance walk, because no real
     row exercises it. A broken walk and an ignored pointer were
     planted, and both were caught.
2. Gallery, `patch_L421_10_citations_typed_facts_20261016.py`, pushed
   at 5032cf2.
   - The mirror writes the orrery's citation beside each linked number:
     99 written, 69 of them reworded and 30 added. An export older than
     schema 7 is refused by name.
   - The website's own words moved to `source_note`, 35 of them. The
     store writer and the editor write that field; the mirror never
     does, and the store writer refuses a linked entry's `source`.
   - The Config mirror check compares citations word for word and fails
     on a difference. It names the links with no citation on either
     side (6) and the ones not served (7).
   - The i panel prints the citation, then the note. A hover carries
     neither.
   - New gating check, Typed facts (`documentation/smoke_typed_facts.js`).
     It builds the Sun and Earth rooms three times: as served, with
     every served word masked, and with every served number scaled.
     A sentence that survives the masking and is not on the allowed
     list fails, by room, feature and sentence. Each room's description
     in `interactive.html` is read the same way. Planted and caught: a
     typed sentence in a hover, a typed fact in a room description, and
     a served word field the check could not cover. A sentence added to
     the allowed list passes, and the check prints the list in full.
     Eight sentences are held open for Tony's ruling (L-451).
3. Gallery, from Tony's phone look the same evening (L-453):
   - The grey type became blue: `patch_drawer_row_colour_20261016.py`
     at cfa3d52, then `patch_grey_to_blue_2_20261016.py` at a83b752.
     `patch_grey_to_blue_20261016.py` stopped on its base check and
     wrote nothing.
   - Earth's four inner shells print "Radius: 5,710 km (0.0000382 AU)"
     instead of a bare "= ...": `patch_km_radius_label_20261016.py` at
     2090a8b. The Display figures check now fails on a bare "= " for a
     radius served in km, shown failing on all four first.
4. Orrery, `patch_L421_11_close_20261016.py` (this close):
   - the dashboard's Typed Facts button and its short line, so
     Dashboard parity matches the gallery's new row;
   - the ledger: L-421 and L-262 closed, L-423 item 1 done, L-367 takes
     L-262's residual, L-413 moves to its design talks, L-449 gains the
     second night's evidence, L-450 to L-453 new;
   - Where We Are, above the marker; the live run-record zone emptied
     only if it holds exactly what your saved copy holds;
   - interactive-exhibit 1.16 with protocol v3.101 and the regenerated
     manifest; the skill's 1.13 entry and protocol v3.98 moved to their
     history files; the versioned copy `project_instructions_v3_101.md`;
   - this record; and your run-record copy, added only if it is not
     already in documentation/.

## 3. What was verified, and how

- Every patch was run on a throwaway copy of the files it edits before
  delivery, and reproduced the intended result byte for byte.
- Tony's runs are the proof, quoted on L-421: the orrery's 31 of 31,
  the gallery's Daily Run 29 of 29 with Typed facts and the Config
  mirror check passing, the live run 2 of 2 with the export served
  byte for byte, and his two i panels, "all correct".
- The close patch was pre-tested by running `orrery_maintenance_run.py`
  on a throwaway copy of the patched orrery; its result is in the
  delivery message.

## 4. Found along the way

- L-449 (the run records) happened again: build 20261016T224259Z left
  one record where the repository held 84, with every rename on the
  first try. Put back from the repository's bytes at Tony's word. A
  check that stops the Daily Run on such a loss is proposed on L-449.
- L-450: some of the orrery's citation texts read as store notes
  ("Converted to km^3 s^-2 here."), and the website now prints them.
- L-452: some of the website's notes repeat the citation printed above
  them; one note carries "(Tony, 2026-09-28)".
- The brief pointed at `test_citation_inheritance.py` for the derived-
  row rule. That test pins a different rule; the derived-row rule is
  pinned in `test_constants_export.py` check 7.

## 5. Tony's actions, all of them

- (do) Run `patch_L421_11_close_20261016.py` from VS Code in the orrery
  folder.
- (do) Run `orrery_maintenance_run.py`. Expect Dashboard parity to
  match 84 steps, and the Ledger index to move L-421, L-262 and L-453
  into section C.
- (do) Commit and push.
- (do) Reinstall interactive-exhibit 1.16 in Settings > Skills, and
  copy PROJECT_INSTRUCTIONS.md into the Project instructions.
- The next session that does exhibit work confirms its loaded copy
  reads interactive-exhibit 1.16. horizons-orbital-mechanics 1.8 still
  travels.

Session written October 2026 with Anthropic's Claude Opus 5.5.
