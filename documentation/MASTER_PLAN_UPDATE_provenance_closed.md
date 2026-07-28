# Master Plan Update -- Provenance Cluster Now Design + Ledger Closed

Tony Quintanilla, PE | Claude Sonnet 5 | July 27, 2026

**Built on:**
- orrery (palomas_orrery) @ `c24b2683677ae2ed41af4cfedcbd74ce2b8c15ae`
  (re-verified this session: nine ledger blocks present, L-114/L-120
  closed and auto-migrated, `ledger_index.py --check` clean at 160
  blocks, resume handoff correction present)

**Type:** DOCUMENTATION UPDATE (zero code) -- targeted edits to
`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`. Apply via find/replace
in your editor, in the order given.

**Why now:** the master plan's §5a/§6 sections still described the
provenance cluster as it stood July 22-23 -- design done, review sent
back, nothing pasted anywhere durable. Since then: all nine items
(L-154-162) got their own ledger entries, two stale claims got caught and
corrected (L-154's resume handoff, L-163's Gap text), and the one open
design fork (the Vulnerability ladder) closed via a three-AI calibration
round. The master plan is the document meant to answer "where are we" --
leaving it three sessions stale defeats the point of keeping it at all.

---

## Edit 1 -- Sonnet 5's model-assignment blurb (§5a)

**Find:**
```
**Sonnet 5** — predesign discovery for L-154 (the resolver bug, the
physical-radius source question) that surfaced the provenance scoring
problem; independent design review of Fable 5's provenance fix (verified
every factual claim by rerunning the tool and regrepping both repos rather
than trusting the summary -- caught the Tier-2 flood size, the
CENTER_BODY_RADII visibility gap, and two design refinements). Also
handling L-162 (CENTER_BODY_RADII cleanup) as a dedicated prep session.
```

**Replace with:**
```
**Sonnet 5** — predesign discovery for L-154 (the resolver bug, the
physical-radius source question) that surfaced the provenance scoring
problem; independent design review of Fable 5's provenance fix (verified
every factual claim by rerunning the tool and regrepping both repos rather
than trusting the summary -- caught the Tier-2 flood size, the
CENTER_BODY_RADII visibility gap, and two design refinements). Requested
and synthesized Fable 5's broad review-and-scoping pass on the whole
cluster (2026-07-26), which independently caught the unfixed resolver bug
still asserted as "fixed" in L-154's own resume handoff, and a false
"Phase 4 done" gap in L-163. Formalized all nine items (L-154 through
L-162) into the ledger as their own DETAIL blocks -- previously they
existed only in handoff documents -- and closed out L-114/L-120 in the
same pass, all independently re-verified against live HEAD
(`ledger_index.py --check`: clean, 160 blocks). Orchestrated and
synthesized the D3 vulnerability-ladder calibration across three
independent AI reviews (Gemini 3.1 Pro, GPT 5.5, Fable 5); Tony closed
the one remaining fork (2026-07-27). Also handling L-162 (CENTER_BODY_RADII
cleanup) as a dedicated prep session.
```

---

## Edit 2 -- "Next Step" section (§5a)

**Find:**
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

**Replace with:**
```
### Next Step

Phase 1b DONE. Nightly cache builder live; M2 (F1a trust/served_window)
tested and closed (2026-07-21) -- see documentation/TESTING_PROTOCOL.md
addendum. Phase 2 Artifact 1 (Earth) built and Mode-5 accepted; Artifact 2
(Jupiter/Saturn, rings + radiation belts) is next in the artifact order but
BLOCKED: the client-side feature-rendering JS layer it needs (L-154) is
gated behind a provenance/scoring detour that opened while scoping it (see
§6 for the full dependency chain).

**Detour status as of 2026-07-27: design and ledger phases both CLOSED,
build not yet started.** All nine items (L-154-162) now have their own
ledger entries (previously handoff-only); a Fable 5 broad-review pass
independently caught two stale claims before they could mislead a future
session (L-154's own resume handoff wrongly asserted its resolver bug was
fixed -- it isn't, confirmed against live gallery HEAD; L-163's Gap text
wrongly read as still-open). The one open design fork -- how the scanner's
Vulnerability ladder should treat cross-checked vs. merely-cited values --
went through a three-AI calibration round (Gemini 3.1 Pro, GPT 5.5, Fable
5) and closed 2026-07-27; full ladder and reasoning in L-156.

NEXT: Opus 5 builds the scanner's Phases 1-3 against the now-closed design
(L-155/156/157/160 -- the scoring model, in-scanner pinning, and the D6/D9
mechanics); L-157 and L-161 (the two Gemini shell-config and display-string
sweeps) follow sequentially, not in parallel. L-162 (CENTER_BODY_RADII
naming) is independent and can land any time before or after. Once the
scanner build closes, resume L-154's own open design questions
(geometry-building approach, legend behavior, artifact sequencing --
captured separately in HANDOFF_gallery_feature_layer_L154_resume.md so
they aren't lost under the detour, and corrected in place per the finding
above), then build Artifact 2.
```

