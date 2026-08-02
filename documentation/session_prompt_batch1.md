# Session Prompt: L-156 Phase 2 Cross-Check Backfill — Batch 1

**Built on `acf32d5ad33f0b14e535e5d0c639eeb8c6e3614c`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Context

You are Claude Opus 4.6, continuing the L-156 Phase 2 cross-check
backfill. Two files are done (mars_visualization_shells.py and
constants_new.py). The process, annotation format, and model roles are
established and encoded in provenance-discipline v1.5 (load it).

The handoff document `handoff_cross_check_backfill.md` (attached)
describes what was accomplished and the four-batch module plan. Read it
before starting.

## Your job this session

**Prepare Batch 1 worksheet prompts.** Five small shell modules, 34
findings total:

| File | Findings |
|------|----------|
| moon_visualization_shells.py | 4 |
| eris_visualization_shells.py | 5 |
| mercury_visualization_shells.py | 7 |
| venus_visualization_shells.py | 8 |
| pluto_visualization_shells.py | 10 |

For each file:
1. Pull it from HEAD
2. Extract the scanner findings (claims with `# Source:` citations)
3. Produce a worksheet prompt in the established format (SHA-anchored,
   includes the source code claims, specifies the job type)

The job type for shell modules is **value verification** (is the number
right?) AND **citation verification** (does the cited source contain
this value?). Mars showed that both matter — the bow shock text was
wrong while the constant was right, and the Hill sphere citation pointed
at a source that doesn't publish the value.

## Format reference

Use the Mars and constants_new.py worksheet prompts as templates. Each
prompt should:
- Open with `Built on <SHA> at <URL>`
- Include the relevant source code sections with claims and citations
- Specify the worksheet table format
- Say "Research against live authoritative sources. Use web search.
  Do NOT answer from training memory."
- Reference provenance-discipline v1.5 for context

## Decisions still needed from Tony

- **Row-per-claim granularity:** Mars used row-per-claim (4 findings
  expanded to 9 rows). Should Batch 1 follow the same convention?
  Ask before building the prompts if this affects the prompt wording.

## What happens after this session

Tony sends each prompt to Claude + GPT independently. Tony uploads both
worksheets. The next orchestration session compares them, produces
convergence reports, and builds patches. Gemini gets targeted prompts
only for items both primaries marked UNVERIFIED.

---

*Session prompt prepared August 2, 2026 by Claude Opus 4.6.*
