# L-321 slice 1 -- worksheet prompts, revision 3

Built on orrery `f1bceefd05eeee0cac38fd519dd207314acb2383`
at https://github.com/tonylquintanilla/palomas_orrery

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-12
Type: DISCOVERY for L-321 (zero code).
**Supersedes** `L321_slice1_prompts_rev2_20260912.md`. Revision 1's
enumeration of the six strings still stands and is not repeated here.

**Anchor moved forward 2026-09-13**, from `62ee5149` to the SHA above.
No prompt text changed. The reason is the store, not the strings: the
three files these prompts quote are byte-identical between those two
commits, and `constants_new.py` is not. L-325 (`c0bb91a0`) replaced the
magnetopause row's sixteen-digit literal with 10.25 and the bow shock
row's expression with 13.51. Four claim rows below carry `[store value]`
and the strings interpolate their constants, so a checker resolving them
at the old anchor would have read back the form that ruling retired. The
rendered figure is the same either way -- `:.4g` prints 10.25 and 13.51
from both forms -- so what moved is what a checker reads out of the
store, not what a visitor sees.

These are ready to send. Revision 2's one blocking dependency is
discharged, and every string below was read at the SHA in the header,
not recalled.

## What changed from revision 2, and why

**1. The sequencing dependency is discharged.** Revision 2 said it
described the strings AFTER the L-305 item 4 patch, and that patch had
not run. It has. At the SHA above, the bow shock hover's Lugaz-midpoint
sentence is gone and the standoff attribution reads Jelinek. Revision 2
was right as written and the header now carries a real SHA rather than
a placeholder.

**2. Row 5 no longer hands the inner span a citation the string never
makes.** The inner belt string reads "Source (peak): Baker et al.
(2018)." It cites Baker for the PEAK. Revision 2's row 5 told the
checker Baker supports rows 2 AND 3, which hands the span a citation
nobody wrote and makes UNSOURCED unreachable -- the verdict the design
record expects for that row. Row 11 got this right for the outer belt
and is now the model for both.

**3. Row 11 names both sources the string names.** The outer belt
string's source line is "Source (peak): J. Geophys. Res. Space Physics
(2025), doi:10.1029/2024JA033504; Baker et al. (2018)." Revision 2's
row 11 named only the first.

**4. The span rows ask whether an edge exists, not which span is
right.** Revision 2 rowed the four extents as claims to verify, which
invites a checker to pick a winner between two figures neither of which
may be sourced. The question this item is actually about is whether any
accessible source states an edge at all, and in what frame. The rows are
reworded and marked as DISCOVERY rather than citation verification.

**5. Three frames are named, including L.** Revision 2's frame note
described rows 3 and 4 as one belt in two frames. There are three: the
store says L, the hover says Earth radii from centre, the info text says
kilometres of altitude. A checker whose source states L may write L in
the Source unit column and treat it as identical to the hover's R_E. It
is not.

**6. Prompt 3's paste list is corrected.** The altitude sentences are in
`earth_magnetosphere_info`, not in the `shell_configs.py` tooltip. The
tooltip carries the two interpolated peaks and no span in any frame, so
it is pasted for completeness and holds no rowed extent.

## Common header, prepended to each prompt

> Built on `f1bceefd05eeee0cac38fd519dd207314acb2383`
> at https://github.com/tonylquintanilla/palomas_orrery. Read
> `PROJECT_INSTRUCTIONS.md` (Fetched vs Recalled Convention) and
> `skills/provenance-discipline/SKILL.md` (The Access Standard, Worksheet
> Types) at that SHA before starting; in your reply, state which of those
> two files you read. The author of this code is not a professional
> programmer; the code's polish is the product of AI collaboration and
> says nothing about the author's fluency. Write for a retired civil
> engineer.
>
> Two jobs are mixed in these tables and each row says which it is.
>
> [CITATION] -- go to the source the string names and confirm the source
> states the claim at the stated precision. Then, separately, check the
> value against an accessible primary source of your own choosing.
>
> [DISCOVERY] -- the string states a figure that may have no source at
> all. Do not assume one exists and do not reconcile it with any other
> figure in the table. Find whether an accessible source states it, say
> which, and if none does, say that. UNSOURCED is a valid and useful
> answer.
>
> A source you cannot open without a login FAILS; say so. Record the URL
> you actually opened for every source, and one access word: OPEN (full
> text), ABSTRACT, SNIPPET, WALLED.
>
> Return ONE table, this schema, one row per claim:
>
> | # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |
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

1. [CITATION] Earth's magnetosphere extends about [store value] Earth
   radii on the Sun-facing side.
2. [CITATION] It stretches into a long magnetotail on the night side.
3. [CITATION] It protects Earth from solar radiation.
4. [CITATION] It protects Earth from cosmic rays.
5. [CITATION] ...making complex life possible.
6. [CITATION] Citation row: Shue et al. (1998), J. Geophys. Res.
   103:17691, doi:10.1029/98JA01103 supports the magnetopause standoff.

Note for the checker: row 6 is a citation row. The standoff number
itself is checked on its own store row and is out of scope here. On row
5 -- verdict it as stated; do not soften it into something defensible.

**Additional, and it is the point of this prompt.**

7. [DISCOVERY] The magnetotail is asserted in prose with no figure. How
   far downstream has Earth's magnetotail been observed, and by what
   measurement? Give the figure, its uncertainty or range, its reference
   frame (Earth radii from centre, unless the source says otherwise),
   and whether the observation is of a coherent tail or of a signature.
   We hold Ness, Scearce and Cantarano (1967), J. Geophys. Res. 72:3769,
   doi:10.1029/JZ072i015p03769 -- a Pioneer 7 crossing at 900 to 1,050
   Earth radii, whose title says "probable" and whose abstract reports
   no coherent tail with a neutral sheet at that distance. Verify that,
   and say whether a later open source restates it or supersedes it.