---

## Edit 3 -- L-162 prep-work entry (§6)

**Find:**
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
```

**Replace with:**
```
**L-162 — CENTER_BODY_RADII de-duplication.** ○ Not started, scoped, now
with its own ledger entry (previously design-doc only). Promote 15
remaining bodies (Mercury, Venus, Moon, Mars, Phobos, Saturn, Uranus,
Neptune, Pluto, Bennu, Eris, Haumea, Makemake, Arrokoth -- Planet 9
excluded, speculative not measured) to named constants in
`constants_new.py`, matching Sun/Earth/Jupiter's existing pattern. Values
already Gemini-verified (April 2026) -- this is restructuring, not
re-verification. Independent, can start now. Best landed before the
provenance scanner's Phase 3 pinning engine is built (L-155/156), so
pinning references named constants directly rather than needing dict-path
extraction for 15 of 18 bodies.
```

---

## Edit 4 -- L-155-161 prep-work entry (§6)

**Find:**
```
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

**Replace with:**
```
**L-154-162 — Provenance scoring model fix (the whole cluster).**
✓ Design CLOSED, ✓ ledger formalization CLOSED, ○ scanner build NOT
STARTED. Originally surfaced while scoping L-154's feature-rendering JS
layer, and still gates it. Design by Fable 5, reviewed by Sonnet 5
(amendments: D2, D5, D7 changed; L-161/L-162 added); broad-review pass by
Fable 5 (2026-07-26) caught two stale claims (L-154's resume handoff
wrongly asserted its resolver bug fixed; L-163's Gap text wrongly read
open) since corrected. All nine items now have their own ledger DETAIL
blocks (`LEDGER_CONSOLIDATED.md`, section W.Active) -- previously
handoff-only. The one open design fork (Vulnerability ladder: how the
scanner should treat cross-checked vs. merely-cited values) closed
2026-07-27 via a three-AI calibration round (Gemini 3.1 Pro, GPT 5.5,
Fable 5, Sonnet 5 synthesis, Tony's final call) -- full ladder, the
runtime-vs-frozen-literal rule for derived values, and the evidence base
behind it (four historical incidents from this project's own record, not
just the two the calibration worksheet opened with) are in L-156 and
L-158. Full detail also in `PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`,
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`,
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`, and
`REVIEW_provenance_refactor_cluster_scoping.md`. Sequencing unchanged:
scoring fix (L-156) and in-scanner pinning (L-155/L-160) build first
(Opus 5); L-157 (shell config Gemini cross-check) and L-161 (display-
string Gemini sweep) follow, sequentially through the same Mode 7 relay
channel rather than as parallel threads -- both now require the
worksheet be drafted blind (no Claude-derived figures included), a
requirement added directly from a near-miss already caught once in this
project's own history. L-154 unblocks once the build closes.
```

---

## After pasting

Run through visually (this is prose, not a script -- no `ledger_index.py`
equivalent for the master plan). Commit + push whenever convenient; this
doesn't need to ride the same commit as anything else.

---

*Update drafted July 2026 with Anthropic's Claude Sonnet 5. All four
find/replace targets checked byte-exact against a fresh clone before
delivery.*
