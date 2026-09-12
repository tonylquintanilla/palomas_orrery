# L-321 slice 1 -- worksheet prompts, revision 2

Built on orrery `a4ead59ac3f3f390710c99c4e3687d60b444447c`
at https://github.com/tonylquintanilla/palomas_orrery

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-12
Type: DISCOVERY for L-321 (zero code). **Supersedes** the three prompts in
`L321_slice1_magnetosphere_strings_20260911.md`; that file's enumeration
of the six strings still stands and is not repeated here.

## What changed from revision 1, and why

**1. A wrong statement to the checkers is removed.** Revision 1's prompt 3
told the checkers that the inner belt figures are consistent -- "1,000 to
6,000 km altitude against 1.1 to 2 R_E". Converted at the store's
`EARTH_EQUATORIAL_RADIUS_KM` of 6,378.1 km, 1.1 Earth radii from centre is
638 km altitude, not 1,000. The inner belt's two strings differ by about
360 km at the low end. Revision 1 compared the two without converting
between them, which is the same omission the strings themselves make.

**2. Both belts now carry the conversion on the prompt**, so no checker
has to do it and no checker can skip it.

**3. Two rows about retired claims are gone.** The pending L-305 item 4
patch deletes the sentence "Drawn at the midpoint of the 11-14 R_E
measured under normal solar wind (Lugaz et al. 2016)" from the bow shock
hover and moves that hover's standoff attribution from Lugaz to Jelinek.
A checker verifying a sentence that is being deleted spends its time on
nothing. The Lugaz range survives as corroboration in the store's own
Note and is rowed as such.

**4. Line numbers are gone; the text is pasted.** Revision 1 quoted lines
at `1fa413d9`, which has moved twice since. The strings are short. Paste
them.

## Sequencing

These prompts describe the strings AFTER the L-305 item 4 patch runs.
Send them once that patch is pushed, and put the new SHA in the header
below. Every claim rowed here survives that patch; nothing rowed here is
one it removes.

## Common header, prepended to each prompt

> Built on `<SHA of the push carrying patch_L305_magnetosphere_constants.py>`
> at https://github.com/tonylquintanilla/palomas_orrery. Read
> `PROJECT_INSTRUCTIONS.md` (Fetched vs Recalled Convention) and
> `skills/provenance-discipline/SKILL.md` (The Access Standard, Worksheet
> Types) at that SHA before starting; in your reply, state which of those
> two files you read. The author of this code is not a professional
> programmer; the code's polish is the product of AI collaboration and
> says nothing about the author's fluency. Write for a retired civil
> engineer.
>
> Job: CITATION VERIFICATION. For each claim, go to the source the string
> names and confirm the source states it at the stated precision. Then,
> separately, check the value itself against an accessible primary source
> of your own choosing. A source you cannot open without a login FAILS;
> say so. Record the URL you actually opened for every source, and one
> access word: OPEN (full text), ABSTRACT, SNIPPET, WALLED.
>
> Return ONE table, this schema, one row per claim:
>
> | # | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
>
> Verdict cells carry exactly one token. Value correct?: YES NO APPROX
> UNVERIFIED. Citation correct?: YES NO PARTIAL DERIVED UNSOURCED
> UNVERIFIED. Reasoning goes in Notes, nowhere else. Where the source
> states a figure in a different unit or reference frame than the code,
> put the source's own unit in the Source unit column and the conversion
> in Notes. Do not rewrite the strings; that is not this job.

## Prompt 1 -- Magnetopause and magnetotail

Paste `earth_magnetosphere_info` from `earth_visualization_shells.py`,
`magnetosphere_text` from the same file, and the `magnetosphere.tooltip`
block from `shell_configs.py`.

Claims to row:

1. Earth's magnetosphere extends about [store value] Earth radii on the
   Sun-facing side.
2. It stretches into a long magnetotail on the night side.
3. It protects Earth from solar radiation.
4. It protects Earth from cosmic rays.
5. ...making complex life possible.
6. Citation row: Shue et al. (1998), J. Geophys. Res. 103:17691,
   doi:10.1029/98JA01103 supports the magnetopause standoff.

Note for the checker: row 6 is a citation row. The standoff number itself
is checked on its own store row and is out of scope here. On row 5 --
verdict it as stated; do not soften it into something defensible.

