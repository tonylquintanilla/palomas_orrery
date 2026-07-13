# Tier 1 close batch -- flips Phase 1b (L-098) to DONE
**Prepared by Opus 4.8, 2026-07-12 | one orrery commit | verified against orrery HEAD 58aec088, gallery HEAD a08bdd10**

State going in (all verified):
- Step 1: encke-mock fix live at gallery HEAD a08bdd10; suite green three ways
  (Opus clone, Tony Windows run, PASS 75/0). CLOSED.
- Step 2: guard logic tested on hardware; banner + live dispatch verified. CLOSED.
- Step 3: raw archive backed up off-repo -- gallery repo green-synced in OneDrive
  (+ git + Google Cloud + Windows). L-106 closes on existing coverage. CLOSED.
- Step 4: master plan v11 reconciliation already in; Status line updated. CLOSED.

This batch is step 5: the ledger flips + one final Status refresh. All orrery repo.

---

## 1. Master plan Status line -- final (replaces the interim one you set in step 4)

The interim line said "Close pending only the backup action (L-106)". Now that
L-098 closes, replace it with the COMPLETE version:

    **Status:** v11 -- Phase 1b (data-serving pipeline) COMPLETE + DEPLOYED (v0.4 fetch-fresh). Live dry-run gate passed 2026-07-11; offline suite green from a clean clone; served cache live at gallery data/solar-system/; raw archive backed up off-repo (OneDrive + git + Google Cloud). L-098 closed 2026-07-12. Next: unattended nightly scheduling (L-111 correctness/operability items) is a separate follow-on.

---

## 2. LEDGER -- paste L-117 (records the encke-mock fix; now DONE)

    #### [L-117] Offline suite red at HEAD: Encke id drift (2P -> 90000091) not mirrored in the mock
    <!-- L:117 status:DONE upd:2026-07-12 section:C flag: rice:3/3/95/0.25 -->
    - **What.** tools/test_gallery_cache_builder_offline.py mocks Horizons by
      horizons_id: ELEMS keys and fake_solution_tp both keyed '2P'. The live-gate
      Encke pin (config 2P -> 90000091) was never mirrored here, so the mock
      returned no data for '90000091', the build dropped encke, and objs['encke']
      KeyErrored. RED from a clean clone -- reached ~22 checks, then died.
    - **Why it hid.** F1's FileNotFoundError (fixed in the L-114 push) masked
      this: prior runs died at config-load before reaching the encke assertion
      (line 138), so no complete green run ever surfaced it. F1's stated
      acceptance ("suite green from a clean clone") was never actually met --
      the path fix made the suite RUN, revealing the next failure.
    - **Fix (verified green + pushed).** Two lines: ELEMS key '2P' -> '90000091';
      fake_solution_tp branch '2P' -> '90000091'. Green three ways (Opus clone,
      Tony Windows run, PASS 75 checks 0 failures) and LIVE at gallery HEAD
      a08bdd10. The true completion of L-114's F1 acceptance and the real green
      gate for L-098 step 1.
    - **Ref.** tools/test_gallery_cache_builder_offline.py (ELEMS ~line 26,
      fake_solution_tp ~line 63). Parent L-098; sibling of L-114/F1. Connects to
      the open "should Encke be in the tranche" question (unresolved; if it later
      resolves to REMOVE, drop encke from config + mock + assertions).

---

## 3. LEDGER -- L-106 resolution + flip DONE

Change the tag `<!-- L:106 status:OPEN upd:2026-07-09 section:H flag: rice:2/2/90/1 -->`
to `status:DONE upd:2026-07-12 section:C`, append this resolution, and move the
block into Section C:

    **Resolution (2026-07-12).** Off-repo backup requirement met by existing
    background coverage, not a new action: the repo tree lives under
    C:\Users\tonyq\OneDrive\Desktop\python_work, so OneDrive continuously syncs
    the whole working tree (raw/ included) off-machine (verified: gallery repo
    folder green "available on this device"); Google Cloud + Windows backup layer
    on top; raw/ is also committed to git (GitHub). The .gitignore entry
    (data/_backup/) was already present. The explicit copy-raw/-to-_backup/
    scheduled action is NOT built -- redundant with OneDrive folder-level backup +
    version history; building it would duplicate infrastructure.

---

## 4. LEDGER -- flip L-098 (Phase 1b) DONE

Change `<!-- L:098 status:OPEN upd:2026-07-09 section:W.Active flag: rice:3/3/50/3 -->`
to `status:DONE upd:2026-07-12 section:C`, and move the L-098 block into Section C.
(Optional: add a one-line close note -- "Closed 2026-07-12: builder built,
offline-verified (75/0 clean clone), live-gated 2026-07-11, deployed to gallery
data/solar-system/, backup covered (L-106). Children: L-102/L-113 (thinning,
deferred), L-107 (provenance register), L-111 (unattended-nightly, follow-on).")

---

## 5. LEDGER -- flip L-108 (master plan) DONE

Change `<!-- L:108 status:OPEN upd:2026-07-09 section:H flag: rice:2/1/90/1 -->`
to `status:DONE upd:2026-07-12 section:C`, and move the block into Section C.
(The optional section-3a schema polish it mentioned stays deferred -- note it in
the block if you want it tracked, or let it go.)

---

## 6. Regenerate + push

1. Run `ledger_index.py` -- regenerates the index tables from the tags (L-098,
   L-106, L-108, L-117 now show DONE / Section C). Never hand-edit the index zone.
2. Commit + push the orrery repo (this batch: the Status line + four ledger flips).
3. Optional but clean: round-trip once and I'll confirm L-098 reads DONE at HEAD
   and the index regenerated.

That's Phase 1b closed. What remains is all deferred or follow-on, none of it
gating: L-111 (unattended-nightly correctness/operability -- the Tier 2 decision),
the builder line-755 comment cleanup, L-107 (provenance register), and the
non-1b tracks (encounter export, earth-system, animation refactor, axis control).
