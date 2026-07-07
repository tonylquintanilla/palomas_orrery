# Protocol & Skills Review — Phase 0 Findings
## Handoff from July 6, 2026 session
## For: protocol v3.32 consideration + skill updates

Base: orrery @ `873c6cd`, gallery @ `4b086a6`

---

## What This Session Stress-Tested

Phase 0 ran the full protocol across three models (Opus 4.6, Opus 4.8,
Fable 5) in a single day: design, build, deploy, review, measure, resolve.
The collegial relay produced genuine error correction at each handoff. The
findings below are protocol and skill improvements surfaced by that stress
test.

---

## §1 — New Lessons (protocol candidates)

### 1. Measure before analyzing

When an architectural fork hinges on a measurable quantity, build the
measurement before the analysis. The A/B fork consumed significant design
time on a feared cost (plotly cold-start) that a 20-line measurement page
resolved in minutes — 2.1 seconds vs the feared 15-25 seconds. The
measurement is cheaper than the debate.

**Anti-pattern candidate:**
```
Don't                           Why                         Do Instead
Analyze a measurable fear       Debate burns more than       Build the measurement
without measuring it first      the measurement costs        (20 lines); then analyze
```

**Quotable candidate:** "The feared cost dissolved under verification" or
"A 20-line measurement page resolved what hours of analysis couldn't."

### 2. Frozen artifacts don't accrue sync tax