**Additional, and it is the point of this prompt.** The magnetotail is
asserted in prose with no figure. An independent extent is wanted:

7. How far downstream has Earth's magnetotail been observed, and by what
   measurement? Give the figure, its uncertainty or range, its reference
   frame (Earth radii from centre, unless the source says otherwise), and
   whether the observation is of a coherent tail or of a signature. We
   hold Ness, Scearce and Cantarano (1967), J. Geophys. Res. 72:3769,
   doi:10.1029/JZ072i015p03769 -- a Pioneer 7 crossing at 900 to 1,050
   Earth radii, whose title says "probable" and whose abstract reports no
   coherent tail with a neutral sheet at that distance. Verify that, and
   say whether a later open source restates it or supersedes it.

## Prompt 2 -- Bow shock

Paste `bow_shock_text` from `earth_visualization_shells.py` and the bow
shock paragraph of `earth_magnetosphere_info`.

Claims to row:

1. The bow shock is the boundary where the supersonic solar wind is first
   slowed by Earth's magnetic field.
2. It is typically located about [store value] Earth radii upstream on the
   Sun-facing side.
3. Citation row: Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res.
   117:A05208, doi:10.1029/2011JA017252 supports the bow shock standoff.
4. Corroboration row: Lugaz et al. (2016), Nat. Commun. 7:13001,
   doi:10.1038/ncomms13001 states that under normal solar wind the bow
   shock forms at a subsolar distance of 11 to 14 Earth radii.

Note for the checker: row 4 is not the source of the drawn value and is
not claimed to be. It is checked because the store keeps it as a
corroborating range, and we want to know whether Lugaz states that range
and in what frame.

## Prompt 3 -- Van Allen belts

Paste `belt_texts` from `earth_visualization_shells.py` and the belt
paragraphs of `earth_magnetosphere_info` and of the `shell_configs.py`
tooltip.

Claims to row:

1. The inner belt holds mainly protons.
2. The inner belt is drawn at its flux peak, [store value] Earth radii
   from centre.
3. The inner belt spans roughly 1.1 to 2 Earth radii from centre.
4. The inner belt extends from about 1,000 km to 6,000 km above Earth's
   surface.
5. Citation row: Baker et al. (2018), Space Sci. Rev. 214:17,
   doi:10.1007/s11214-017-0452-7 supports rows 2 and 3.
6. The outer belt holds mainly electrons.
7. The outer belt is drawn at its flux peak, [store value] Earth radii
   from centre.
8. The outer belt spans roughly 3 to 7 Earth radii from centre.
9. The outer belt extends from about 13,000 km to 60,000 km above Earth's
   surface.
10. The outer belt moves with geomagnetic activity.
11. Citation row: J. Geophys. Res. Space Physics (2025),
    doi:10.1029/2024JA033504 supports row 7.

**Note for the checker, and please read it before starting.** Rows 3 and
4 describe the same inner belt in two reference frames, and so do rows 8
and 9 for the outer belt. The two frames are Earth radii from CENTRE and
kilometres of ALTITUDE above the surface, and they differ by one Earth
radius. At Earth's equatorial radius of 6,378.1 km these convert as:

| Row | As written | Converted |
|---|---|---|
| 3 | 1.1 to 2 radii from centre | 638 to 6,378 km altitude |
| 4 | 1,000 to 6,000 km altitude | 1.16 to 1.94 radii from centre |
| 8 | 3 to 7 radii from centre | 12,756 to 38,269 km altitude |
| 9 | 13,000 to 60,000 km altitude | 3.04 to 10.41 radii from centre |

**Both pairs disagree.** The inner belt differs by about 360 km at the
low end. The outer belt agrees at the low end within rounding and differs
by a factor of about 1.5 at the high end. Do NOT reconcile them and do
not assume one is a rounding of the other -- verdict each row on its own
against a source, state the frame your source uses in the Source unit
column, and let the disagreement stand in the table. Deciding which
survives is our job, not yours.

## Scope, unchanged from revision 1

Tony, 2026-09-11: the belts are in slice 1. Strings A and B carry belt
claims, checking a string means checking all of it, and the belt hovers
are the twins of those claims. All three prompts run in one round,
competitive pattern -- each prompt to two checkers independently, the two
worksheets compared.

Written September 2026 with Anthropic's Claude Opus 5.
