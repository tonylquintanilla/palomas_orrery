# Worksheets and Model Roles (provenance-cross-check reference)

Opened from provenance-cross-check before writing a worksheet prompt
or choosing which models to send it to. Moved here from
provenance-discipline 2.26 on 2026-10-08 (L-418), word for word apart
from the two pointer edits provenance-cross-check 1.0 lists. The
annotation format, the exhibit requirement and the send-back rules are
in the skill's SKILL.md.

### Model Roles in the Competitive Pattern

Tested and validated in the Mars and constants_new.py cross-check
sessions (August 2026). These are demonstrated strengths, not
assumptions.

| Model | Demonstrated strength | Use for |
|-------|----------------------|---------|
| Claude (Opus) | Derivations, citation-shape errors (catches when a source cannot contain the claim as written), honest about limitations (marks UNVERIFIED rather than bluffing) | Primary checker: papers, web sources, derivations, structural analysis |
| GPT | Papers with DOIs, explicit derivations with worked math, thorough web sourcing, catches date/year errors in citations | Primary checker: independent of Claude, complementary source selection |
| Gemini | Domain knowledge, structural/philosophical dialogue. Fetching is TIER-DEPENDENT -- see the roster note below. Book content is LEAD GENERATION only -- see the demotion below | Domain review, tiebreaker when primaries diverge |
| Fable | Large-context comprehensive review, far-reaching audits across many files, pattern recognition at scale | Cross-codebase audits, manifest generation, bulk review when scope exceeds a bounded session |

**Default two-leg pattern:** Claude + GPT independently. Covers papers,
web sources, derivations, NASA/JPL data.

**Gemini escalation:** When either primary leg marks items UNVERIFIED
due to book citations, or when Claude and GPT diverge on domain-knowledge
questions. Also effective as a third independent leg when sent the same
prompt (tested: all three models received the same constants_new.py
remaining-items prompt; complementary coverage emerged naturally).

**Fable escalation:** When the scope of review exceeds what a bounded
session can hold -- auditing an entire manifest, reviewing cross-file
consistency, or pattern-matching across the full codebase. Not for
per-claim worksheet work (Opus handles that), but for the architectural
view that requires seeing everything at once.

**Demoted 2026-08-27: Gemini's book access is LEAD GENERATION, not a
clearing route.** This skill previously recorded that Gemini could
"open the books" -- reaching Carroll & Ostlie and Golub & Pasachoff
content neither Claude nor GPT could -- and routed book citations to
it. Under The Access Standard that is a model's ACCOUNT of a book, not
the book. It has the same standing as any other free-form model query:
useful for finding where a claim lives, never citable on its own.

The pilot supports the demotion independently. The Gemini leg returned
a quotation on 1 percent of 92 rows and a locator on 28 percent.

Book citations now route to RE-HOMING first -- find an accessible
authority carrying the same result -- and to Tony's Scholar or Books
queue only when none exists.

**Gemini: the tier decides whether it can check citations at all.**
Flash 3.8 cannot fetch; it declared so and returned a table with every
Source cell WALLED. Pro 3.1 with Extended Thinking fetches -- it opened
three PDFs in full. So the constraint recorded at L-276 is about the
interface and the tier, not about Gemini, and a Flash tier is not a
citation checker at any prompt quality.

**A checker inside the Project is not independent for a rerun.** Once
an instance has transcribed or reviewed a return, it has seen the
answer, and past chats are searchable, so a fresh session in the same
Project does not restore independence. A rerun meant to test search
depth has to go outside the Project or not happen.

### Worksheet Types

Two types, same format, same competitive pattern, different job:

**Value verification:** "Is this number right?" The checker independently
researches each claim against primary sources, without seeing what the
other checker found. Catches wrong values behind correct-looking
citations. Used for shell modules (Mars was the first: bow shock 1.5
should have been 1.64, Hill sphere 324.5 should have been 320).

**Citation verification:** "Does the cited source actually contain this
value?" The checker goes to the stated source and confirms the value
appears there at the stated precision. Catches citations that point at
sources that don't contain the claimed value -- right number, wrong
provenance. Used for constants_new.py (IAU B3 cited for Mars/Saturn/
Uranus/Neptune radii it doesn't define; heliopause arithmetic used 123
AU where the source says 121.6).

Both types use the same worksheet table format:

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Read by | Notes |

**`Read by` names WHO opened the source**, a model by name or Tony, and
it is not optional. A verdict is only as good as the reading behind it,
and the two readings are reached differently: a model reads what its
search tools can open, and Tony reads what only he can (The Read Field,
in provenance-discipline). A worksheet that does not say which happened cannot be turned
into a `# Read:` line without guessing, and guessing there is the
failure that rule exists to prevent. (Promised on 2026-09-11; it did
not ride 2.13.)

**Every row says which job it is.** The two types above describe what a
whole worksheet is FOR; a real worksheet usually needs both, and the
marker is per row:

    [CITATION] -- the string names a source for this claim. Go to that
    source and confirm it states the claim, at the stated precision.
    Then, separately, check the value against an accessible primary
    source of your own choosing.

    [DISCOVERY] -- the string states a figure that may have no source
    at all. Do not assume one exists, and do not reconcile it with any
    other figure in the worksheet. Find whether an accessible source
    states it, say which, and if none does, say that. UNSOURCED is a
    valid and useful answer.

Do not treat a DISCOVERY row as a CITATION row with a missing citation.
They ask different questions, they fail differently, and per Route the
Effort Tier by Job Type, in the skill's SKILL.md, they are not worth
the same effort tier.

