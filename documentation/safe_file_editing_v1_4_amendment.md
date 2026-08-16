# safe-file-editing v1.3 -> v1.4 -- proposed amendment

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Two changes, both to the **Encoding Gate** section. The rest of the
skill is unchanged.

---

## 1. Replace the Encoding Gate section body

Current text ends at the two shell commands. Append this:

> ### Fix In Passing, Report It [QUALITY]
>
> When a patch is already fingerprinting a file and finds a violation
> of an ALREADY-RULED convention in it -- non-ASCII bytes, CRLF where
> the repo is LF -- fix it in the same patch and say so in the output.
> Do not note it and move on.
>
> The reasoning is about what actually gets scheduled. A dedicated
> sweep for two characters is costly and low priority, so "recorded
> for later" means never. Meanwhile the patch already holds the two
> things that make the fix safe: a fingerprint proving the file is the
> expected one, and an all-or-nothing harness. Those conditions will
> not recur more cheaply than right now.
>
> This is NOT a licence for scope creep. It applies only where all
> three hold:
> - the convention is already ruled, not a judgment call being made
>   on the spot;
> - the file is already being edited by this patch, not opened for
>   the purpose;
> - the fix is mechanical, with no reading of intent.
>
> A design change, a refactor, or anything needing a decision stays
> out of scope and goes to the person. "Fix only what asked" governs
> DESIGN. It was never meant to preserve a ruled violation in a file
> you are already holding open.
>
> **Scope the gate to what the patch INTRODUCES, then sweep what it
> can reach.** A gate that fails the whole run because the file
> already held a violation blocks a correct patch over somebody
> else's bug. A gate that stays silent about it is how a convention
> quietly stops being true. So: hard-fail on non-ASCII in inserted
> lines, fix pre-existing violations where the three conditions hold,
> and print which of the two happened.
>
> Report both outcomes explicitly, because they are different facts:
>
> ```
> note: palomas_orrery_helpers.py had 6 non-ASCII byte(s); normalized
>       to ASCII in passing
> note: <file> still holds N non-ASCII byte(s) this patch did not reach
> ```
>
> The second line is the one that matters. A patch that fixes some
> and not all must say which, or the next session reads a clean run
> as a clean file.
>
> **The patch script's own bytes are also in scope.** A script that
> repairs a Unicode character has to CARRY that character to match
> on it. Write it escaped (`'\u2192'`) so the deliverable stays ASCII
> and does not fail the gate it exists to enforce.

## 2. Add to Field Notes

> - **A pre-existing violation found mid-patch gets fixed, not
>   noted.** A chromosphere patch touching eight files hit its own
>   ASCII gate on two Unicode arrows in a comment that predated the
>   work by months. The first instinct was to report and leave it,
>   citing "fix only what asked." Tony's ruling: the convention was
>   already ruled, the file was already fingerprinted, and a separate
>   sweep for two characters would never be scheduled -- so fix it in
>   passing and report it. The anti-pattern being avoided by "fix
>   only what asked" is unreviewed DESIGN change, not mechanical
>   compliance with a standing rule. (2026-08-16)

---

## Version line

Line 9 of the skill currently reads:

```
Skill version: 1.3 | Cut from palomas_orrery @ 1ba20c3 (v1.3), earlier @
3398970 (v1.2), bdaaa0c (v1.1) | August 7, 2026
```

It becomes 1.4, cut at whatever SHA carries this change, with the
existing lineage kept and one line added to the provenance sentence
noting that v1.4 adds Fix In Passing, Report It.

---

## Handoff obligation this creates

Per the resident protocol's **Stale Skill = Stop**, a mid-session
skill bump cannot be verified from inside the session that made it.
The loaded copy appears bound at conversation start, so a reinstall
lands in the account invisibly and Tony's word that he reinstalled it
is an assertion standing in for a check.

So this does not clear in session. It carries forward as written:

> `safe-file-editing` went to 1.4 at `<SHA>`; the session that bumped
> it loaded 1.3; the next session confirms its loaded copy reads 1.4
> before doing patch-script work.

Three stores to update, in order: `skills/safe-file-editing/SKILL.md`
in the repo, then Settings > Skills to reinstall, then
`skills_index.py` to regenerate the manifest table in
`PROJECT_INSTRUCTIONS.md`.

---

*Prepared August 16, 2026 with Anthropic's Claude Opus 5. Built on
`a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery.*
