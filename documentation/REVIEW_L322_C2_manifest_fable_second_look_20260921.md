# Second look -- the revised L-322 Stage C2 build manifest

**Built on orrery `b9cd48440a8879f7c79207dfc181bfaaf584caf4`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `06fdad8cc16da72d00e28c8066dbcbde7f590587`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs re-read live with `git ls-remote` on 2026-09-21; neither has
moved.** The first SHA is the orrery, the second the gallery. The
revised manifest is still not in either repository; I reviewed the copy
Tony carried.

**Type: REVIEW, second look.** Written September 21, 2026 by Claude
Fable 5.1, inside Tony's Project, same session as the first review.
Rule files read: as listed in the first review, nothing added. Nothing
was built and the manifest was not edited.

## The twelve findings

All twelve were taken up and I have no quarrel with how. Two of Opus's
corrections to MY figures are right and I re-measured both: the plain
sum of the five effects is 0.248 (I wrote 0.24, from a one-sided step,
the very mistake Finding 3 was about), and the kilometre line holds to
0.2479, so it sits on its boundary at the ceiling and is not "safe
across the whole range" as I said.

## New findings

### A. The checker's new fail rule would fail twelve finished C1 rows, and two of C2's own. -- **blocks the build**

Manifest 4.7, second bullet, and 4.0 "When the route fires".

The new rule says: if any measured primary in a row's chain STATES an
uncertainty, the row must use the uncertainty route, and a row that
counts instead FAILS.

Three Earth primaries finished in C1 already state an uncertainty on
their `# Figures:` line (measured on the clone):

- `EARTH_EQUATORIAL_RADIUS_KM` -- "an uncertainty of 0.1 m"
- `EARTH_GM_KM3_S2` -- "the tabulated uncertainty, 8e5 m^3 s^-2"
- `EARTH_D660_DEPTH_KM` -- "660 +/- 10 km"

Twelve derived Earth rows chain through the radius, all counted today:
`EARTH_INNER_CORE_RADII`, `EARTH_OUTER_CORE_RADII`,
`EARTH_LOWER_MANTLE_RADII`, `EARTH_UPPER_MANTLE_RADII`,
`EARTH_GEOSTATIONARY_RADII`, `EARTH_LEO_INNER_KM`, `EARTH_LEO_OUTER_KM`,
`EARTH_LEO_INNER_RADII`, `EARTH_LEO_OUTER_RADII`,
`EARTH_STRATOPAUSE_RADII`, `EARTH_THERMOPAUSE_RADII`,
`EARTH_HILL_SPHERE_RADII`. Two more chain through GM:
`EARTH_GEOSTATIONARY_RADIUS_KM`, `EARTH_HILL_SPHERE_KM`.

So do C2's own two new bow shock rows, `EARTH_BOW_SHOCK_STANDOFF_KM`
and `_AU`. The manifest says they count "since Jelinek states no
uncertainty", but the radius they multiply by does.

And 4.7 names Earth's equatorial radius as its example of a primary
that states NO uncertainty. It states one.

Whether these rows actually go red depends on how the checker reads the
words, which the manifest does not pin down. If it matches only the new
form `uncertainty 0.10`, the three C1 lines are in prose and escape --
and then the rule silently depends on phrasing, which is a check that
cannot fail for the wrong reason. If it matches the word, fourteen rows
fail the moment Earth closes. Either way it is wrong.

What I would change. The route should fire on what MATTERS, not on
whether anything in the chain states a number. Two honest options, and
choosing between them is method, not Tony's:

1. The route is mandatory only when a stated uncertainty is large
   enough to change the reported place. In practice: run the propagation
   for every derived row whose chain states any uncertainty, and FAIL
   only if the count it supports is LOWER than the declared one. A row
   that counts and lands on the same or a coarser place passes, and the
   output says both numbers. This is the one I recommend. It costs no
   rewrite of C1 and it can still fail.
2. Rewrite the fourteen rows' figures lines to the uncertainty form in
   C2. Correct, larger, and it moves C1 hovers only if a count changes
   (I expect none would).

Whichever is chosen: the three C1 primaries' figures lines should be
brought to the 4.0 form (`uncertainty 0.0001` and so on) in this patch,
so the checker reads a field and not prose. Section 8 needs a test on a
C1 row, and its bow shock test should name `STANDOFF_RADII`, the only
bow shock row whose chain truly states none.

### B. The skill text now has two answers for an approximate relation and no rule for choosing. -- **fix before the 2.16 bump**

Manifest 4.0, first bullet.

Rule 3 already says a row may declare FEWER figures when the relation is
approximate; the Hill sphere was cut from seven to three that way. The
new bullet says a model's scatter is SHOWN beside the value, not used to
cut it. Both are right for their cases, but the next body's builder gets
two rules and nothing to pick with. One sentence settles it: where the
source publishes the size of the mismatch as a number that can be
served and shown, show it; where it does not, cap the count and say why
on the row. That is what the two cases actually did.

### C. "about" must not leak into other bodies' hovers. -- **fix before the build**

Manifest 5.1 item 3, 2.3, section 7.

`kmAndAu` is shared by every shell. If "about" goes into it
unconditionally, Sun, Jupiter and Saturn hovers move, which section 7
forbids and the fixture would catch late. 5.1 should say the word is
printed only where a served `standoff_km` is present.

### D. Section 6 is the acceptance test but three of its lines are not strings yet. -- **fix before the gallery patch is cut**

The two km lines say "wording per 2.3" and the scatter lines say "words
Tony's". 5.6 grades by finding each line verbatim. So after Tony
approves the words (section 13, item 5), section 6 is updated with the
exact strings BEFORE the patch is cut, and the manifest should say that
in section 9. Otherwise the builder writes both the hover and the
string it is graded against.

### E. Small leftovers. -- **notes**

- 4.0 says "Three sentences join Rule 3" and lists five bullets. Name
  the five or drop the count.
- 5.2's heading still says "if Tony agrees". He has.
- Section 8's "served lines" bullet says the patch "refuses" on a null
  `standoff_km`; 5.2 now says it rolls back. Make them say the same.
- The closing stamp says September 20; the header says revised the 21st.

## What I did not re-check

The dry-run results, the join counts (78 to 84), and the fixture count
are accepted as written, as before.

---

Written September 21, 2026 with Anthropic's Claude Fable 5.1.
