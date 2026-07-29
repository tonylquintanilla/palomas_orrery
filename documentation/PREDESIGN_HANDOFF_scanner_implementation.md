# Preliminary Design Handoff: Provenance Scanner Implementation Design (L-155/156/158/160)

Tony Quintanilla, PE | Claude Sonnet 5 | July 27, 2026

**Built on:**
- orrery (palomas_orrery) @ `9c9c9352c02e3d86a8c6628e2e575a62b758fb60`
- gallery (tonyquintanilla.github.io) @ `519ca776c811c0e6442560d55f501c70b13c5bbe`

**Type:** PRELIMINARY DESIGN (zero code). This is NOT a build request. The
policy-level decisions for this cluster are closed; what's missing is the
implementation-level design that bridges "here's the rule" to "here's how
the code enforces it." Building straight from policy language risks
guessing at architecture calls that deserve a real decision -- see
section 2 for the concrete evidence.

---

## Who you're writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist -- not a professional software developer and
not a formally trained astronomer. He builds this project (Paloma's
Orrery, palomasorrery.com) as a "vibe coder," through conversation with AI
partners, and holds sole commit authority and final judgment throughout.
The codebase's discipline is the product of Claude-Tony collaboration, not
evidence of Tony's own programming background -- please don't read code
quality as a signal about that. Unpack jargon rather than assume
programmer or astronomer fluency.

---

## 1. What's already decided -- don't relitigate this

The full policy is closed, via Fable 5's design (July 22), Sonnet 5's
review, a Fable 5 broad-review pass, and a three-AI calibration round
(Gemini 3.1 Pro, GPT 5.5, Fable 5, Sonnet 5 synthesis, Tony's final call).
Full record in `LEDGER_CONSOLIDATED.md`'s `[L-156]`, `[L-155]`, `[L-158]`,
`[L-160]` entries and `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` /
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`. Summary:

- **Criticality: two categories, MEASURED and RELATIONAL**, judged by
  category (independently-measured vs. derived-from-something-tracked),
  not by import count. Ring geometry is MEASURED ("rings are better
  defined" than planetary shells generally -- Tony). Orbital period and
  radius share the top category despite different failure shapes
  ("these are fundamental data" -- Tony). An explicit `undetermined`
  sentinel exists for anything that can't be confidently placed.
- **Vulnerability: four rungs**, unchanged in count from today --
  `V1 FETCHED` (live pipeline), `V2 CROSS-CHECKED` (structured, dated,
  independently-verified, records whether the check was blind/non-
  anchored, never auto-promotable to V1), `V3 SOURCED` (cited-unchecked,
  merged with what would have been a separate "stale" rung), `V4 RECALLED`.
- **Derived values are a rule, not a rung**: runtime-derived values
  inherit their weakest input's V-rung once the derivation logic itself
  clears one cross-check; values derived once and then frozen as a
  literal get no special treatment (plain V3, the comment is their
  citation).
- **Pinning checks live inside `provenance_scanner.py`**, absorb
  `test_constants_provenance.py`'s existing logic, fail loud (nonzero
  exit) -- the only hard exit-code gate in the cluster.
- **Tier-1 never gets an auto-exit gate**, at any threshold -- permanent
  banner, human judgment, indefinitely.

If anything below conflicts with this section, this section wins -- come
back and flag it rather than silently deciding it differently.

---

## 2. What's NOT decided -- this is the actual ask

Five concrete gaps, found by reading the live scanner rather than just the
design prose. Please produce a design (pseudocode / decision logic / the
table itself, not working code) for each.

### 2a. How MEASURED/RELATIONAL integrates with the existing five-level scale

`provenance_scanner.py` already has a criticality taxonomy wired into
`action_tier()`'s thresholds:

```python
C_COSMETIC    = 1   # Colors, label positions, descriptive text
C_INTERNAL    = 2   # Used in code but not displayed
C_LOADBEARING = 3   # Drives geometry, shell radii, orbit params
C_PUBLIC      = 4   # Visible in hover text, gallery, Instagram
C_PROPAGATING = 5   # Imported by other modules, affects calculations

def action_tier(score):
    if score >= 16: return 1
    if score >= 10: return 2
    if score >= 5:  return 3
    return 4
```

and a role-based fallback that only fires when import-count resolution
comes up empty (the actual root-cause path):

```python
def _role_based_criticality(unit):
    """Fallback criticality when per-name resolution doesn't apply."""
    if unit.kind == 'dict' and unit.name:
        lname = unit.name.lower()
        if lname in ('colors',) or 'label' in lname or 'color' in lname:
            return C_COSMETIC, f"Cosmetic dictionary ({unit.name})"
    role = unit.role or ''
    if unit.kind == 'dict' and role.startswith('rendering'):
        return C_LOADBEARING, f"Geometry dict in {role} module"
    if unit.kind == 'constant' and role in ('computation', 'data'):
        return C_LOADBEARING, f"Numeric constant in {role} module"
    return C_INTERNAL, "Internal use (not imported externally)"
```

`unit.role` here is the *module's* functional role from `module_atlas.py`'s
`ROLE_MAP` (L-163) -- data/rendering/devtool/etc. It's a per-module
classification, not a per-constant one, which is worth naming explicitly
if it turns out to matter: a single "rendering" module can hold both a
MEASURED ring radius and a RELATIONAL derived color fraction.

**Design this:** does MEASURED/RELATIONAL replace the five-level scale
outright (and if so, does `action_tier()`'s scoring math need
re-deriving, since the score ceiling would change)? Does it sit alongside
it as a second axis? Or does it just replace `_role_based_criticality`'s
guessing logic for constants specifically, landing on the *existing*
`C_PROPAGATING`/`C_PUBLIC` numeric values under clearer names (they
already happen to equal 5 and 4)? Any of these could be right -- this
just hasn't been decided at the code level yet.

### 2b. The `undetermined` sentinel's trigger condition

Decided: it exists, gets its own banner (same visibility as Tier-1), and
must be spelled `undetermined` (matching L-163's naming, not
`UNCLASSIFIED`). Not decided: what code path actually assigns it. Is it
the `else` branch above (currently `C_INTERNAL`)? A new explicit check
that fires when none of MEASURED/RELATIONAL/COSMETIC pattern-match?
Design the actual trigger.

### 2c. L-155's key-path mapping table

The ledger's own words: "finalize the explicit key-path mapping...as a
table, not name-matching" -- this doesn't exist yet. What needs mapping,
concretely: `objects_config.json`'s `features` values (gallery repo) on
one side, `CENTER_BODY_RADII[x]` (physical radius) and the specific ring/
belt/atmosphere dict literals in `earth_visualization_shells.py` /
`jupiter_visualization_shells.py` / `saturn_visualization_shells.py` (the
orrery repo) on the other. Design: the actual table (gallery key -> orrery
source expression), and where the pinning function lives in
`provenance_scanner.py` (a new function alongside the existing
`find_cross_file_issues`, per the settled design -- but its signature and
call site aren't spec'ed).

### 2d. The five comprehensive-sweep findings (L-156)

Folded into L-156's Gap, still open: the never-fixed inline `'source':`
dict-value pattern; the duplicate-detector's same-file/dict-kind blind
spots; missing magnetosphere unit vocabulary; the comet accepted-residual
that contradicts the new scheme; "Option A" (retired -- confirm nothing
still assumes it). Each needs an actual resolution, not just a bug ticket.

### 2e. L-158's derived-value detector

The two-factor check (`# Derived:` comment + AST confirmation it's
actually computed) is the settled mechanism, but the comment convention
is already used inconsistently in `constants_new.py`. Four instances at
current HEAD:

