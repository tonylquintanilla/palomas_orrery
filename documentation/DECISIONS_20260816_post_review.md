# Decisions -- 2026-08-16 -- post-review rulings and the build package

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
No code changed during the review window; the anchor still describes
the tree.

Lands in `documentation/`. Ledger material for L-192 / L-195 and two
new handles.

---

## Rulings

### 1. The returned request gets its own checking path

A returned `REQUEST_<batch>.md` is bound to claims by key on a
separate path. Source annotations are NOT repointed at it, because
repointing erases which worksheet the original `# Cross-checked:`
claim referred to. The existing annotation-to-worksheet audit stays
exactly what it is.

The annotation is **append-only**: a new check adds a
`# Cross-checked:` line beside the old one and never edits or deletes
it. The old worksheet stays on disk untouched.

Unblocks review blockers 3, 4, 5 and 6 -- two-verdict reading, string
key binding, and shift enforcement all belong on this new path, so
building them into the annotation path first would build them twice.

### 2. Disagreement between checks is recorded by a `# Resolved:` leg carrying a ledger handle

Third provenance kind. `# Source:` is the value's provenance,
`# Cross-checked:` is the check's, `# Resolved:` is the disagreement's.
It records which disposition fired -- mechanical (SEND BACK, known
cause) or conversation (CONVERSATION, three live causes, no tool
assigns them) -- and where the reasoning lives.

**The handle is the point.** The leg must carry a ledger handle the
checker verifies resolves to a real item with a status. A dated prose
note cannot fail, and a line that clears suspicion while being
unverifiable is cite-to-clear at a third layer -- worse here than at a
citation, because a resolution is the line a future reader trusts most
and can check least.

Naming: `# Resolved:` rather than `# Resolution:`. `resolution` is
already a worksheet COLUMN role in the followup worksheets, where it
carries verdicts. Different namespace, nothing would break, but one
word meaning two things is the drift class this protocol exists to
kill.

Why it is needed at all: two adjacent `# Cross-checked:` lines with no
marker read as corroboration. If they actually disagreed, the
annotation is stronger-looking than the evidence behind it.

**BUILD DEFERRED to the first real disagreement.** No resolution can
exist until a dispatch produces one, and the shape of that first case
should settle the open sub-questions -- whether a resolved dispute
drops out of the action list or keeps reporting every run, and whether
the handle must be closed or merely open. Deciding those now locks a
shape in before anything has been learned. Same reasoning that parked
the batching question on 2026-08-15.

Note: the stale case needs nothing new. L2b already compares the
code's value now against what the checker read then and produces
DRIFTED / CORRECTED / UNCHECKED_MOVE, so a value moving after a check
does not silently turn an old cross-check line into a false
endorsement.

### 3. Truncated citations: explicit continuation marker plus normalization

Neither reviewer's shape as proposed. Fable's asymmetry argument holds
-- over-joining is visible in a human-read document, under-joining is
silent -- but GPT is right that an unlabeled indented comment is
genuinely ambiguous and that building an inference layer into an
anti-inference system is how this class returns.

Three parts, in order:

1. **Normalize the 33 sites.** One-time edit pass, done BEFORE any
   builder change. Prepend a continuation marker to each unmarked
   continuation line. Mechanical -- the tail is the rest of the same
   sentence, so no per-site judgment about which leg it belongs to.
   Re-labelling the tails as `# Ref:` or `# Also:` was rejected for
   exactly that reason: 33 judgments is 33 chances to get one wrong.
   Mercury's tail is neither Ref nor Also; it is the rest of the
   Source sentence.
2. **Builder joins on the marker only.** No indentation inference.
3. **Builder fails loudly** on any unmarked continuation following a
   leg. The current defect is a silent drop; the fix must not be a
   silent join.

Marker character to be settled at build time -- ASCII, and must
collide with nothing existing.

Two checks after the pass, both of which can fail: zero unmarked
continuations remain, and all 45 affected rows re-render whole,
including the eris row that currently ends mid-parenthesis.

---

## Measured: the two annotation passes are disjoint

Checked at the anchor. None of the six Finding A constants has a
wrapping `# Source:` line:

| Constant | Line | Source wraps |
|---|---|---|
| `STREAMER_BELT_RADII` | 195 | no |
| `ROCHE_LIMIT_RADII` | 203 | no |
| `ALFVEN_SURFACE_RADII` | 213 | no |
| `TERMINATION_SHOCK_AU` | 228 | no |
| `HELIOPAUSE_RADII` | 235 | no |
| `PARKER_CLOSEST_RADII` | 277 | no |

The six sit in one tight cluster in `constants_new.py` (195-277); the
33 continuation sites span seven files. Independent edits, either
order, neither complicates the other.

---

## Build package as it now stands

**Ready, no decision outstanding**

- Normalize 33 continuation sites; builder joins on marker; builder
  fails loudly on unmarked continuation. (Blocker 1, 45 of 65 rows.)
- Ordinal context window: excerpt around each claim's offset with the
  number marked. `physical_claims` already recomputes offsets.
  (Blocker 7 -- 26 ordinal rows currently share 8 distinct excerpts,
  and 3 units carry duplicate values that are unanswerable by
  construction.)
- Print the seven verdict tokens in the request, with one line of
  semantics each. (Blocker 8 -- verified absent from the emitted
  file.)

**Waiting on a ruling**

- Shape A swaps for the six Finding A sites.
- Claim typing for `CHROMOSPHERE_RADII` -- introduce measurement /
  derived / design as real types, or exclude the one row from this
  dispatch and defer typing. (Blocker 9.)
- Lazy responder -- Fable's canaries or GPT's removal of
  `Value correct?` and of the shown code value. Deferrable until after
  the pilot; both reviewers confirmed the attack is real and
  undetectable today.

**Deferred by ruling**

- `# Resolved:` grammar -- to the first real disagreement.
- Batching -- to the first dispatch, per 2026-08-15.

**Standing constraint**

Both reviewers independently recommended a small pilot before the full
65, chosen to force every structural branch. GPT's sharper version:
include at least one row that should route to SEND BACK and one to
CONVERSATION, because a run where everything is expected to pass does
not test routing.

---

*Prepared August 16, 2026 with Anthropic's Claude Opus 5. Built on
`a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery.*
