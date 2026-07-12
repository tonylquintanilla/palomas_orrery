# Gallery Cache Builder -- Live Gate Session Handoff
**Date:** 2026-07-11 (Sonnet 5, mobile/chat session, Tony integrating)
**Scope:** TESTING_PROTOCOL.md Layer 2 (live dry-run gate) executed in full on
real hardware, real Horizons, for the first time. This handoff is a claim;
Opus should re-verify against the actual repo state before acting, same as
always.

## SHAs (last known pushed -- re-pull fresh at session start)

- **Gallery** (`tonyquintanilla.github.io`): `44e553ecd82f05984d1418d0448245f51af8b0b0`
- **Orrery** (`palomas_orrery`): `3708de8cc9ef48bbf90e6fa037c8e588ecbaf405`

**Neither repo has tonight's changes pushed yet.** See "Not yet committed"
below -- this is the most important thing to get right before building on
top of anything described here.

---

## What actually happened tonight (brief)

All 11 tranche objects were dry-run tested individually, live. Encke failed
with `solution-TP not_present`, traced through three hypotheses (wrong
`.gitignore`-adjacent guesses ruled out; `closest_apparition` ruled out by a
controlled A/B test) to the real cause: the automated query used the bare
designation `"2P"` with `id_type='smallbody'`, which resolves ambiguously
(61 historical apparition records) or throws a syntax error when
`closest_apparition` is added (astroquery only prepends the required `DES=`
key for `id_type='designation'`/`'name'`/etc., never for `'smallbody'`).
Fixed by pinning Encke to its current specific record number (`90000091`),
matching the orrery's own already-proven Halley pattern (`id='90000030'`) --
no apparition flag needed once you're not searching by a short designation
anymore. Confirmed live, three ways (direct astroquery A/B test, real
`--dry-run --object encke`, and the resulting manifest).

Voyager 1's arc was verified structurally, not just by point count: both
flyby windows (Jupiter 1979, Saturn 1980) came back completely daily with
zero gaps; the 49-year glide thinned from 2549 raw points to 29, with a
12-year gap (1992-2004) where the trajectory is genuinely straight.

A real `--first-build` ran clean (all 11 objects `backfilled`, structural
validation pass). While inspecting the resulting directory, a real bug
surfaced: **`objects_config.json` does not survive the atomic swap** (see
L-114 below) -- discovered because the config that had just been hand-edited
with the Encke fix vanished from `data/solar-system/` after the build. Worked
around locally (pointed `--config` at a manual backup) long enough to also
run the crash-recovery drill and a real `--nightly`, both of which passed
cleanly once the workaround was in place.