```python
# Derived: 695700 / 149597870.7 = 0.004650467...
# Derived: 149597870.7 / 299792.458 / 60 = 8.31675...
# Derived: core extends to ~0.2 solar radii
# Derived: radiative zone extends to ~0.7 solar radii
```

The first two are real formulas. The last two are descriptive notes that
happen to start the same way -- not derivations at all. Design how the
detector tells these apart (the AST-confirmation half of the two-factor
check should already handle this -- `provenance_scanner.py` has
substantial AST infrastructure already, including expression evaluation
around line 757-770 -- but confirm it actually discriminates "the comment
is followed by a computed assignment" from "the comment is followed by a
plain string or unrelated literal" before assuming it's ready to reuse).

---

## 3. What to produce

A design document -- pseudocode, decision tables, the key-path mapping
table itself, not working code -- covering 2a through 2e. This comes back
to Sonnet 5 for review (same pattern as your original design going
through review before Fable's broad-review pass) before Phase 1-3 of the
actual scanner build starts.

## 4. Out of scope for this pass

L-157 and L-161 (the two Gemini cross-check sweeps) are separate
workflow items, not scanner architecture. L-162 (`CENTER_BODY_RADII`
naming) is an independent prep session -- worth landing before your Phase
3 pinning-table design if it's already done by the time you pick this up
(simplifies 2c to 18 named constants instead of 3 named + 15 dict-path
lookups), but not a hard dependency for this design pass.

## 5. Where this goes next

Back to Sonnet 5 for review, then the actual Phase 1-3 build (still
Opus 5), then Mode 5 acceptance isn't relevant here (no visual output --
this is a backend tool) but the agentic-pre-test protocol applies before
any delivery once code exists.

---

*Handoff drafted July 2026 with Anthropic's Claude Sonnet 5. Every code
snippet above copied verbatim from a fresh clone at the SHA anchored
above, not paraphrased from the design documents.*