`Source unit` is not decoration. The same belt edge reads 1.1 to 2 in
Earth radii and 1,000 to 6,000 in kilometres, and a row that omits the
unit cannot be compared against the code value at all.

**State this schema IN THE PROMPT, with the verdict vocabulary.** Eight
different column layouts exist across the worksheets on disk because no
prompt ever specified one, and a tool that must read them all needs a
header-role registry to do it. That is the consumer paying for a
producer that was never pinned.

A verdict cell carries EXACTLY ONE of these tokens and nothing else,
with the reasoning in Notes. **The tokens are scoped to their column.**

    Value correct?     YES  NO  APPROX  UNVERIFIED
    Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED

Two verdicts per row, never conflated. `Value correct?` asks whether
the number is right; `Citation correct?` asks whether the named source
publishes it. A right number under a wrong authority is value-YES and
citation-NO, and that split is the whole reason for two columns.

**The scoping is the substance, not the formatting.** APPROX qualifies
a VALUE -- the number is right to a stated tolerance. PARTIAL qualifies
a CITATION -- the source supports some of what is claimed. They were
commissioned that way and they are not synonyms; listing all of them on
one flat line lost the distinction, and a checker reading the flat list
cannot tell which word answers which question.

UNSOURCED belongs to the citation column: the named source does not
publish this value at all, as against NO, which is the source
publishing a DIFFERENT value. Both send the row to conversation; the
distinction survives because it changes the repair.

**Vocabulary version.** A worksheet states which vocabulary it was
written against, on its own line near the top:

    Vocabulary: v2 (2026-08-13)

Seventeen worksheets on disk predate any settled vocabulary and carry
no such line. A tool reads the line rather than guessing from a date,
and an absent line means pre-v2 -- which is a fact about the file, not
a defect in it.

`Code value` is what the checker read from the code at the prompt's
SHA. It is not redundant with `Your value`: comparing it against the
code NOW detects a value edited after its check, which no diff-based
tool can see once the edit is committed.

PARTIAL means the claim is genuinely half-right -- a source that
publishes the value at lower precision than the code carries.
A checker that STOPPED BEFORE FINISHING writes UNVERIFIED, and the
Notes say what blocked it: a context limit, a paywalled paper, a
conversation that ended. An honest UNVERIFIED is a usable answer; a
PARTIAL standing in for one is not.

DERIVED answers the CITATION question, not the value question. It
means no source publishes this number because the number is computed,
so there is no citation for that column to be right about. It can
pair with any value verdict, including NO. Reading it as a third
member of the PARTIAL/APPROX family is the error to avoid: those two
qualify a value, DERIVED describes where one came from.

A DERIVED row is COMPLETE when it names its inputs, shows the
arithmetic, and the arithmetic closes. Then L-158 governs: the
derivation logic has cleared its own check, and the value inherits
the rung of its WEAKEST INPUT. That is not a completed check on its
own -- it hands the question to the premise. Worked example, the
Moon's Hill sphere in lunar radii: 60,000 / 1737.4 = 34.53 closes
exactly, and the 60,000 km premise under it reads APPROX and
UNSOURCED, so the derived figure is worth precisely that and no
more. A DERIVED row showing no work is incomplete and goes back.

The distinction matters because the same file can need both: a shell
module's display text needs value verification while its `# Source:`
comments need citation verification.

### Batch Worksheet Workflow

For scaling the competitive pattern across many modules:

1. **Claude prepares worksheet prompts** (one per file, SHA-anchored,
   with the file's claims extracted from the scanner findings).
2. **Tony sends each prompt to Claude + GPT independently.** Multiple
   file prompts can go in one session per model.
3. **Tony uploads both worksheets; Claude compares** and produces the
   convergence/divergence report per file.
4. **Tony decides on divergences.** Unresolved divergences go to Gemini
   or GPT as tiebreaker.
5. **Claude builds a transactional patch** (fixes + annotations) per
   file or per batch.
6. **Gemini gets targeted prompts** only for items both primaries
   marked UNVERIFIED (typically book citations).
7. **Blind source lookup**, when models converge suspiciously or diverge
   in a way that smells like anchoring. Every earlier round shows each
   model the value already in the code, which invites confirming it. So
   run a round with the expected value REMOVED: present the claim text
   only, and ask each model to source it cold. Batch 1 ran 8 items this
   way; 4 reached a primary source and 4 came back honestly unsourced --
   and it is what caught Mercury's sodium tail at 10,000 R_M (observed
   range is ~120 to ~1,400) and re-attributed Eris's 875 K core.
   A "NOT FOUND" from a blind round is a RESULT, not a failed round: it
   is how a claim earns removal rather than a softer citation.
8. **Fable consistency audit**, after the patches land. Full-codebase
   pass checking visualization CONSTANTS against display TEXT, and
   mapping every duplicated value for the single-source-of-truth
   migration (L-181). This catches what the per-claim worksheet
   structurally cannot: the worksheet asks "is this claim right?", never
   "does the geometry still agree with it?" Batch 1 corrected text and
   citations across five modules and left six `radius_fraction` values
   drawing the pre-patch physics. Prompt:
   `documentation/PROMPT_fable_shell_consistency_audit.md`; report:
   `documentation/FABLE_shell_consistency_audit_report.md`.

This keeps Gemini's book-access strength aimed where it matters rather
than diluted across routine web-checkable claims.
