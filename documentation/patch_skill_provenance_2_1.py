"""Patch: provenance-discipline skill 2.0 -> 2.1.

Run command:

    python patch_skill_provenance_2_1.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run. It edits
skills/provenance-discipline/SKILL.md. Transactional: every edit must
find exactly one anchor or nothing is written.

Three follow-up steps AFTER this runs, in order:
  1. Run skills_index.py -- it rewrites the manifest table in
     PROJECT_INSTRUCTIONS.md and prints what the manifest was
     advertising before the overwrite.
  2. Reinstall the skill to your account (Settings > Skills), reading
     the repo file to confirm it says 2.1 before installing.
  3. Commit and push.

The reinstall CANNOT be verified from inside this session -- the skill
copy a conversation loads appears bound when the conversation starts.
That verification defers into the handoff and is discharged by the next
session's load. This is the same limit protocol v3.38 records for the
1.9 and 2.0 bumps.

Success prints one `ok` line per edit, then `patch applied (N bytes)`.
Failure prints a single ERROR or ANCHOR FAIL line and writes nothing.
"""

import hashlib
import os
import sys

TARGET = os.path.join('skills', 'provenance-discipline', 'SKILL.md')


EDITS = [
    # ---- 1. version line ----------------------------------------------
    (b"""Skill version: 2.0 | Cut from palomas_orrery @ eb77c83 (v2.0), earlier
@ cdcdb4b (v1.9), @ 8e4b5ca (v1.8) | August 12, 2026""",
     b"""Skill version: 2.1 | Cut from palomas_orrery @ 00219d9 (v2.1), earlier
@ eb77c83 (v2.0), @ cdcdb4b (v1.9), @ 8e4b5ca (v1.8) | August 13, 2026"""),

    # ---- 2. changelog: v2.0 was never recorded, plus v2.1 -------------
    (b"""carried the retired global gate for a week; caught by Fable's
document-layer claim audit, finding F1, August 11, 2026.
""",
     b"""carried the retired global gate for a week; caught by Fable's
document-layer claim audit, finding F1, August 11, 2026.

v2.0 (August 12, 2026) replaced the annotation grammar: checker first,
optional ` -- <source>` clause, and the retired source-first order now
REFUSED as `legacy_source_first` rather than reconstructed. The old
order was ambiguous by construction -- a source carrying its own
publication year ate the check date, so the model name landed outside
the checker identity and two annotations by two DIFFERENT models read
as one checker written twice. All 134 lines were migrated. The
store-binding check lives in skills_index.py, which asserts that every
annotation example in every SKILL.md parses as the scanner reads it --
placed there because it runs at the moment a skill changes, which is
the moment the drift is introduced.

v2.1 (August 13, 2026) extends Worksheet First, Annotation Second with
two clauses about what the worksheet has to CONTAIN, and specifies the
worksheet table schema and verdict vocabulary at the prompt so the
evidence arrives usable. Earned August 12-13: two annotations in
constants_new.py credited a worksheet for checks it explicitly did not
perform, and one cited worksheet was prose a tool cannot read. Tony's
ruling -- we do not have to accept and interpret incomplete or
malformed answers -- is the second clause, and the session that
produced the evidence can be reopened to finish the job.
"""),

    # ---- 3. the two new clauses ---------------------------------------
    (b"""Do not write the annotation planning to file the worksheet afterwards.
The gap between the two is where the first shape comes from.
""",
     b"""Do not write the annotation planning to file the worksheet afterwards.
The gap between the two is where the first shape comes from.

**The worksheet has to SAY THE THING.** Existence is clause one, not the
whole rule. An annotation names a checker who verified THIS value; the
worksheet must record that check, for that value, with a verdict that
amounts to a completed one.

Two live failures, both found August 13, 2026, and both the same shape:

- `BENNU_RADIUS_KM` -- worksheet row G10 reads UNVERIFIED, "Not
  checked." The annotation credits Claude with a cross-check against
  Nolan et al.
- `ARROKOTH_RADIUS_KM` -- the worksheet said the OLD value was wrong.
  The value was then corrected against Keane et al. 2022, a paper the
  worksheet never opened, and the annotation still credits the
  worksheet.

**A worksheet that says a value is WRONG is not a worksheet that says
the replacement is RIGHT.** Those are different claims resting on
different evidence. The correction is the moment this enters: someone
fixes a value against a new source, and the existing annotation rides
along unchanged. Re-check the annotation whenever the value under it
moves.

**Incomplete or malformed evidence is sent back, not interpreted.**
[Tony's ruling, August 13, 2026.] If a worksheet is prose a tool cannot
read, or its verdict is PARTIAL because the checker ran out of session
rather than because the claim is half-right, the answer is a better
worksheet -- not a cleverer parser and not a charitable reading.

The move that makes this cheap: **reopen the session that produced it.**
Conversations persist and can be continued. The session holds the
research context, so asking it to finish costs a fraction of starting
over, and the addendum lands in the format the tools expect. Measured
the first time this was tried: of seventeen unresolved rows, nine
closed, including one that had blocked on nobody opening the cited fact
sheet.

Ask for a NEW file rather than an edit. The original worksheet is the
record of what was known on its date, and rewriting it makes it assert
something it did not say at the time.
"""),

    # ---- 4. producer half: schema and vocabulary ----------------------
    (b"""Both types use the same worksheet table format:

| # | Claim/Constant | Value | Source | Verified? | Notes |
""",
     b"""Both types use the same worksheet table format:

| # | Claim/Constant | Code value | Your value | Source | Value correct? | Citation correct? | Notes |

**State this schema IN THE PROMPT, with the verdict vocabulary.** Eight
different column layouts exist across the worksheets on disk because no
prompt ever specified one, and a tool that must read them all needs a
header-role registry to do it. That is the consumer paying for a
producer that was never pinned.

A verdict cell carries EXACTLY ONE of these tokens and nothing else,
with the reasoning in Notes:

    YES  NO  PARTIAL  APPROX  DERIVED  UNVERIFIED

Two verdicts per row, never conflated. `Value correct?` asks whether
the number is right; `Citation correct?` asks whether the named source
publishes it. A right number under a wrong authority is value-YES and
citation-NO, and that split is the whole reason for two columns.

`Code value` is what the checker read from the code at the prompt's
SHA. It is not redundant with `Your value`: comparing it against the
code NOW detects a value edited after its check, which no diff-based
tool can see once the edit is committed.

PARTIAL means the claim is genuinely half-right -- a source that
publishes the value at lower precision than the code carries.
"I ran out of session" is UNVERIFIED, and the Notes say what blocked
it. An honest UNVERIFIED is a usable answer; a PARTIAL standing in for
one is not.
"""),

    # ---- 5. the prompt step names the schema --------------------------
    (b"""   being checked, and specifies the job type (see Worksheet Types below).
   Claude does NOT propose corrected values -- only what needs checking.""",
     b"""   being checked, and specifies the job type (see Worksheet Types below).
   The prompt states the table schema and the verdict vocabulary
   explicitly -- an unspecified format is how eight of them happened.
   Claude does NOT propose corrected values -- only what needs checking."""),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print(f"ERROR: {TARGET} not found under this script's folder "
              f"({here}). Save this script in the repo root.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    print(f"base fingerprint: {fp}  ({len(data)} bytes)")

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print("note: file uses CRLF; anchors translated")

    staged = data
    for i, (old, new) in enumerate(EDITS, 1):
        o, n = old, new
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = staged.count(o)
        if count != 1:
            head = o.split(b'\n')[0][:70]
            print(f"ANCHOR FAIL edit {i}: expected 1 match, got {count}: "
                  f"{head!r}")
            print("nothing written")
            return 1
        staged = staged.replace(o, n, 1)
        print(f"ok  edit {i}")

    with open(path, 'wb') as f:
        f.write(staged)

    print(f"patch applied ({len(staged)} bytes)")
    print("")
    print("Next: run skills_index.py, then reinstall the skill to your")
    print("account (Settings > Skills), then commit and push.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
