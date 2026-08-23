# HANDOFF -- 2026-08-23 -- the braid lands, and segment 3 begins

**Orrery: built on `38923c1cc64d492006135ec77779e1fb592582d5`, pushed at
`15741822cb8f54ac26fc252aa8382cd90534570d`**
(https://github.com/tonylquintanilla/palomas_orrery, branch main).
**Gallery: `493a0bd7fcba4067c56db318357889e965fba514` to
`8ec4f261013f09697d649efd25c8a746bffeff64`**
(https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Every SHA here was confirmed against the live remote, not carried
forward from a session note.

**Type: DOCUMENTATION, then one small BUILD.** Six patch scripts.
Documentation through five of them; the sixth is the first code change
under the braid.

**Companion to** `documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`,
which carries the ARGUMENT for the braid. This carries what was done
with it.

---

## What landed

| Patch | Target | Result |
|---|---|---|
| `patch_L221_2_master_plan_v19.py` | `MASTER_PLAN_INTERACTIVE_GALLERY.md` | 34 edits, v18 -> v19 |
| `patch_L221_3_ascii_and_dates.py` | the plan + `..._SUMMARY.md` | 20 edits + an ASCII sweep |
| `patch_L221_4_ledger_l154_l225.py` | `LEDGER_CONSOLIDATED.md` | L-154 unblocked, L-225 opened |
| `patch_L221_5_critical_path_summary.py` | `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` | 11 edits |
| `patch_L221_6_safe_file_editing_1_8.py` | the skill + the ledger | 1.7 -> 1.8, L-226 opened |
| `patch_L154_1_resolver_feature_params.py` | **gallery** `resolver.py`, `cache_reader.py` | segment 3, first half |

The braid -- Tony's ruling of 2026-08-22, that provenance stops being a
GATE and becomes a per-artifact slice -- now exists in every document
that had asserted the opposite, and the first work under it is built.

The master plan is at **v19**. Its five segments did not move; the order
they are worked in did, and Section 5a carries both separately now.

---

## Segment 3, first half -- BUILT

`resolver.py` had `features = tuple(rec.get("features") or ())`, which
reduced a nested mapping to a tuple of its category names one step
before anything could use the numbers inside. Jupiter's ring system
arrived at the browser as the string `'ring_system'`.

It now keeps the mapping and passes each feature's parameters into
`FeatureRequest.params`.

**The field already existed and had never been populated.**
`models.py` declares `params: Dict[str, Any]`, and `assemble.py` line 93
already emitted `"params": fr.params` into the report. The pipe from the
served cache to the browser was built, wired, and shipping empty dicts.

**Measured through the real dispatch, not a fixture.** Earth:
`atmosphere_shell` 2 keys, `van_allen_belts` 7. Jupiter: `ring_system`
4 rings, `radiation_belts` 4 keys. Saturn: `ring_system` 7 rings.
**Thirty-two numeric values now reach the browser for the Artifact 2
scene** -- the thirty measured ones plus `n_rings` and `n_points`, which
are declared drawing parameters.

**Artifact 1's lock held.** `python -m assembler.tests.test_artifact1_earth`
was run before and after: five checks OK both times, `scene_spec_hash`
`abbd01094852b57f` unchanged. That was the real risk and it was checked
BEFORE the patch was written -- the golden fingerprint hashes
`feature_keys`, never `params`.

**Two departures from the plan.** `models.py` was NOT touched: nothing
anywhere reads `ResolvedObject.features`, so the type change an earlier
plan called for would have been churn. And the non-dict cases RAISE
rather than coerce -- a resolver that quietly accepts a malformed record
and renders a feature with no numbers behind it is a check that cannot
fail. All twelve served objects carry dicts today, so the guard
announces a blind spot rather than handling a known case.

**Nothing renders from this yet.** The client-side renderers are the
second half.

---

## The sweep, and what its findings have in common

Tony's instruction was to update the whole master plan rather than only
Section 5a. Every numeric and status claim was measured against HEAD
instead of read forward, and all 63 file references were resolved
against both repos. Twenty-nine items had moved; writing the patch
surfaced five more, for 34.

The PATTERN is the part worth carrying:

- **Five ledger items the plan called open had closed.** L-087
  (2026-07-15), L-108 (07-12), L-120 (07-27), L-151 (07-27), L-162
  (07-29). None noticed in a month.
- **One stated REASON was false while its conclusion held.** The plan
  said `palomas_orrery_helpers.py` "imports tkinter directly" and made
  the split a Phase 2 requirement. At HEAD the file has zero tkinter
  references. The requirement is still real -- three modules in its
  TRANSITIVE closure import tkinter -- but the reason had been wrong
  since July.
- **Two size figures disagreed inside one document.** Section 1 said
  436 MB / 588 headroom; Section 3a said 474 / 526. Measured: 439 /
  ~585. Nothing compares them, so nothing caught it.
- **Two questions the plan told a future session to resolve BY LOOKING
  were answered by looking.** Section 7 decision 12's constructor count
  is TWO (`HORIZONS_MAX_DATE`, and `stellar_class_labels` with twelve
  `dict()` calls the August 11 count missed). Decision 16's Jupiter ring
  count is FOUR.
- **Three internal contradictions**, each between two parts of one file:
  Layer 3 "enabled with a known open issue" forty lines after
  "RETIRED"; L-151 unbuilt in the closing block and done in the header;
  the JS layer "next after scanner work" in a document whose header
  now says it is first.

---

## The finding that became a rule

**A correction written into the code does not travel to the prose that
describes it, and nobody is assigned to carry it.**

`constants_new.py` had said 15 R_sun since 2026-08-22, when L-209
corrected DeForest at source. `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`
still said 17 the next day -- INSIDE the paragraph that file had written
to correct an EARLIER wrong claim about the same row, in a document
whose own text argues that a wrong claim in a summary outlives the
conversation it came from. The same file named `STREAMER_BELT_RADII`,
which L-224 had renamed the day before, and called L-214 "designed and
unbuilt, and the next scheduled work" two days after L-214 went DONE.

Three instances, one file, one cause. The provenance machinery watches
the code; nothing watched whether the documents describing it kept up.

**This is now safe-file-editing 1.8, "The Correction Does Not Travel"**
(L-226), scoped one level out from Stamp What You Change: that section
governs the file the patch is editing, this governs the OTHER files
quoting the value it just changed. Its confirming question is Tony's,
pointed sideways: WHAT ELSE SAYS THIS?

**And it was found in the wild the same afternoon.** `resolver.py` and
`cache_reader.py` both still said `served_window` "is null at HEAD" and
"tracked with F1." F1 (L-118) closed 2026-07-22 and the cache carries a
real window. The gallery-assembler skill had carried "fix next time
you're in that file" as a known-stale note since August 5. Fixed in
`patch_L154_1` -- the rule applied to itself, hours after being written.

---

## Two errors of Claude's, and how they were caught

**1. The ASCII sweep was declined and should not have been.**
`patch_L221_2` found 23 non-ASCII characters and reported them instead
of fixing them, reasoning the encoding gate was scoped to delivered
code. Tony overruled it. The sharper point, now in the skill: Stamp What
You Change ALREADY said markdown is not an exception, so the skill's two
halves disagreed and the reader followed the narrower one. Swept in
`patch_L221_3`. Caught by Tony reading run output, not by any check.

**2. The date was wrong.** `patch_L221_2` stamped its authorship
2026-08-22 throughout and ran on the 23rd. Ruling dates were right;
eight authorship and measurement dates were not. Fixed one at a time
rather than swept, because the distinction between when something was
decided and when it was written is what this project's anchors exist to
preserve.

**Gates that earned their keep.** `patch_L221_2`'s first build was
rejected by its own line-loss gate -- three anchors were not cut on line
boundaries and would have silently dropped text no edit claimed to
rewrite. Its ASCII gate had to be rewritten: a blunt "inserted text must
be ASCII" test refused an anchor that merely CARRIED an existing prime.
It now checks that no edit RAISES the non-ASCII count, and separately
that the script's own bytes are clean. That form was reused in every
later patch.

---

## Skills

`safe-file-editing` went **1.7 -> 1.8** this session (L-226). All three
stores were reconciled and verified at `15741822`: the skill file
declares 1.8, the generated manifest in `PROJECT_INSTRUCTIONS.md` reads
1.8, and Tony reinstalled to the account.

**CARRIED OBLIGATION.** A mid-session reinstall cannot be verified from
inside the session that makes it. This session loaded 1.7, correctly at
the time. **The next session confirms its loaded copy reads 1.8 before
any file-editing work.**

Also loaded and matched: `ledger-and-session-records` 1.8,
`gallery-assembler` 1.1. No other bumps.

Maintenance last ran clean at `15741822`: 11 of 11 gating checkers, 2
report-only (worksheet checker 66 of 105 routed / 8 clean; provenance
scanner 292 Tier-1 in the scanned tree).

---

## (do) and (decide) -- Tony-side

- **(do) Mode 5, carried from 2026-08-22. ONE Sun render closes both
  outstanding items.** The streamer band (L-224) should read as a band
  with a dissolving stalk, not a smear -- if it smears, raise
  `fade_exponent` in `STREAMER_BAND_DEFAULTS`
  (`planet_visualization_utilities.py`); that is a parameter, not a
  rewrite. And the Alfven shell (L-209) should render one solar radius
  larger than before, 18.8 -> 19.7, still nested inside the 50 R_sun
  outer corona. L-209's remaining item is explicitly "Tony's eyes on a
  plot, not a build" -- the code already reads 19.7.
- **(decide)** Two proposed RICE scores, both Claude's, both tagged
  `**Note:**` so neither reads as a ruling: **L-225** at 2/3/80/2
  (score 2.4) and **L-226** at 3/3/90/1 (score 8.1). Confirm or
  redirect, then re-run `ledger_index.py`.
- **(do)** Archive the loose patch scripts to `documentation/`.
  `patch_L154_1` lives in the GALLERY repo at `gallery/assembler/` and
  is the first script this project has aimed at that repo -- where it
  should live is Tony's call, and there is no precedent.

---

## A convention defect, reported not fixed

**There are two `patch_L221_2_*` scripts in `documentation/`:**
`patch_L221_2_critical_path_update.py` (August 20) and
`patch_L221_2_master_plan_v19.py` (today). Claude picked the number
having seen only `_1`, without listing the family first.

This defeats the point of the sequence number -- "sort order is then run
order" (safe-file-editing 1.8). It is adjacent to L-219, which is open
on the convention's inability to express CROSS-handle run order; this is
the WITHIN-handle collision case, which L-219 does not cover. Renaming
an archived one-shot script would rewrite the record, so it is left
alone and written down here.

---

## Next session

**The second half of L-154: the client-side renderers.**

The data is in place and measured. The renderers read `ring_system`,
`radiation_belts`, `atmosphere_shell` and `van_allen_belts` out of
`FeatureRequest.params` and turn them into traces. Saturn on screen,
unfingerprinted, which v19 explicitly allows -- drawing is not locking.

**First, three cheap things:**
1. Confirm the loaded `safe-file-editing` reads **1.8** (above).
2. **L-154's ledger entry does not yet record that its first half
   shipped.** It reads OPEN with no build note. One anchor, worth
   fixing at session start while it is cheap.
3. SHA round trip: orrery `15741822`, gallery `8ec4f261`.

**Then Artifact 2's provenance slice.** Thirty measured numbers:
Saturn's seven rings at two fields each, Jupiter's four rings at three,
the belts' three distances plus one thickness. `n_rings` and `n_points`
are DECLARED, not findings. Saturn has no radiation belts in the served
cache or in `objects_config.json` -- only Jupiter's.

Then lock Artifact 2, then ship.

**Not on that path:** segment 2 (transport), the general audit, and
L-225.

---

*Session written August 23, 2026 with Anthropic's Claude Opus 5. Orrery
built on `38923c1cc64d492006135ec77779e1fb592582d5`, pushed at
`15741822cb8f54ac26fc252aa8382cd90534570d`; gallery
`493a0bd7fcba4067c56db318357889e965fba514` to
`8ec4f261013f09697d649efd25c8a746bffeff64`. Both confirmed against the
live remote. Supersedes the earlier draft of this handoff, which was
written before L-226 and the resolver work and is stale in four places.*
