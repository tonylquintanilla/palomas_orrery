## L-214 ledger detail block -- the build, closed

Built on `c214da5074ce51628d3851f975fd8eeba70470da` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 21, 2026 with Anthropic's Claude Opus 5.

Paste the block below onto the END of the existing L-214 detail block,
replacing its current `**Gap:**` line (the one that reads "the BUILD.
Design is settled and nothing is built."). Update the metadata comment
at the top of the block to `status:DONE upd:2026-08-21 section:C`, then
run `ledger_index.py` and let it regenerate the index. Do not
hand-edit the index zone.

---

- **BUILT 2026-08-21, in two patches, both landed and verified against
  the pushed bytes.** `patch_L214_1_vocabulary_registry.py` at
  `dbe50bc9` (nine files, one transaction) and
  `patch_L214_2_scanner_derives.py` at `c214da50` (one file,
  behavior-preserving). Both archived to `documentation/`.
- **What patch 1 changed.** `worksheet_keys.py` gained the label
  registry: `RECORD_LEGS`, `LABEL_TRANSPORT`, and `ANY_LABEL_RE` as a
  generic `# Label:` detector that runs AHEAD of classification.
  `Note` joined `CONTEXT_LEGS`; `Review-note` entered `RECORD_LEGS` as
  the withheld free-form label. `legs_of` now returns a named
  `Legs(cited, context, problems, unmarked, joined, unknown)`, and its
  sixth field is the disposition this item existed to create. Its two
  consumers and its 15 test unpacks moved with it in the same
  transaction. The `Role: devtool` tag went in under Fix In Passing.
- **PADDING IS CHECKED BEFORE THE LABEL PATTERN, and that ordering is
  now load-bearing.** With a generic detector, `#   Highly
  ellipsoidal: 1050x840x537 km` would read as a label called `Highly
  ellipsoidal`. Before L-214 the vocabulary itself prevented that by
  accident. The `PADDED_RE` test is what prevents it now, and the
  reason is written into the code beside it.
- **THE MARKING OBLIGATION WAS 17 LINES AT 9 SITES, NOT 28 AT 10**
  [verified @`e1c64dc9`]. The 2026-08-21 handoff's 28 counted wrapped
  lines under WITHHELD labels. The settled design says a withheld
  label's continuations are withheld with it and are never flagged
  unmarked -- nothing is being dropped from a request the text was
  never entering. Excluding them, and accounting for the moon line
  leaving `Note` for `Review-note` while the two relabelled odd
  spellings joined it, gives 17 at 9. Re-measured with the project's
  own `collect_claims` and `PADDED_RE`; the live builder run after the
  patch joined exactly 17 more continuation lines, at exactly those
  nine sites, with no other site moving.
- **Tony's ruling on packaging, 2026-08-21: two patch scripts.** One
  all-or-nothing transaction for the vocabulary and the corpus
  together, because a signature change with four consumers has no
  valid intermediate state and the admit/mark ordering fails in both
  directions if split. The scanner derivation follows separately
  because it is behavior-preserving.
- **Tony's ruling on the form of `Removed` and `Corrected`,
  2026-08-21: option B.** Register both as withheld free-form record
  labels AND unify the dated spellings at source in the same corpus
  patch, so the date moves into the body (`# Corrected: 2026-08-02 --
  ...`). The argument that decided it: the new report's value is that
  a non-empty run means something, and shipping it on day one already
  listing seven known lines would teach its reader that its contents
  are usually noise. `Removed` had one spelling and no drift;
  `Corrected` had four, and a fifth (`# Corrected 2026-08-20:`)
  appeared the day AFTER the design was settled, which is what made
  the set worth closing rather than watching.
  Eight dated lines were unified across `constants_new.py` and
  `mars_visualization_shells.py` -- all of them in files the patch
  already opened, one more than the seven attached to scored values,
  under Fix In Passing.
- **`# Corrected in Phase B:` in `shell_configs.py` was left alone**
  [verified @`e1c64dc9`]. It is not attached to a scored value, so the
  builder never sees it, and the file was outside the patch. If that
  site is ever scored, the new report names it. The Artifact Bounds
  the Audit.
- **The verification that mattered.** Live builder run against the
  pushed bytes at `dbe50bc9`: 98 rows, 176 continuation lines joined,
  `0 unrecognised label(s) at 0 site(s)`. The ratchet did not refuse,
  which is what proves all 17 markers landed on the right lines. The
  `Note` under `SOLAR_RADIUS_KM` travels as context where it was
  silently dropped before; the moon's rehomed single-leg comment
  travels nowhere and does not trip the ratchet either. For patch 2,
  old literal patterns and new derived patterns were compared over
  every `.py` file in the tree: 127 cross-check matches, 5 resolved
  matches, zero disagreements. Tier-1 stayed at 292 across both
  patches -- checked against a pre-patch clone, not assumed.
- **The import guard in patch 2 was tested by making it fail.**
  Deriving a pattern from a shared name is decorative unless a rename
  that never reaches the scanner can actually break the import. The
  membership check against `RECORD_LEGS` was probed with a misspelled
  name in a throwaway copy; it raised and named both sides. A Check
  That Cannot Fail Is Not Passing, applied to the patch's own guard.
- **A defect found by the pre-test, not by a check** -- recorded
  because it is the third instance of this shape in this project. The
  first build of patch 1 rewrote the test file's unpack lines by
  matching a list of six literal spellings, counted nine matches,
  compared that against its own expected nine, and passed -- while
  leaving six of the fifteen sites unconverted. The count check was
  built from the same list as the rewrite, so it could not have
  failed. The xvfb-less runtime test caught it when the suite crashed
  on the seventh site. The shipped version matches by pattern and
  asserts the full population of 15, with the reason written in beside
  it.
**Note:** the `Legs` namedtuple is the shape that keeps this from
recurring. A seventh field can be added without breaking any consumer
that reads by attribute; the 15 test unpacks that had to move this
time were positional.
**Ref:** `worksheet_keys.py` (`LABEL_TRANSPORT`, `ANY_LABEL_RE`,
`legs_of`); `worksheet_request_builder.py` (the report in `main()`);
`provenance_scanner.py` (`_record_line_re`);
`documentation/patch_L214_1_vocabulary_registry.py`;
`documentation/patch_L214_2_scanner_derives.py`;
`documentation/L214_MEASUREMENT_20260819.md`;
`documentation/L214_REVIEW_RECONCILIATION_20260819.md`;
L-209 (the row that exposed it); L-203 (the Visibility Convention);
L-195 (the ratchet this preserves); L-219 (patch naming -- both
scripts follow the convention and self-archived).
