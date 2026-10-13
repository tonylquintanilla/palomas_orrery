<!-- Doc-Kind: hand | Brief for the session that changes worksheet_checker.py's compare() for two items at once: L-424 (two words for two cases of a moved value) and L-426 (very small numbers compared as equal). One checker, one session, by the ruling of 2026-10-08. -->
# Brief: the worksheet checker's compare(), L-424 with L-426

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Fable 5.1, in a
coordination session; the build is for an Opus session.

- Type: build brief (zero code). The design is settled; nothing waits
  on Tony except his run.
- Companions: L-424 and L-426's ledger blocks;
  `documentation/HANDOFF_L418_testing_20261009.md` Part 2 (the planted
  faults F7a and F7b, with the checker's lines word for word);
  `documentation/DESIGN_rulings_20261012.md`, ruling 1.
- Why one session: both items open `compare()` and the L2b block of
  `worksheet_checker.py`, and a change to a checker gets its own
  session (ruling of 2026-10-08). Carry both, one patch.

## 0. Before building

- Pull the orrery at HEAD and pin the SHA; this brief was cut at
  c5dff25 and Tony has pushed since.
- Skills this task fires: provenance-cross-check (the two cases are
  defined there; the skill's bullet is updated to match the checker),
  provenance-discipline (fires beside it), safe-file-editing,
  agentic-pre-test, ledger-and-session-records. Confirm each loaded
  version against the manifest at HEAD.

## 1. What is settled

- **L-424.** Tony, 2026-10-12: "I thought we decided this already?" He
  had, on 2026-10-08: the provenance-cross-check skill defines the two
  cases of a moved value separately. The checker follows the skill:
  UNCHECKED_MOVE where the worksheet carries no value verdict (it
  checked only the citation, or the value cell is blank, holds a word
  outside the vocabulary, or holds DERIVED); UNVERIFIED_MOVE where it
  carries a value verdict and that verdict was UNVERIFIED (which the
  checker reads as ABSENT). Today both branches print UNCHECKED_MOVE
  (`worksheet_checker.py`, the L2b block, the `column ==
  'citation-only'` branch and the final `else`).
- **L-426.** Method, not a ruling: `compare()` rounds both values to
  the coarser of their DECIMAL PLACES, so near 1e-11 everything rounds
  to 0 and any two such numbers match. Probe at 1e30953: 1e-11,
  9.9e-11, 6.674e-11 and 2e-7 each MATCH 6.67430e-11. The fix rounds
  to SIGNIFICANT FIGURES, the coarser of the two as written, so 243
  still matches 243.0226 and Mercury's 2439.7 against 2439.4 is still
  the mismatch it is (the docstring's own cautionary case).

## 2. The build

- Add the word UNVERIFIED_MOVE to the L2b verdict table in the
  checker's comment block and in `dispose`'s routing: routed to
  CONVERSATION, like UNCHECKED_MOVE. The line names the case in words,
  as the no-value-verdict line already does.
- Rewrite `compare()`'s rounding on significant figures. Keep the
  asymmetry it documents: exact equality first, then the coarser
  precision of the two as written. `displayed_precision` and
  `float_precision` change meaning (places to figures) or get
  siblings; the builder's call, said in the handoff.
- Tests in `test_worksheet_checker.py`, planted first and shown caught:
  - the probe values above report MISMATCH against 6.67430e-11, and
    6.67430e-11 still matches 6.6743e-11;
  - 243 matches 243.0226; 2439.7 against 2439.4 is MISMATCH;
  - a moved value on a citation-only worksheet prints UNCHECKED_MOVE;
  - a moved value whose worksheet verdict was UNVERIFIED prints
    UNVERIFIED_MOVE;
  - the summary counts the two words apart.
- The skill: provenance-cross-check's UNCHECKED_MOVE bullet now
  describes two words, not one word with two cases. One version, with
  the protocol entry and the manifest run in the same commit (the four
  steps, One Session, One Bump).
- WORKSHEET_CHECK.md regenerates on the maintenance run; its summary
  line, and the run's, name the two words.
- Docstring stamps; L-424 and L-426 close, each naming the other and
  this brief.

## 3. Tony's actions, all of them

- (do) Start the Opus session from this brief, when it comes in your
  order; nothing to decide in it.
- (do) Run the patch and the maintenance run; read the worksheet
  checker's line; push.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
