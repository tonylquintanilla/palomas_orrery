# L-321 slice 1 -- Earth's magnetosphere strings, enumerated, with worksheet prompts

Built on orrery `1fa413d95e3017debe4d78a6e1fd3d62038c2cb8`
at https://github.com/tonylquintanilla/palomas_orrery (files read live
2026-09-11: earth_visualization_shells.py, shell_configs.py,
palomas_orrery.py, PROVENANCE_AUDIT.md). Line numbers are at that SHA.

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-11
Type: DISCOVERY for L-321 (zero code). Enumerates; fixes nothing.
Skills loaded: provenance-discipline 2.11 (matches manifest).
Companion: L321_design_round_20260911.md, same session.

## The six strings

Slice as ruled: magnetopause, bow shock, magnetotail. The belt claims
ride inside two of these strings and cannot be split out, so the belts'
own two strings are listed too (see the scope question at the end).

| # | Where | Lines | Reaches the visitor as | Claims |
|---|-------|-------|------------------------|--------|
| A | `earth_visualization_shells.py` `earth_magnetosphere_info` | 726-741 | GUI checkbox tooltip (`palomas_orrery.py:9203`) | standoff (store); "long magnetotail"; protects from solar radiation and cosmic rays; "making complex life possible"; bow shock definition; bow shock standoff (store); inner belt mainly protons, 1,000-6,000 km altitude; outer belt mainly electrons, 13,000-60,000 km altitude |
| B | `shell_configs.py` Earth `magnetosphere.tooltip` | ~2290-2305 | GUI tooltip | same as A, belt lines rewritten to flux peaks (store) |
| C | `earth_visualization_shells.py` `magnetosphere_text` | 791-796 | plot hover, info marker | standoff (store); "long magnetotail"; protects from solar radiation and cosmic rays; "making complex life possible". Source line: Shue et al. 1998; Lugaz et al. 2016 |
| D | `earth_visualization_shells.py` `bow_shock_text` | 845-851 | plot hover, info marker | definition; standoff (store); "midpoint of the 11-14 R_E measured under normal solar wind (Lugaz et al. 2016)"; axis note (a drawing statement, not a claim). Source line: Lugaz 2016 |
| E | `earth_visualization_shells.py` `belt_texts[0]` | 884-887 | plot hover, info marker | inner belt mainly protons; drawn at flux peak (store); spans 1.1-2 R_E from centre. Source: Baker et al. 2018 |
| F | `earth_visualization_shells.py` `belt_texts[1]` | 888-891 | plot hover, info marker | outer belt mainly electrons; drawn at flux peak (store); spans 3-7 R_E; moves with geomagnetic activity. Source: JGR Space Physics 2025 doi:10.1029/2024JA033504; Baker 2018 |

A and B are a pair (tooltip in two homes). C and D are the strings
L-305 rewrites. E and F are belt strings in the same builder.

Store values referenced (not claims of these strings; they are checked
on their own rows): `EARTH_MAGNETOPAUSE_STANDOFF_RADII`,
`EARTH_BOW_SHOCK_STANDOFF_RADII`, `EARTH_VAN_ALLEN_INNER_RADII`,
`EARTH_VAN_ALLEN_OUTER_RADII`.

## Two findings from the enumeration

**1. Two of the six are not in the audit.** `PROVENANCE_AUDIT.md`'s
section for `earth_visualization_shells.py` lists lines 727 and 734
(string A) and 885 and 889 (E and F). It does not list 791 (C) or 845
(D). Both are public-facing hovers with a Source line, and the audit
was cut at `b2c77350`, whose line numbers match these within a few
lines. The likely cause is the list-of-concatenated-strings form both
use (`name = ["...<br><br>" f"..." "..."]`), which the belt strings
also use but inside a two-element list. Not diagnosed here. This is
A Check That Cannot Fail: the audit's Earth count (22 strings) was read
as the denominator and it is short by at least two. Disposition: one
class row for the scanner (strings the scanner does not see), and the
slice uses THIS enumeration, not the audit's, as its denominator.

**2. A and B disagree with E and F on the outer belt.** A says the
outer belt extends "13,000 km to 60,000 km above Earth's surface";
60,000 km altitude is 10.4 R_E from centre. F says the belt spans 3-7
R_E from centre (about 12,700-38,000 km altitude). Same belt, two
figures, both cited, in strings a visitor can see one after the other.
The inner belt figures are consistent (1,000-6,000 km altitude against
1.1-2 R_E). The worksheet decides which survives; the pattern is the
one Verify Execution names -- the hover asserted one size while the
store held another.

Also noted: A's `# Verified: April 2026 via Gemini fact-check` is the
retired stamp form the skill names. It records that a model agreed,
not what was opened. The `# Source:` above it names agencies without
documents. Both clear or fail with the worksheet.

