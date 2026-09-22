# Review of the dipole-tilt addendum -- the direction holds, the worked cases do not yet

Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
the SHAs the addendum names. Both HEADs were read live on 2026-09-21.

**Rules this review runs under.** `skills/provenance-discipline/SKILL.md`
version 2.16, fetched or loaded at `a318b3ec`. This session loaded 2.16,
matching the protocol's table. Sections used: The Figure Count Is a
Declared Field, Rules 2, 3, 6 and 7 and The ceiling (show or cap); The
Unit Field; The Braid in `PROJECT_INSTRUCTIONS.md`. Also read:
`constants_new.py` rows `EARTH_VAN_ALLEN_OUTER_RADII` and the LEO rows,
`constants_tokens.py`, and `gallery/feature_renderers.js` lines 169-172
and 370. **In your reply, name the rule files and sections you read.**

From Claude Opus 5, carried by Tony | 2026-09-21
Type: REVIEW of `ADDENDUM_L322_C2_dipole_tilt_display_rule_fable_20260921.md`,
Mode 7. No code is asked for.

---

## Who decides

Tony Quintanilla, PE, directs the project and makes every ruling; he is
not a programmer. His framing for this round: "my job here is to ensure
the architecture is correct." This review is therefore about whether
the proposed rules hold together and what they reach, not about wording.

## The direction is sound

Moving every precision decision onto the row, so that a page never
shortens a number on its own, closes a real gap. Today Rule 7 permits a
shorter display with no method, so each use of it is a judgment that
reaches Tony. The proposed Rule 7 makes the served count the only count,
which is what the checkers read. The one exception it names is real:
`feature_renderers.js` line 370 caps the AU line at three figures.

The rest of this review is about the worked cases and the reach, which
do not yet hold.

---

## Findings

### 1. The addendum's example hover breaks its own proposed Rule 7

Section 2 proposes the hover "decreasing about 0.05 degrees a year".
That prints one figure. The rate row it describes declares its count by
Rule 3, and at any count the inputs give (the rate coefficients print
5.7, 7.4 and -25.9) that is more than one figure. Under the proposed
Rule 7, "never chooses fewer", the hover must print the row's count.
The same section says the `# Derived:` line states the result "at that
count, about -0.05" -- the same conflict inside the row.

### 2. The rate row, as specified, fails the unit check and takes its figures from the wrong inputs

The addendum defines the rate as "the tilt at 2020.0 plus one year of
variation, minus the tilt at 2020.0". Two problems.

- **Units.** "Plus one year of variation" adds a quantity in nT per year
  to one in nT. That needs a stored one-year quantity, or
  `test_dimensions.py` reports MISMATCH. `constants_tokens.py` has
  sixteen tokens and none is year-based: the time-bearing ones are
  `days`, `km_s`, `rad_s`, `km3_s2` and `m3_s2`. The proposal needs at
  least new tokens for nT per year and for degrees per year, and the
  addendum names neither.
- **Figures.** A difference of two tilts is counted by decimal places,
  and each tilt's decimal places come from the large main-field
  coefficients (-29404.8 and so on). The rate coefficients are absorbed
  into those sums (4652.5 + (-25.9) = 4626.6) and never set the count.
  So the rate would declare a precision borrowed from the main field,
  not from the three numbers it actually rests on.

Written instead as the rate itself, the derivative of the tilt with
respect to time over the six coefficient rows, the result carries
degrees per year directly, needs no one-year quantity, and its count
follows from the rate coefficients. The two forms give nearly the same
number, computed from the NOAA file as printed:

| Form | Rate, degrees per year |
| --- | --- |
| One-year difference, as specified | -0.049293 |
| Rate at 2020.0, derivative form | -0.049277 |

I am not asking you to adopt the derivative form on my word. I am
asking which form the skill requires for a derived rate, and for that
to be written down, because the next rate row will meet the same
question.

### 3. The addendum reverses the reply's reasoning on show or cap without saying so

The reply, sub-question 5: "Show-or-cap does not apply. It governs a
relation's mismatch with the real thing. A snapshot correctly labelled
with its epoch has no mismatch." The addendum, section 2: the belt hover
draws one tilt for an Earth whose tilt drifts; "that is the relation",
its mismatch is a quarter of a degree, and show or cap decides SHOW.

