<!-- Doc-Kind: hand | Session record for L-395's design talk and first build: the orrery's object list feeds the website. -->
# HANDOFF -- L-395: the orrery's object list feeds the website

Built on orrery 6b2ef097da67e67ab8f748b5481c222e5dd34acc at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
5a38de15d69df48749ba230cdfacf0e9d9e2fb5e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Orrery pushed at feb5e369 (patch_L395_1; the small Mars and Jupiter
patch filed unrun, its fixes folded in). Gallery pushed at 43993b49
(patch_L395_2, the mirror's first write, and the cache rebuilt by
daily_run.py). This record lands with the closing patch
patch_L395_ledger_close_20261001.py.

Type: BUILD (with its design talk).
Supersedes: nothing. Follows HANDOFF_L398_distance_figures_20261001.md,
whose section 6 items 1 and 2 this session carried out.

Session written October 2026 with Anthropic's Claude Opus 5.5.

## 1. Skills at session start

All loaded copies matched the manifest, including the two the last
session bumped: provenance-discipline 2.23 and interactive-exhibit 1.7
(obligation discharged). Also loaded: ledger-and-session-records 1.13,
safe-file-editing 1.11, gallery-cache-builder 1.6,
horizons-orbital-mechanics 1.1. This session bumps
provenance-discipline to 2.24 and interactive-exhibit to 1.8 (protocol
v3.76). THE NEXT SESSION CONFIRMS its loaded copies read 2.24 and 1.8
before any provenance or exhibit work.

## 2. Rulings

- The website keeps copies of each served object's identity facts,
  written by a tool from the orrery's list and checked (option B).
- A new `'key'` field on each served entry, spelled as the website's
  slug. Confirmed as recommended.
- Tony: "simple errors such as the Apophis naming discrepancy should be
  fixed and reported." Now provenance-discipline 2.24.
- Tony: "I lean to a clean export and fix the orrery where needed." One
  description and one link per object, in the orrery.
- Tony: "Please fix" -- the Mars and Jupiter links.
- Tony asked whether the new tools belong on the dashboard. That is
  method already settled (every maintenance-run tool has a button,
  L-322, L-324), so the closing patch adds them.
- From Where We Are: a bare interactive.html link opens the Solar
  System room; the Explorer moves to its own address. Recorded on L-363.

## 3. What was built, verified

| Patch | Repo | Pushed | Verified |
|---|---|---|---|
| patch_L395_1_objects_export_20261001.py | orrery | feb5e369 | Sandbox: three starting states (with and without the small link patch, LF and CRLF), refuses a rerun and the wrong folder; export of 11, check passes, both its refusals shown; scanner Tier 1 unchanged at 296. Tony's run. |
| patch_L395_2_objects_mirror_20261001.py | gallery | 43993b49 | Sandbox: LF and CRLF; the room's driver run in CPython on the real cache, every body and the Sun carrying its words and link, no warnings. Tony's runs: 22 of 22 gating after daily_run.py; phone "perfect". |
| patch_L395_ledger_close_20261001.py | orrery | -- | This patch. |

## 4. Found this session

- The Apophis "discrepancy" was two right names for one Horizons
  record; the list's convention (designations for numbered asteroids)
  decides it under B.
- The cache builder's offline suite fed Apophis stand-in data under
  99942 only; caught in the sandbox before delivery and fixed in
  patch_L395_2.
- 135 of the list's 182 descriptions carry numbers: L-403, one class
  row.
- The orbital mechanics README's Haumea example gives the barycentre
  id; the code uses Haumea itself. Noted in the README.
- My first answer said the "Horizons:" opening could not be rebuilt
  from the id field because it carries a different version of the id.
  Exactly: it carries the permanent number, which no field holds.

## 5. Discrepancies

- None between handoff and base.

## 6. Next session

1. Confirm the loaded skills read provenance-discipline 2.24 and
   interactive-exhibit 1.8.
2. L-363 step 3b: the drawer's behaviours, then Tony's phone check.

## 7. Tony-actions, rolled up

- (do) Run patch_L395_ledger_close_20261001.py in the orrery root; then
  orrery_maintenance_run.py; move the patch to documentation/; commit
  and push.
- (do) Reinstall provenance-discipline and interactive-exhibit from
  skills/ (Settings > Skills).
