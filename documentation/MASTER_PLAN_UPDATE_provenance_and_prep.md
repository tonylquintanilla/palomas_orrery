# Master Plan Update -- Provenance Detour and Prep Work

Tony Quintanilla, PE | Claude Sonnet 5 | July 23, 2026

**Applies to:** `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
**Built on:** orrery @ `9b4571851184e599f72de928cada16d30c9010f6`

Targeted edits, not a full-file replacement, per the same discipline used
for any large existing file -- apply each block below via find/replace in
your editor. Four edits, in file order.

---

### Edit 1 -- "Next Step" (end of §5a), bring current

**Find:**
```
### Next Step

Phase 1b build UNDERWAY. The standalone `gallery_cache_builder.py` +
`objects_config.json` + an offline smoke test are built and offline-verified
(47 checks, py_compile clean; provenance to orrery `4e2629c`). NEXT: live dry-
runs on Tony's hardware (manifest v2 S10 -- voyager_1 ephemeris start, encke
solution-Tp + Mode-5 Tp match), first full build, schedule nightly + backup.
```

**Replace with:**
```
### Next Step

Phase 1b DONE. Nightly cache builder live; M2 (F1a trust/served_window)
tested and closed (2026-07-21) -- see documentation/TESTING_PROTOCOL.md
addendum. Phase 2 Artifact 1 (Earth) built and Mode-5 accepted; Artifact 2
(Jupiter/Saturn, rings + radiation belts) is next in the artifact order but
BLOCKED: the client-side feature-rendering JS layer it needs (L-154) is
gated behind a provenance/scoring detour that opened while scoping it (see
§6 for the full dependency chain). NEXT: close the provenance work
(L-155/156/157/158/159/160/161, L-162), then resume L-154's own open
design questions (geometry-building approach, legend behavior, artifact
sequencing -- captured separately in
HANDOFF_gallery_feature_layer_L154_resume.md so they aren't lost under the
detour), then build Artifact 2.
```

---

### Edit 2 -- Model Assignments (§5a), add Sonnet 5's role

**Find:**
```
**Opus 4.6** — daily conversational partner, iterative build. Phase 1b design
led and converged. Phase 1b build (CORS check, export script, coverage index).
Helpers split, all assembler and interactive page builds.
```

**Add directly after it:**
```

**Sonnet 5** — predesign discovery for L-154 (the resolver bug, the
physical-radius source question) that surfaced the provenance scoring
problem; independent design review of Fable 5's provenance fix (verified
every factual claim by rerunning the tool and regrepping both repos rather
than trusting the summary -- caught the Tier-2 flood size, the
CENTER_BODY_RADII visibility gap, and two design refinements). Also
handling L-162 (CENTER_BODY_RADII cleanup) as a dedicated prep session.
```

---

### Edit 3 -- §6 Prep Work, add the new items

**Find:**
```
**`palomas_orrery_helpers.py` split** — ○ Not started. Separate computation
from tkinter GUI helpers. Computation the assembler needs:
`calculate_planet9_position_on_orbit`, `rotate_points2`,
`calculate_axis_range`. Required before Phase 2.
```

**Add directly after it:**
```

**L-162 — CENTER_BODY_RADII de-duplication.** ○ Not started, scoped.
Promote 15 remaining bodies (Mercury, Venus, Moon, Mars, Phobos, Saturn,
Uranus, Neptune, Pluto, Bennu, Eris, Haumea, Makemake, Arrokoth -- Planet 9
excluded, speculative not measured) to named constants in
`constants_new.py`, matching Sun/Earth/Jupiter's existing pattern. Values
already Gemini-verified (April 2026) -- this is restructuring, not
re-verification. Independent, can start now. Best landed before the
provenance scanner's Phase 3 pinning engine is built (L-155/156), so
pinning references named constants directly rather than needing dict-path
extraction for 15 of 18 bodies.

**L-155/156/157/158/159/160/161 — Provenance scoring model fix.**
○ Design done (Fable 5), reviewed (Sonnet 5, this session), amendments
sent back. Not a gallery-track item originally -- surfaced while scoping
L-154's feature-rendering JS layer and now gates it. Full detail in
PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md and
DESIGN_REVIEW_provenance_scoring_and_pinning.md. Sequencing: scoring fix
(L-156) and in-scanner pinning (L-155/L-160) build first; L-157 (shell
config Gemini cross-check) and L-161 (display-string Gemini sweep) follow,
sequentially through the same Mode 7 relay channel rather than as parallel
threads. L-154 unblocks once these close.
```

---

### Edit 4 -- §7 Open Decisions, add a pointer (optional, low priority)

Given §9 already states "the existing ledger is unaffected" as this
document's own scope boundary, the provenance work's detailed decisions
belong in the ledger and the two documents named above, not duplicated
here. No new numbered Open Decision needed -- Edits 1-3 are sufficient to
keep this document orienting correctly. Skip this edit unless you want an
explicit cross-reference line added to §7's list; not required for
orderliness.

---

*Patch note written July 2026 with Anthropic's Claude Sonnet 5.*