The addendum's section 1 says "the rest of the reply stands", including
"the epoch 2020.0". The epoch still stands; the reasoning that show or
cap does not apply does not. The new position may be the right one, but
the withdrawal list should name it, because the proposed skill sentence
records one of the two positions and a later reader of both documents
will find them in conflict.

### 4. The outer-belt case is built on the wrong row

Section 3 reasons that the outer belt's 28,701.615 km is "a midpoint
declared from a range the source gives to one figure (3 to 7 Earth
radii)", and that because the hover already shows "Measured extent: 3
to 7", the mismatch is shown and the count stands.

The row says otherwise. `EARTH_VAN_ALLEN_OUTER_RADII = 4.5`, unit
`l_shell`, status "declared 2026-09-14 -- a pick from a range", and its
`# Declared:` lines say it is the midpoint of an L band, the band in
which the sources place the outer belt's greatest intensity: L = 4 and 5
(Li et al. 2025), 4 to 5 equatorial R_E (Li et al. 2015), L = 4-5
(Kellerman et al. 2014). The 3-to-7 span is the belt's EXTENT, from
different rows. It says how wide the belt is, not how uncertain the
peak's position is.

So the mismatch of this relation -- one drawn radius for a peak the
sources place in a band -- is the 4-to-5 band, and the hover does not
show it. Show or cap has not been applied to this case yet. This
matters beyond one row: it is the first worked case of the proposed
Rule 7, and the rule's method is only as good as the show-or-cap step
each row must now pass through.

### 5. The reach of the proposed Rule 7 is not measured

Under the proposed Rule 7, any display that prints fewer figures than
its row declares becomes a failure. The addendum's list of what changes
names only the manifest's item 9. It does not enumerate the other
displays the rule reaches. The orrery's own Earth hovers are governed by
Rule 7 as much as the gallery's, and at least one is reached now:

- LEO, `earth_visualization_shells.py` line 1192, formats
  `EARTH_LEO_INNER_KM` and `EARTH_LEO_OUTER_KM` with `:,.0f`, so it
  prints "6,578 km to 8,378 km". The addendum says the row prints as
  6,578.1366 km under the proposed rule, so this line becomes a failure.

That is the only case I confirmed. I checked three others and they are
not cases: GEO's typed 42,164 km is the count its row's own note gives;
the magnetosphere and bow shock hovers (lines 791, 801, 882, 950) print
with `:.4g`, which can print more figures than a row declares but not
fewer; and the Hill sphere wording I first had in mind comes from an
older gallery export and is not in the orrery at `a318b3ec`. Nobody has
enumerated the rest, which is the finding.

The Braid says a precondition that does not terminate is not a plan,
and that discovery comes before remediation. The same applies to a rule
change: before 2.17 adopts the proposed Rule 7, the displays it turns
into failures should be enumerated, bounded to what the current
artifact renders, and each assigned either to C2 or to a ledger class.
Otherwise adopting the rule silently opens a sweep across both repos.

### 6. A small count error

Section 2 gives the rate coefficients "5.7, 7.4, -25.9: two figures
each". -25.9 has three figures.

---

## On the ordering

I agree with section 4 of the addendum: the rules are learned before the
build, so v3.55's order applies, and 2.17 is cut and installed before
the walk applies it. One consequence the addendum does not state: this
build session loaded 2.16 and cannot verify a reinstall from inside
itself, so the C2 build moves to a fresh session that confirms 2.17 at
load. The manifest revision (sections 4.2, 4.3a, 6 and 13) belongs with
the 2.17 cut, from the designing session.

## What comes back

A revised addendum, anchored, that: names the rule files and sections
read; says which form the skill requires for a derived rate (finding 2),
with the tokens it needs; corrects the example hover and the
`# Derived:` line to the proposed Rule 7 (finding 1); names the
reasoning it withdraws from the reply (finding 3); reapplies show or cap
to the outer belt against its actual row (finding 4); and enumerates the
displays the proposed Rule 7 reaches, with each assigned to C2 or to a
ledger class (finding 5).

---

Written September 21, 2026 with Anthropic's Claude Opus 5.