The ledger itself got audited while doing all this: 8 items (L-067, L-103,
L-104, L-105, L-106, L-107, L-108, L-111) had `section:` tags that didn't
match where they physically sat in the document (mostly stranded inside
Section C's closed archive). All 8 relocated and verified byte-for-byte
(no content lost, only reorganized). 13 unscored OPEN/DEFERRED items got a
placeholder `rice:2/2/50/2` so they're easy to find and distinguish from
genuinely-unscored-on-purpose items.

---

## CRITICAL -- needs Opus, real code + real commits

### 1. [NEW] L-114 -- the config-swap bug (draft below, ready to paste)

This is the most important item in this handoff. Full ledger entry:

```
#### [L-114] objects_config.json does not survive the atomic swap; also blocks crash-recovery
<!-- L:114 status:OPEN upd:2026-07-11 section:D.Priority flag: rice: -->
- **What.** objects_config.json lives inside data/solar-system/, the exact
  directory the whole-generation atomic swap replaces wholesale. Nothing in
  the builder copies the config into staging before the swap -- it's read
  once at the top of main(), never rewritten like coverage_index.json or
  feature_configs.json are. So every successful real build silently strands
  the config in data/solar-system.prev/, invisible until the next command
  fails with FileNotFoundError. Confirmed live tonight: this exact sequence
  happened on the real --first-build.
- **Worse, compounding:** main() calls load_config() before run_build() (and
  therefore before recover_incomplete_swap()). So if the config becomes
  unreadable -- which is exactly the state a real crash mid-swap produces --
  the self-healing recovery mechanism never gets a chance to run at all.
  Confirmed live: simulated the crash state and hit FileNotFoundError before
  any [RECOVER] line printed. A genuine crash at the wrong moment would leave
  the pipeline stuck with no built-in path back, no backup copies lying
  around unless someone happens to have one (as we did tonight).
- **Fix.** Move objects_config.json outside data/solar-system/ entirely
  (e.g. data/objects_config.json, a sibling). Update the --config argparse
  default and load_config's call site. This removes the config from the
  swap's blast radius AND removes load_config's dependency on the directory
  that might need recovering -- both failure modes close at once, no
  special-casing needed.
- **Workaround used tonight (not a fix):** `--config data\objects_config.json`
  pointing at a manual backup copy, to complete the crash-recovery drill and
  nightly test despite the bug. A corrected copy of the config (with the
  Encke fix already applied) currently exists in THREE places on Tony's
  machine: the live data/solar-system/ (current, correct), the stranded
  data/solar-system.prev/ (also correct, kept deliberately as a backup), and
  data/objects_config.json (also correct, kept deliberately as a second
  backup). None of this is git-committed yet -- see "Not yet committed."
**Ref:** gallery_cache_builder.py (argparse --config default; load_config;
run_build's staging/swap sequence; recover_incomplete_swap). tools/
gallery_cache_builder.py module docstring (already carries a matching
"Operational gotchas" note -- remove that note once this fix lands).
```

Suggested placement: `### D.Priority -- real bugs` section (matches the
existing heading for confirmed, live bugs). No RICE assigned -- your call,
though the crash-recovery implication argues for high priority.

### 2. `orrery-coding-conventions` skill amendment

Add to the Module Docstring Standard section. Diff in prose:

> Add an optional block to the template, for modules where getting something
> wrong has a real cost:
>
> ```
> Operational gotchas (if any -- omit this block for modules without real
> operational risk):
>     - Known trap: [what looks fine but isn't; what happens if you get it
>       wrong; what to do instead]
>     - Normal-but-scary state: [something that looks like a problem, but
>       self-resolves or is expected -- so it doesn't get "fixed" by hand]
> ```
>
> Ground: L-114 (this session) is exactly the case this exists for -- a real,
> currently-live trap that a "purpose + key functions" docstring would never
> surface, discovered only through live debugging.

Tier: PRACTICE (matches where Module Docstring Standard already sits). Bump
skill version.

### 3. `gallery_cache_builder.py` docstring update

Already written and `py_compile`-verified in a separate sandbox tonight (not
this repo checkout -- Opus should re-verify against live HEAD before
applying). Full replacement text for the module docstring:

```python
#!/usr/bin/env python3
"""
gallery_cache_builder.py -- standalone nightly builder for the Paloma's Orrery
web gallery cache (Phase 1b, ledger L-098). GALLERY repo tool.

Nightly: read objects_config.json -> fetch fresh from JPL Horizons per object
with the explicit canonical center -> validate on write (structural invariants
and #B3 conversion-consistency and the shrink gate ABORT; Guard v2 WARNs as a
monitor -- warn + keep, never reject) -> build raw cache + derived served files
in STAGING -> whole-generation atomic swap -> single verified commit. No orrery
imports; hard-won fetch specifics are COPIED WITH PROVENANCE from the orrery and
kept in sync on change (see per-function comments). See GALLERY_BUILDER_MANIFEST
v2 + GALLERY_DATA_SOURCE_HANDOFF v0.4.

Operational gotchas (found live, 2026-07-11 -- read before hand-editing
anything in data/solar-system/):
    - objects_config.json does NOT survive a real (non-dry-run) build.
      The atomic swap replaces the whole data/solar-system/ directory;
      the config is only ever READ from there, never copied into staging,
      so every successful real build silently strands the config in
      data/solar-system.prev/. KNOWN BUG, not yet fixed in code -- L-114.
      If objects_config.json is ever missing after a build, it's in
      .prev, not lost. Once L-114 lands, this note should be removed.
    - data/solar-system.prev/ is a NORMAL, SELF-HEALING artifact, not a
      problem to fix by hand. It's the one-generation rollback the swap
      keeps; recover_incomplete_swap() deletes it automatically the next
      time a build runs successfully. Do not delete it manually unless
      you've first confirmed (per the gotcha above) that nothing you need
      is stranded inside it.
    - data/.staging_solar-system_<timestamp>/ folders are throwaway
      dry-run/build workspaces, one per run. Safe to delete by hand;
      accumulate harmlessly otherwise (auto-sweep is a deferred item).

Provenance base: orrery HEAD 4e2629c (copy sources), gallery HEAD 4b086a6
(deploy target). Re-pin both on change.

Model updated: July 2026 with Anthropic's Claude Opus 4.8.
"""
```

### 4. L-113 and the L-102 correction

**Already done, not still pending.** Both are already in the corrected
`LEDGER_CONSOLIDATED.md` produced tonight (which also includes the 8-item
section-mismatch fix and the 13-item RICE placeholder pass). Opus's job here
is just to make sure the corrected file actually gets committed -- see "Not
yet committed."

### 5. Fable + GPT's Part B amendments (July 10 review, untriaged)

7 amendments from Fable, 10 from GPT (several tagged CRITICAL by GPT --
real-layout pre-test invocation, unattended-infrastructure kill-point testing,
exact remote-reference verification). These never got the verify-against-code
treatment Part A got. Needs its own pass before adoption, same rigor as
everything else tonight -- don't take severity tags on faith, check against
current HEAD.

### 6. Small decision, not code

Should `inspect_staging.py` and `debug_encke_tp.py` (both written and used
live tonight, both working) get committed into `tools/` for real, or stay as
Tony's personal local scratch scripts? Either is fine -- just needs deciding
once. (Tony: flag your preference here if you want it settled before the
Opus session rather than during it.)

---

## Not yet committed -- read this before building on anything above

**Gallery repo:** tonight's real first-build + nightly run (with the fixed
Encke config) exists only locally on Tony's machine. Nothing has been pushed
-- this matches the decided manual-push model (Tony reviews, then pushes on
his own timeline). The corrected `objects_config.json` needs to be part of
whatever Opus commits.

**Orrery repo:** the corrected `LEDGER_CONSOLIDATED.md` (8 relocations + 13
RICE placeholders + L-113/L-102 already included) and the corrected
`TESTING_PROTOCOL.md` (68->75 fix, Purpose paragraph reworded, full session
annotations added) both exist as files delivered in tonight's chat session,
not yet saved over the real files or committed. These need to land before
Opus reads either document as current.

---

## Housekeeping (low priority, not blocking)

`data/` on Tony's machine has accumulated a dozen-plus
`.staging_solar-system_<timestamp>/` folders from tonight's individual
dry-run testing, plus `data/solar-system.prev/` and a leftover
`data/solar-system.prev_old/` (the original pre-testing archive, renamed
aside earlier in the session). All safe to clean up whenever convenient --
connects to the existing (not yet built) staging-sweep deferred item. Not
urgent, not blocking anything.