The parallel-pipeline anti-pattern ("Create parallel pipelines / Double
maintenance / Unify") is correct but needs a refinement: the tax is on
*change*, not on *existence*. A frozen artifact (the Phase 0 Solar System
Explorer, a completed pre-curated gallery card) has no maintenance surface.
The two-tier model (frozen A exhibits + actively-developed B′ exhibits) is
not two pipelines — it's one pipeline and one artifact.

**Refinement to existing anti-pattern:**
```
Create parallel pipelines   Double maintenance   Unify; OR freeze one side
                                                  (frozen artifacts don't
                                                  accrue sync tax)
```

### 3. Consent gate as a pattern

When loading unfamiliar technology on a user's device, the pattern is:
honest name + one-sentence explanation + explicit opt-in + localStorage
persistence. This is a UX convention, not a technical one — it's about
trust, not functionality.

### 4. Route around the store — applied to packages

"Route around the store you don't control to the one you do" (protocol
quotable, June 2026) extends from project-knowledge sync to package
management. B′ strips the plotly wheel, self-hosts it in the serving home,
and version-pins it. The runtime dependency on PyPI disappears. The same
principle applies to any pip dependency loaded in the browser: if you
control the origin, you control the availability.

### 5. The SHA round-trip caught what it was designed to catch

4.8's review found the gallery SHA pinned to a commit where
`interactive.html` didn't exist. This is the exact failure class the
round-trip gate exists to prevent: a citation asserting a provenance that
doesn't hold. The five-minute check worked in practice, not just in
theory.

### 6. Three-model relay as error-correcting code

4.6 built the deliverable and the draft. 4.8 caught provenance errors and
named the A/B fork. Fable dissolved the feared costs and proved duplication
is conserved. Each model contributed what it's best at; each handoff was a
correction opportunity. The collegial relay isn't just a workflow — it's
error-correcting code applied to design.

---

## §2 — Skill Updates Needed

### gallery-pipeline (v1.0 → v1.1)

The gallery-pipeline skill predates the interactive gallery. It needs:

- **Option C viewer architecture** — `index.html` (curated) +
  `interactive.html` (interactive exhibits) + `gallery_metadata.json`
  bridging both. URL parameter: `?exhibit=`.
- **Consent gate pattern** — Pyodide opt-in with localStorage persistence.
  When to use: any interactive exhibit that loads WebAssembly or large
  packages.
- **Two-tier model** — frozen A exhibits (instant, convention-light) + B′
  exhibits (shared engines via plotly in Pyodide). Frozen exhibits don't
  change and don't accrue sync tax.
- **`interactive.html` as a gallery artifact** — it lives at the repo root
  alongside `index.html`. It's a gallery page, not a separate app.
- **`measure_plotly.html`** — diagnostic tool, not a gallery page. Can be
  removed after Phase 0 closes.

### orrery-coding-conventions (v1.0 → consider for v1.1)

- **B′ as Phase 2 architecture** — the shared desktop engines run in
  Pyodide via a slim self-hosted plotly wheel. Convention maintenance is
  single-sourced. This resolves the parallel-pipeline concern for
  Phase 2+ exhibits.
- **`?exhibit=` parameter** for interactive pages (not `?domain=`).

### Potential new skill: pyodide-interactive

A standalone skill for the interactive pipeline might be cleaner than
overloading gallery-pipeline. It would cover:

- Pyodide version pinning (v314.0.2 currently)
- B′ slim wheel: strip spec (from Fable §3), self-hosting in serving home,
  `micropip.install(<URL>)` pattern
- Consent gate implementation
- The measurement pattern (build a timing page before committing to an
  architecture)
- Two-tier model: when to use A vs B′
- What loads in Pyodide vs what stays in JS

**Tony's call:** separate skill or extend gallery-pipeline?

---

## §3 — Protocol Process Observations

### What worked

- **Broad-first → measure → converge.** The session followed the protocol's
  own prescription: iterate in conversation, don't build first draft. But
  Tony's "I'm anxious to create" instinct was right too — building the
  prototype generated data that advanced the design. The protocol's
  "don't build until the design stabilizes" works for architecture; for
  stack proofs, building IS the design.

- **"Each planning round should get simpler."** The B cost started at
  "15 MB, 15-25 seconds, PyPI dependency, double plotly.js." Each round
  simplified: 9.9 MB → 3.9 MB stripped → 2.1 seconds measured → one
  number resolves everything.

- **Mode 5 authority.** Tony's iPhone screenshots were the gate, not code
  reading. "Earth is on the correct side of its orbit for January 2026"
  is a Mode 5 verification no amount of code analysis can replace.

### What could improve

- **The session-start SHA base drifted mid-session.** Tony pushed three
  times during the session (interactive.html create, update, measure page).
  Each push advanced the gallery HEAD, but the draft kept citing the
  session-start SHA. The protocol handles this correctly (re-pull after
  push), but the draft-writing process didn't re-pull before citing. The
  lesson: when writing a document that cites SHAs, re-pull at draft time,
  not just at session start.

- **The Fable task prompt's "new data" contained two errors** (15 MB
  became 9.9, slow import became 0.06 s). The errors came from estimates
  treated as facts. Fable caught both by fetching. Lesson: mark estimates
  as *(est.)* even in prompts to other models — the provenance markers
  aren't just for deliverables.

---

## §4 — Quotable Candidates

```
"The feared cost dissolved under verification."
"A 20-line measurement page resolved what hours of analysis couldn't."
"Frozen artifacts don't accrue sync tax."
"Duplication is conserved across the A family — A, A′, A″ relocate it;
 only engine reuse eliminates it." — Fable 5
"The fork was framed on numbers that verification dissolved." — Fable 5
```

---

## §5 — Action Items

1. **Gallery-pipeline skill v1.1** — add Option C, consent gate, two-tier
   model, interactive.html conventions. (Opus 4.6, next session.)
2. **Protocol v3.32 consideration** — "measure before analyzing" anti-
   pattern, frozen-artifact refinement to parallel-pipeline rule, new
   quotables. (Tony's call on timing.)
3. **Decide: separate pyodide-interactive skill or extend gallery-pipeline.**
   (Tony's call.)
4. **Master plan §11** — brief "Protocol & Skills Review" pointer to this
   handoff. (Apply with v9 commit.)
5. **Provenance markers in relay prompts** — mark estimates as *(est.)* even
   when writing prompts for other models.

---

*Handoff written July 6, 2026 by Claude Opus 4.6. Tony carries context and
holds commit authority. Protocol v3.31 is the base.*