## The claim that will not source as written

"making complex life possible" (A, B, C). A sourceable form exists --
that the magnetosphere deflects most solar wind and shields the
atmosphere from erosion -- but the causal step to complex life is a
popular-science phrasing, and the checker is likely to return
UNSOURCED on it. Per the design round: the sentence goes, the shape
stays, and the string says what the magnetosphere does, not what it
makes possible. Flagged now so the verdict is not a surprise.

## Three worksheet prompts

One per shell. Citation-verification type, competitive pattern: send
each prompt to two checkers independently, compare the worksheets. Each
prompt is paste-ready below the rule. The relay anchor names the rule
files the task fires and asks for a read-back (L-290).

Common header, prepended to each prompt:

> Built on `1fa413d95e3017debe4d78a6e1fd3d62038c2cb8` at
> https://github.com/tonylquintanilla/palomas_orrery. Read
> `PROJECT_INSTRUCTIONS.md` (Fetched vs Recalled Convention) and
> `skills/provenance-discipline/SKILL.md` (The Access Standard, Worksheet
> Types) at that SHA before starting; in your reply, state which of
> those two files you read. The author of this code is not a
> professional programmer; the code's polish is the product of AI
> collaboration and says nothing about the author's fluency. Write for
> a retired civil engineer.
>
> Job: CITATION VERIFICATION. For each claim, go to the source the
> string names and confirm the source states it at the stated
> precision. Then, separately, check the value itself against an
> accessible primary source of your own choosing. A source you cannot
> open without a login FAILS; say so. Record the URL you actually
> opened for every source, and one access word: OPEN (full text),
> ABSTRACT, SNIPPET, WALLED.
>
> Return ONE table, this schema, one row per claim:
>
> | # | Claim | Code value | Your value | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
>
> Verdict cells carry exactly one token. Value correct?: YES NO APPROX
> UNVERIFIED. Citation correct?: YES NO PARTIAL DERIVED UNSOURCED
> UNVERIFIED. Reasoning goes in Notes, nowhere else. Do not rewrite the
> strings; that is not this job.

**Prompt 1 -- Magnetopause and magnetotail (strings A, B, C).**
Paste lines 726-741 and 791-796 of `earth_visualization_shells.py` and
the `magnetosphere.tooltip` block from `shell_configs.py`. Claims to
row: (1) Earth's magnetosphere extends about [store value] R_E on the
Sun-facing side; (2) stretches into a long magnetotail on the night
side; (3) protects Earth from solar radiation; (4) protects Earth from
cosmic rays; (5) making complex life possible; (6) Source line
attribution: Shue et al. (1998) J. Geophys. Res. 103:17691 supports
the standoff; (7) Lugaz et al. (2016) Nat. Commun. 7:13001 supports the
standoff. Note for the checker: (6) and (7) are citation rows; the
standoff number itself is checked on its store row and is out of scope
here.

**Prompt 2 -- Bow shock (string D, and the bow shock lines of A, B).**
Paste lines 845-851 and the bow shock paragraph of 726-741. Claims to
row: (1) the bow shock is the boundary where the supersonic solar wind
is first slowed by Earth's magnetic field; (2) typically located about
[store value] R_E upstream on the Sun-facing side; (3) measured
11-14 R_E under normal solar wind, per Lugaz et al. (2016); (4) Lugaz
2016 doi:10.1038/ncomms13001 is the source of (3). Note for the
checker: L-305 has already ruled the "midpoint" derivation out; row (3)
still needs its verdict so the record shows why.

**Prompt 3 -- Van Allen belts (strings E, F, and the belt lines of A,
B).** Paste lines 884-891 and the belt paragraphs of 726-741. Claims to
row: (1) inner belt is mainly protons; (2) inner belt spans roughly
1.1-2 R_E from centre; (3) inner belt extends 1,000-6,000 km altitude;
(4) Baker et al. (2018) Space Sci. Rev. 214:17
doi:10.1007/s11214-017-0452-7 supports (2) and the flux peak; (5) outer
belt is mainly electrons; (6) outer belt spans roughly 3-7 R_E from
centre; (7) outer belt extends 13,000-60,000 km altitude; (8) the belt
moves with geomagnetic activity; (9) doi:10.1029/2024JA033504 (JGR
Space Physics 2025) supports the outer flux peak. Note for the
checker: (3) and (7) come from one string and (2) and (6) from another,
and (6) and (7) disagree; do not reconcile them, verdict each.

## Scope, ruled

Tony, 2026-09-11: the belts are in slice 1. Strings A and B carry belt
claims, checking a string means checking all of it, and E and F are
the twins of those claims. All three prompts run in one round.

Written September 2026 with Anthropic's Claude Fable 5.1.
