# Findings: Document-Layer Claim Audit

**Built on `df7ca50f1730a40717c9f0fc22138465a5c4cef1`
at https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery repo pinned at `d5437f08f94feccd70b697729b52cdc44df8b51d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs matched these SHAs at audit time, verified by `git ls-remote`.**

**Prepared August 11, 2026 by Claude Fable 5 for Tony Quintanilla,
integrator.** Method: shallow clone at the anchor SHA; every count below
was measured against the cloned bytes, and each finding's "check" column
states how. The project's own validators were also run: `ledger_index.py
--check` (186 blocks, clean), `skills_index.py` (manifest matches all ten
skills exactly), and `provenance_scanner.py` (on a throwaway copy).

---

## Sorting, before the table

Two findings change what you do next: **F1** (the push gate two of your
three stores describe is not the gate you ratified) and **F2** (the
ledger's version-history appendix, the declared change log, is missing
the last three protocol versions). Everything else is a correction --
including four that you already ruled on and recorded in the summary's
CORRECTIONS TO CARRY section but that were never applied to the ledger.

Of the nine instances the review request listed as on record: #9 is
confirmed live (F2 below). #7 (the carried-forward oddity) and #8 (the
verbatim lessons list) are repaired at this SHA -- the ledger's preserved
list now matches the v3.29 protocol's list byte-for-byte, 27 bullets,
verified by diff. The rest lived in handoffs, which are out of scope.

---

## Findings

| # | Verdict | Location | The claim | The check | The reality | Weight |
|---|---|---|---|---|---|---|
| F1 | STALE | `skills/provenance-discipline/SKILL.md` line 53; `PROJECT_INSTRUCTIONS.md` line 385 (manifest row) | "Tier-1 = 0 before any GitHub push" | Compared against the ratification recorded in ledger L-184 and the master plan (line 1816) | You ratified on 2026-08-05 that the gate for this phase is "Tier-1 = 0 **on the interactive build path**." The skill and the protocol manifest row still state the global gate, and the skill never mentions the phase-scoped one. A fresh session reading protocol-then-skill enforces the wrong gate. The skill's line sits under "The Goal State," so part of this is wording -- the global gate may survive as the long-run goal -- but the current gate is absent from the store that teaches it. | **Changes what you do.** Decision on wording, not just a fix. |
| F2 | FALSE | `PROJECT_INSTRUCTIONS.md` line 819 | "The full version history (v1.0 through current) lives in LEDGER_CONSOLIDATED.md, Protocol Version History appendix" | Grepped all 6,746 ledger lines for `v3.35`, `v3.36`, `v3.37`: zero matches. Read the appendix end: last entry is v3.34, at line 6714. | The appendix covers v1.0 through v3.34. The last three protocol versions have no entry in the declared change log. This is the phantom-backup subtype: the pointer is confident and the thing pointed at is partial. | **Changes what you do.** The change log has a three-version hole. |
| F3 | FALSE | `LEDGER_CONSOLIDATED.md` lines 1065--1066 (and the "7 derived" echo at 1071) | "7 of 45 top-level assignments are derived rather than literal" | Parsed `constants_new.py` with Python's `ast` module (a parser that reads code structure without running it): 49 top-level assignments. | 49 top-level, not 45. Your own recorded correction (summary, CORRECTIONS TO CARRY) says 49 with 6 derived. The correction was recorded but never applied here. | Correction, already ruled. |
| F4 | FALSE | `LEDGER_CONSOLIDATED.md` line 927 | "126 dead `tooltip` fields (83 sphere + 41 custom)" | AST count of `'tooltip'` dictionary keys in `shell_configs.py`: 124 total -- 83 in SHELL_CONFIGS, 41 in CUSTOM_SHELLS. Raw text grep gives 126 because one docstring mention and one comment also match. | 124. The bullet contradicts its own breakdown: 83 + 41 = 124. | Correction, already ruled. |
| F5 | FALSE | `LEDGER_CONSOLIDATED.md` line 1045 | "decide on the 126 dead tooltip fields" | Same AST count as F4. | 124. | Correction, already ruled. |
| F6 | FALSE | `LEDGER_CONSOLIDATED.md` lines 1591--1592 | "the `'tooltip'` key in `shell_configs.py` is defined **126 times** and read by nothing ... updating the count" | Same AST count as F4. | Defined 124 times. The 126 is raw text matches, two of which are documentation, not definitions. This is the bullet that took the corrected 124 and "updated" it back to 126 on the strength of a raw grep -- the same measurement error the summary's correction note explains. | Correction. |
| F7 | FALSE | `documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` lines 407--408 | "Two sites in the ledger carry 126" | Grepped the ledger for the figure and read each hit in context. | Three live sites carry it: lines 927, 1045, and 1592. (A fourth, line 5360, sits inside a completed-batch historical record and is correctly left alone -- correcting it would falsify the record.) | Correction: the correction note itself undercounts. |
| F8 | STALE | `MODULE_ATLAS.md` lines 4 and 8; `MODULE_INDEX.md` (whole table) | "Modules: 116 \| Functions: 1021 \| Lines: 94,615" and "All 116 modules declare a valid Role:" | Counted root `*.py` files (117) and diffed that list against the index's module rows. | One module, `test_cross_checked.py` (the L-156 Phase 2 regression tests, added after the August 1 generation), is in the repo but not in either generated document. It declares `Role: devtool`, so a rerun of `module_atlas.py` picks it up cleanly. | Correction: rerun `module_atlas.py`. |
| F9 | STALE | `PROVENANCE_AUDIT.md` lines 3--6 | "Generated: August 10, 2026 / Files scanned: 119 / Total findings: 880 / ... Dicts: 39" | Ran `provenance_scanner.py` on a throwaway clone at this exact SHA. | The scanner at this commit reports 117 files, 879 findings, 38 dicts. The committed audit describes the codebase as it stood a day and two files earlier, not the code it sits beside. (The run also printed 206 Tier-1 findings with the per-domain split -- consistent with the 206 recorded in L-184; no live document claims Tier-1 is currently zero, so that is not a finding.) | Correction: regenerate at the commit. |
| F10 | FALSE | `DATA_INVENTORY.md` lines 1 and 3 | "(local, gitignored -- CURRENT state)" and "Repo copies stale/absent" | Grepped `.gitignore` (no entry; grep exit code 1) and ran `git ls-files DATA_INVENTORY.md` (tracked). | The file is committed to the repo and is not in `.gitignore`. The tracked copy asserts it is not in the repo. | Decision: either actually gitignore it or reword the header. |
| F11 | FALSE | `PROJECT_INSTRUCTIONS.md` lines 19 and 614 | "see documentation/PROJECT_ORIGIN.md" | Listed both paths. | The file exists at the repo root as `PROJECT_ORIGIN.md`. `documentation/PROJECT_ORIGIN.md` does not exist. Both protocol pointers fail to resolve. | Decision: fix the two pointers or move the file. |
| F12 | STALE | `LEDGER_CONSOLIDATED.md` line 148 | "the next new item is L-062" | Read the index: highest handle is L-191. | The next new item is L-192. The sentence was true once and has been false for 130 handles. | Correction: reword without a number, or have `ledger_index.py` maintain it. |
| F13 | STALE | `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` lines 57--58 | "current HEAD orrery `ee0da47c` / gallery `61a78c00`" | Compared to live HEADs. | Current HEADs are `df7ca50f` and `d5437f08`. The "built on" anchors elsewhere in the same document are the durable form -- they stay true forever. "Current HEAD is X" goes false on the next push by construction. | Wording decision, low weight. |
| F14 | STALE | `README.md` lines 175 and 331 | "~121 Python modules" / "121 Python modules and roughly 92,000 non-blank lines as of July 2026" | Counted: 117 root modules, 95,653 non-blank lines today. | Off by four modules against the current tree. Line 331 dates itself to July and explicitly defers to MODULE_ATLAS.md as authoritative, which softens it; line 175 carries no date. | Correction, low weight. |

## Unverifiable

| Verdict | Location | The claim | What would settle it |
|---|---|---|---|
| UNVERIFIABLE | `DATA_INVENTORY.md`, whole document | That the inventory reflects "CURRENT state" of the local data stores | The data directories it describes are gitignored, so nothing in the repo can confirm or refute the tables. Rerunning the inventory tool on your machine settles it. |
| UNVERIFIABLE | `README.md` line 331 | That the module count was 121 in July 2026 | A shallow clone has no history. Deepening the clone and counting `*.py` at a July commit settles it. The atlas reported 116 on August 1, so either five modules were deleted in late July or the figure was never right -- I could not tell which. |

---

## Second output: what a tool could check, and what needs a person

The boundary falls on where the ground truth lives. When a claim's ground
truth is bytes in the same repo at the same SHA, a tool can check it:
counts (modules, lines, dictionary keys via `ast`), pointer resolution
(file paths, L-handles, section names), store agreement (the three-way
skill version check, of which `skills_index.py` already covers two legs),
generated-document freshness (does rerunning the generator at this commit
reproduce the committed file -- F8 and F9 are both this one check), and
contradiction patterns (a tracked file claiming to be gitignored, a
"current HEAD" phrase anywhere, a stated total disagreeing with its own
stated breakdown in the same sentence -- F4 is mechanically detectable as
126 != 83+41). Eleven of the fourteen findings above are in that class,
and notably your three existing index tools already ARE this checker for
their own zones; every finding here lives in prose those tools do not
read. The hard part a tool cannot do reliably is knowing which sentences
make claims: extracting "126 dead tooltip fields" as an assertion to test
is the human-shaped step. A workable middle is registration -- a claim
that matters gets a small machine-readable line (what to run, what to
expect) next to the prose, and the checker reruns the registered set;
unregistered prose stays a discipline. What genuinely requires a person:
status claims whose authority is a conversation ("ratified," "Tony's
ruling") -- F1 could only be caught by reading the ruling and the skill
side by side; scope judgments (whether line 5360 is a historical record
or a live claim -- a tool would have "corrected" it and falsified the
record); and any claim whose truth is a decision rather than a
measurement.

---

## Outside scope, noticed anyway

- `documentation/LESSONS_ARCHIVE.md` says the working copy at trim time
  was 824 lines; the protocol's v3.37 entry says trimmed from 882 (the
  archived v3.36 is exactly 882). Both may be true at different moments
  of the same day's reversed first cut, but the two numbers sit
  unreconciled.

---

## Constraint 1, honored recursively

One of my own checks was wrong before it was right: my first L-handle
resolution pass flagged L-014, L-016, L-026, L-046, and L-084 as
unresolved, because my pattern missed the legacy-alias block format
(`#### [L-016 | #6]`). Rechecking against the actual format, every
handle referenced in every in-scope document resolves. The failure was in
my regex, not your ledger -- reported here because an auditor's false
positive left unmentioned becomes someone else's finding #10.

*Prepared August 11, 2026 with Anthropic's Claude Fable 5, built on
`df7ca50f1730a40717c9f0fc22138465a5c4cef1` at
https://github.com/tonylquintanilla/palomas_orrery and
`d5437f08f94feccd70b697729b52cdc44df8b51d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