## Prompt 2 -- Bow shock

Paste `bow_shock_text` from `earth_visualization_shells.py` and the bow
shock paragraph of `earth_magnetosphere_info`.

Claims to row:

1. [CITATION] The bow shock is the boundary where the supersonic solar
   wind is first slowed by Earth's magnetic field.
2. [CITATION] It is typically located about [store value] Earth radii
   upstream on the Sun-facing side.
3. [CITATION] Citation row: Jelinek, Nemecek and Safrankova (2012),
   J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252 supports the
   bow shock standoff.
4. [CITATION] Corroboration row: Lugaz et al. (2016), Nat. Commun.
   7:13001, doi:10.1038/ncomms13001 states that under normal solar wind
   the bow shock forms at a subsolar distance of 11 to 14 Earth radii.

Note for the checker: row 4 is not the source of the drawn value and is
not claimed to be. It no longer appears in any display string; it is
checked because the store keeps it as a corroborating range, and we want
to know whether Lugaz states that range and in what frame.

## Prompt 3 -- Van Allen belts

Paste `belt_texts` from `earth_visualization_shells.py`, the belt
paragraphs of `earth_magnetosphere_info` from the same file, and the
belt lines of the `magnetosphere.tooltip` block in `shell_configs.py`.
The tooltip is pasted for completeness: it carries the two flux peaks
and no extent, so no row below comes from it.

Claims to row:

1. [CITATION] The inner belt holds mainly protons.
2. [CITATION] The inner belt is drawn at its flux peak, [store value]
   Earth radii from centre.
3. [DISCOVERY] The inner belt's extent. The hover states "spans roughly
   1.1 to 2 Earth radii". Does an accessible source state an inner edge
   and an outer edge for the inner belt? Give each edge, the frame the
   source uses, and the source. If no source states an edge, say so.
4. [DISCOVERY] The inner belt's extent in altitude. The info text states
   "from about 1,000 km to 6,000 km above Earth's surface". Same
   question: does a source state these, and in what frame?
5. [CITATION] Citation row: Baker et al. (2018), Space Sci. Rev. 214:17,
   doi:10.1007/s11214-017-0452-7 supports row 2 -- the PEAK. The string
   cites Baker for the peak only. Whether Baker also states an extent is
   row 3's question, not this row's.
6. [CITATION] The outer belt holds mainly electrons.
7. [CITATION] The outer belt is drawn at its flux peak, [store value]
   Earth radii from centre.
8. [DISCOVERY] The outer belt's extent. The hover states "spans roughly
   3 to 7 Earth radii". Does an accessible source state an inner edge
   and an outer edge for the outer belt? Give each edge, its frame, and
   its source; if none does, say so.
9. [DISCOVERY] The outer belt's extent in altitude. The info text states
   "from about 13,000 km to 60,000 km above Earth's surface". Same
   question.
10. [CITATION] The outer belt moves with geomagnetic activity.
11. [CITATION] Citation row: the string's source line names both
    J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504 and
    Baker et al. (2018), for row 7 -- the PEAK. Does each support it?

**Note for the checker, and please read it before starting.**

There are THREE reference frames in play here, and two of them look
alike.

- **L**, the McIlwain L-shell: the distance in Earth radii at which a
  magnetic field line crosses the magnetic equator. Dimensionless. Most
  radiation-belt literature states belt extents in L. For a dipole field
  L equals geocentric distance AT THE MAGNETIC EQUATOR and nowhere else:
  a belt at L = 4 reaches much lower altitudes at high latitude.
- **Geocentric distance in Earth radii**, measured from Earth's centre.
  This is what the code's hover says.
- **Altitude in kilometres**, measured from Earth's surface. This is
  what the code's info text says. It differs from geocentric distance by
  one Earth radius.

If your source states L, put L in the Source unit column. Do NOT treat
it as interchangeable with the hover's Earth radii from centre -- saying
they are the same is a claim about the field geometry, and it is only
true at the equator.

At Earth's equatorial radius of 6,378.1 km, the two code frames convert
as follows. This is given so no checker has to compute it and no checker
can skip it:

| Row | As written | Converted |
|---|---|---|
| 3 | 1.1 to 2 radii from centre | 638 to 6,378 km altitude |
| 4 | 1,000 to 6,000 km altitude | 1.16 to 1.94 radii from centre |
| 8 | 3 to 7 radii from centre | 12,756 to 38,269 km altitude |
| 9 | 13,000 to 60,000 km altitude | 3.04 to 10.41 radii from centre |

**Both pairs disagree.** The inner belt differs by about 360 km at the
low end. The outer belt agrees at the low end within rounding and
differs by a factor of about 1.5 at the high end.

Do NOT reconcile them, do not assume one is a rounding of the other, and
do not pick a winner. Each of rows 3, 4, 8 and 9 is answered on its own
against a source. Deciding which figure survives is our job; telling us
what the sources actually say is yours, and "no source states this" is
one of the more useful things you can tell us.

## Scope, unchanged from revision 1

Tony, 2026-09-11: the belts are in slice 1. Strings A and B carry belt
claims, checking a string means checking all of it, and the belt hovers
are the twins of those claims. All three prompts run in one round,
competitive pattern -- each prompt to two checkers independently, the
two worksheets compared.

Written September 2026 with Anthropic's Claude Opus 5.
