# HANDOFF v28 -- Ledger Consolidation + Chain Reconciliation

**Date:** June 7, 2026
**Session model:** Claude Opus 4.8
**Supersedes:** v27 as the running-ledger head. v27 (dipole cone), v26
(rotation axis), v25 (N15 ring planes), v24 (bow shocks / Movement 1), and v23
(shell-consolidation D-track) all remain authoritative AS SESSION RECORDS by
reference; their embedded deferred-item ledgers are now SUPERSEDED by the single
running file (below). Nothing renumbered.
**Type:** DOCUMENTATION -- ledger consolidation + reconciliation. ZERO orrery
code changed this session. Review of the v23 -> v27 chain (+ the June-1 erratum),
with the load-bearing items verified against the live code at HEAD rather than
trusted from handoff prose.
**Built on:** GitHub repo HEAD `76c330ea4dbe6bc667fba2ffb5baa1a65ae56d22`
(branch main). Round trip confirmed at session start (remote HEAD == this base;
Tony's /documentation update was the intervening push).
**New artifact:** `LEDGER_orrery_consolidated.md` -- THE running ledger from here
forward. Future handoffs UPDATE IT IN PLACE and reference it; they do not
re-embed a ledger copy.
**Integrator:** Tony Quintanilla

> **The cure for rebase-leak.** v24-v27 carried the v23 canonical ledger only
> "by reference," and real items quietly fell out of view across the rebases.
> This session re-absorbed the full backlog into one authoritative running file,
> restored the leaked items, corrected a stale "open" against HEAD, unified three
> records of the animation issue into one, and recorded two Tony decisions. The
> protocol already named the fix ("one authoritative running ledger beats
> per-handoff renumbering"); this is that fix, executed.

---

## 1. WHAT THIS SESSION DID

- **Enumerated the full /documentation set first** (377 files at HEAD) before
  reviewing -- the enumerate-before-claiming-a-review gate. Then read the chain
  since v23: v23 (canonical ledger body), v24, v25, v26, v27, and the June-1 v21
  erratum.
- **Verified load-bearing items against the live code at HEAD** (not handoff
  prose). Findings in Section 2.
- **Created `LEDGER_orrery_consolidated.md`** as the single running ledger:
  v23's numbered backlog carried forward (nothing renumbered), reconciled against
  v24-v27 Movement work and against HEAD, with a per-item verification tag
  (`[verified @76c330e]` / `[per chain]` / `[render-gated]`) so the ledger is
  honest about which of its own claims are checked vs carried.
- **Recorded two Tony decisions** (Section 3).

---

## 2. RECONCILIATION FINDINGS (verified vs carried)

Verified against HEAD `76c330e`:
- **Uranus 105-deg belt/ring fudge: DONE.** The June-1 erratum recorded it "NOT
  STARTED / still live at L643/L1023"; at HEAD it is retired -- belts (L732) and
  rings (L1097) route through orient_to_planet_pole. The erratum text is
  superseded; not carried forward as open.
- **Mercury +0.2 R_M northward dipole offset: OPEN (absent in code).** Only the
  cosmetic tail-marker offset and the standard sunward-recenter exist in
  mercury_visualization_shells.py. This was a v24 Movement-2 item that fell out of
  the v26/v27 ledgers. LEAK RECOVERED.
- **Duplicate `'Sun'` key in CUSTOM_SHELLS: OPEN.** Two top-level `'Sun'` keys
  inside CUSTOM_SHELLS (starts L2052): L2642 and L2823; last wins, first dropped.
  (The L1868 `'Sun'` is in SHELL_CONFIGS -- different dict, legitimate.) Confirms
  the v26/v27 carried bug.
- **Inner-four bow-shock hover: OPEN (radii only).** Mercury hover reads "1.4 to
  2.0 radii" (L304/L364) -- no km/AU, unlike the giants. Hover-Text-AU-Convention
  gap. LEAK RECOVERED from v24 sec5.

Other leaks restored (carried-by-reference, absent from v26/v27 ledgers):
- v24 Movement-2 bow-shock honesty (now closed-by-redesign; see Section 3 Q2).
- v24 sec5 precision batch (Jupiter bimodal-MP toggle, Earth MP/BS citation
  upgrade, per-body eccentricity) -- `[per chain]`.

Unified:
- The animation issue appeared in THREE places -- v23 item 21/51, v25's animation
  deferral, and v27's "rotation axis + dipole cone do not render in animate
  frames." It is ONE architectural item, now tracked once under 21/51 in the
  ledger (the body-triggered render gap is an objective inside it).

Closed:
- N13 (v23 Bucket B dipole sweep-cone) closed AS the v27 dipole cone.
- N12 (planet N/S pole markers) closed -- Tony-confirmed done (June 7).
- Rotation-axis Mode-5 render sweep of the remaining 8 bodies -- dropped as a
  non-issue (most confirmed; Tony, June 7).

---

## 3. TONY DECISIONS RECORDED

- **Q1 (packaging):** standalone running ledger file + this v28 handoff (not an
  in-place v27 edit), because the reconciled backlog is substantially different
  from v27's embedded section. Done.
- **Q2 (bow-shock flank poke):** CLOSED BY REDESIGN. The geometric "tilt
  enclosure" is retired; the chosen path is the HOVER DISCLOSURE -- state what
  geometry is sourced from physics vs approximate/schematic. Envelope hovers
  (Uranus/Neptune) carry it as of v27. OPEN REMAINDER: extend the same
  sourced-vs-schematic disclosure to the BOW-SHOCK hovers (they cite the standoff
  but not the conic-section approximation, per v27 sec4).

---

## 4. PENDING ACTIONS

- **Commit protocol v3.28 to the repo root.** Confirmed by Tony: v3.28 is in the
  working copy / project instructions but NOT pushed (no new root files pushed
  yet). Until pushed, the doc and its stamp have not travelled together.
- **Commit `LEDGER_orrery_consolidated.md` + this v28 handoff** to /documentation,
  then confirm the round trip (remote HEAD moves; this becomes the next base).

---

## 5. ACTIVE SEPARATE TRACK -- FOOD INSECURITY (reopened)

Earth System track, not the orrery refactor. Design locked
(HANDOFF_food_insecurity_design_v1 + MANIFEST_food_insecurity_sudan_first_cut):
Sudan first cut, IPC vector polygons (approach B), folders-per-period,
transcribe-not-synthesize. Status: awaiting IPC Public API key (request
submitted; CC BY-NC-SA 3.0 IGO terms reviewed, compatible with non-commercial
educational use). Live pipeline confirmed at HEAD: the Earth System engine uses
simplekml (real KML polygons already via newpolygon/outerboundaryis), aabbggrr
color order, package_and_cleanup KMZ assembly, data/ output, and a file-launcher
controller -- the food layer reuses the primitives, not the scalar-field
run_scenario spine. RELEASE-DRIFT CORRECTION to fold in at build: current Sudan
release is Feb-May 2026 + projections to Jan 2027 and names NO current Famine --
the manifest's El Fasher/Kadugli Phase-5 spot-check (Sept 2025) must be rewritten.

---

## 6. CARRIED FORWARD (session records, by reference; ledgers superseded)

- **v27** dipole cone (Movement 2 sub-item 2).
- **v26** rotation-axis primitive (Movement 2 sub-item 1).
- **v25** N15 ring-plane migration + analytical-orbit retirement.
- **v24** bow shocks + magnetosphere nest (Movement 1).
- **v23** shell-consolidation D-track (its ledger body is now the running ledger).

All open items from these now live in `LEDGER_orrery_consolidated.md`.

---

## 7. NEXT-SESSION PRIORITIES

1. **Push** v3.28, the ledger, and this handoff; confirm the round trip; the new
   HEAD becomes the next base.
2. **Animation parallel-pipeline gap** (ledger 21/51) -- the most concrete
   deferred orrery item; map the animate dispatch, one fix for both
   body-triggered elements (rotation axis + dipole cone). Smoke-test the animate
   pipeline to a KNOWN state when deferring.
3. **Bow-shock hover disclosure remainder** (Q2) -- extend sourced-vs-schematic to
   the Uranus/Neptune bow-shock hovers.
4. **Earth dipole cone** (source the ~11 deg tilt first) -- the compass anchor.
5. **AU-convention sweep** (ledger section E) -- KEEP OPEN, revisit (Tony does not
   immediately recall the origin); verified specifics noted in the ledger for that
   revisit (inner-four bow-shock hover reads radii-only at HEAD; GEO altitude lacks
   AU).
6. **Food Insecurity build** -- when the IPC key arrives; map endpoints from the
   bundled docs, keep the key in a local env var.

---

Module updated: June 2026 with Anthropic's Claude Opus 4.8
