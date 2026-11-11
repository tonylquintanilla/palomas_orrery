<!-- Doc-Kind: hand | Each working document's length cap and where its old lines go; the maintenance run's Document caps row reads the table here. -->
# Document caps

Each working document has a cap on its length, and a home for the
lines that leave it. This page is where the caps are written. The
maintenance run's row "Document caps" reads the table below and names
every document over its cap. Tony's rulings of November 10, 2026
(L-522, document caps).

## The three rules

1. Each document in the table has a cap, in lines, and a home: the
   place an old line goes when it leaves. "git only" means the line is
   deleted and git keeps it.
2. A session that adds to a document at its cap moves something out
   first, to that document's home. The session does not choose the
   home.
3. The maintenance run names every document over its cap. Only Tony
   changes a cap's number; a session never raises one.

A handoff, a brief or a design record is written once and has no cap.
A generated document is written by its tool and has none.

## The table

Change a number here and the next run uses it. The run's row is red
when a document is over its cap, when a document in the table is not
found, when a skill under skills/ has no row, or when a row cannot be
read. Each cap was set on November 10, 2026 at the document's size that
day, so nothing could grow from then on; each step of L-522 that
shortens a document lowers its cap to the new size.

| Document | Cap in lines | Where old lines go |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | 1394 | `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` |
| `skills/agentic-pre-test/SKILL.md` | 126 | `documentation/SKILL_HISTORIES.md` |
| `skills/earth-system-pipeline/SKILL.md` | 199 | `documentation/SKILL_HISTORIES.md` |
| `skills/gallery-assembler/SKILL.md` | 307 | `documentation/SKILL_HISTORIES.md` |
| `skills/gallery-cache-builder/SKILL.md` | 944 | `documentation/SKILL_HISTORIES.md` |
| `skills/gallery-pipeline/SKILL.md` | 160 | `documentation/SKILL_HISTORIES.md` |
| `skills/horizons-orbital-mechanics/SKILL.md` | 904 | `documentation/SKILL_HISTORIES.md` |
| `skills/interactive-exhibit/SKILL.md` | 738 | `documentation/SKILL_HISTORIES.md` |
| `skills/ledger-and-session-records/SKILL.md` | 807 | `documentation/SKILL_HISTORIES.md` |
| `skills/orrery-coding-conventions/SKILL.md` | 726 | `documentation/SKILL_HISTORIES.md` |
| `skills/provenance-cross-check/SKILL.md` | 638 | `documentation/SKILL_HISTORIES.md` |
| `skills/provenance-discipline/SKILL.md` | 1512 | `documentation/SKILL_HISTORIES.md` |
| `skills/safe-file-editing/SKILL.md` | 765 | `documentation/SKILL_HISTORIES.md` |
| `documentation/WHERE_WE_ARE.md` | 130 above the marker | git only |
| `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` | 1818 | `documentation/MASTER_PLAN_HISTORY.md` |
| `README.md` | 664 | git only |
| `CLAUDE.md` | 111 | git only |
| `DOCUMENT_CAPS.md` | 58 | git only |
| `LEDGER_CONSOLIDATED.md` | none until step 4 | none until step 4 |

Where We Are's cap counts only the lines above its run-record marker,
the line that begins "--- Your run record below this line". The ledger
gets its cap when step 4 of L-522 gives its closed items a place of
their own; until then the run prints its size and says it has none.
