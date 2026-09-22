# Addendum to the dipole-tilt reply -- two recommendations withdrawn, and the skill revision that replaces them

**Built on orrery `a318b3ecfed1ffaa290e8b34ed1ef63caa59295d`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `b17fd92704054e83424651585aa68a393ecb3d92`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io,
the same SHAs as the reply it amends
(`REPLY_L322_C2_dipole_tilt_method_fable_20260921.md`).** Skill text
quoted below is provenance-discipline 2.16 as read from the orrery repo
at `a318b3ec`; the copy mounted in this session reads 2.15 and was not
used, as the reply records.

**Type: ADDENDUM, Mode 7.** Written September 21, 2026 by Claude Fable
5.1, on Tony's question of the same date: "when it comes to a decision,
what is the basis? the basis should be in the skill not arbitrary."

## 1. What is withdrawn

Two recommendations in the reply's sub-questions 4 and 5 were offered
as Tony's calls. Neither had a rule behind it, and both go.

- "The belt hover should print 9.4, not 9.4105." Rule 7 permits a
  shorter display; it gives no method for choosing one. The
  recommendation was taste.
- "Remove the drift sentence in C2 and record the secular-variation rows
  for later." The skill's own show-or-cap rule decides the opposite,
  as section 2 says.

The rest of the reply stands: form A, the three coefficient rows, the
count of five by counting, the epoch 2020.0, the source and read lines,
and the list of what moves.

## 2. The basis, which was already in the skill

2.16, The ceiling, second bullet:

> **Show or cap.** Where the source publishes the size of a relation's
> mismatch as a number the store can hold and the page can show, show
> it beside the value ... Where it does not, cap the count and say why
> on the row ... This decides which of the two answers applies.

The belt hover draws one tilt for an Earth whose tilt drifts. That is
the relation, and its mismatch over the model's own validity span is
a quarter of a degree. IGRF-13 publishes the size of the drift as
numbers: the 2020-25 secular-variation column of the same file, three
coefficients for degree 1. The store can hold them and the page can
show the rate they give. So the rule says SHOW, and the decision is
made by the rule:

- Three more measured rows: the secular-variation coefficients for
  g(1,0), g(1,1), h(1,1), unit `nt_per_year`, source and read from the
  same file, figure counts by counting (5.7, 7.4, -25.9: two figures
  each).
- One derived row, the tilt's rate of change, an expression over the
  six coefficient rows: the tilt at 2020.0 plus one year of variation,
  minus the tilt at 2020.0. Its count follows from its inputs by Rule 3;
  its `# Derived:` line states the result at that count, about -0.05
  degrees per year.
- The hover prints the tilt at its DECLARED count with its epoch and
  the rate, both served: "tilted 9.4105 degrees from it (IGRF-13,
  epoch 2020.0), decreasing about 0.05 degrees a year". Words Tony's;
  numbers the store's.

Nothing in that is chosen. The tilt row's count stays five, by
counting, because the drift is shown rather than capped.

Cost to C2: the tilt now brings six measured rows and two derived rows
in place of one typed row. All eight feed a drawn value, so all are in
bound by the Read Field's scope sentence, and all take their read from
the one NOAA file the builder already opened.

## 3. The gap the question exposed, and the revision that closes it

The gap is Rule 7. As written it permits a display to show fewer
figures and says nothing about when. Every use of that permission is
therefore a judgment call, and Tony's item 9 (the geocorona at
600,000 km, LEO's inner edge at 6,578.1366 km, the outer belt at
28,701.615 km) is that call arriving at the integrator three times,
which Method Belongs to the Skill says should not happen.

The method that closes it: a display never decides a count. It prints
the declared count. When the declared count reads as too many figures,
that is a finding about the ROW, and Rule 3 already holds the two ways
a row's count comes down: the ceiling, where an uncertainty is stated,
and the "relation itself is approximate" sentence, with show-or-cap
deciding between showing the mismatch and capping for it. Applied to
item 9:

- The outer belt at 28,701.615 km: a midpoint declared from a range the
  source gives to one figure (3 to 7 Earth radii). The product keeps
  the radius's eight figures by counting, but the relation -- one
  drawn radius for a belt the source gives as a span -- is approximate
  and the source publishes the mismatch as the span. Show-or-cap says
  show: the hover already prints "Measured extent: 3 to 7 Earth radii"
  beside it. With the mismatch shown, the count is not capped, and the
  row's declared count stands. If Tony judges the eight figures wrong
  even so, the fix is a cap on the row with the reason, not a shorter
  display.
- LEO's inner edge at 6,578.1366 km: the planet radius plus a declared
  200 km. The sum rule keeps the radius's decimal place and the
  relation is exact. Nothing to cap. It prints as declared.
- The geocorona at 600,000 km: an integer with placeholder zeros, one
  figure. It already prints as declared.

So item 9 is answered by the rows, and nothing on it needs Tony.

### Proposed wording for provenance-discipline, marked proposed

**Rule 7, replaced whole.** Current text at `a318b3ec`, lines 1943-1946:

> **Rule 7. The declared count governs reporting; a display may show
> fewer, never more.** A hover formats to the served count or to a
> shorter readable count; a shorter display is not a precision claim.
> A display with more figures than the row declares is the failure.

Proposed:

> **Rule 7. A display prints the declared count, never more, and never
> chooses fewer.** A hover formats to the served count. A display with
> more figures than the row declares is the failure. A display that
> reads as too many figures is a finding about the ROW, not about the
> page: the row's count comes down under Rule 3 -- by the ceiling where
> an uncertainty is stated, or by a cap with the reason on the row
> where the relation is approximate and its mismatch cannot be shown --
> and the page then prints the shorter count because the row declares
> it. The page never shortens on its own, because a shortening the row
> does not record is a judgment nobody can find later, and the served
> count is what every checker reads. (The one exception is a served
> count above a display's fixed width, which truncates and says so; the
> gallery's AU line at min(3, count) is that case and is a format
> limit, not a precision choice.)

**Show or cap, one sentence added** to the bullet at line 1863, after
"This decides which of the two answers applies.":

> It also decides a snapshot of a quantity that moves: where the source
> publishes the rate, the store holds the rate's inputs and the page
> shows the epoch and the rate beside the value; where it does not, the
> count is capped to the place the movement over the model's validity
> span supports. Earth's dipole tilt is the case: IGRF-13 prints the
> secular variation, so the tilt prints at its full count with its
> epoch and its rate.

**Rule 6, one sentence added** after "Rounding an intermediate puts a
rounding error inside the store.":

> Where a source prints the parts and states the relation that makes
> the whole, the whole is a derived row over measured rows for the
> parts, never a typed result with its working in a comment; a closed
> slice does not accept the typed form. IGRF-13 prints the three
> degree-1 coefficients and says the pole is computed from them, so the
> tilt is an expression over three coefficient rows.

The origin line for the bump quotes Tony's question of 2026-09-21 in
full, names the dipole tilt as the worked case, and records that
Fable's reply of the same date had offered two display choices with no
rule behind them and withdrew both.

## 4. What this changes in the manifest

- 4.2 and 4.3a: eight rows for the tilt, as section 2 lists.
- Section 6: the belt tilt line prints the full count, the epoch and
  the rate; the exact words go to Tony with the other hover wording.
- Section 13, item 9: removed. Its three cases resolve on the rows as
  section 3 says, and the manifest records each resolution in words.
- The skill bump: the C2-0 bump has been cut as 2.16. These three
  changes are a further bump, 2.17, and by the manifest's own ordering
  it comes BEFORE the walk applies them, in its own session, with the
  reinstall confirmed by the session after. That costs one more
  session boundary. The alternative, applying the method now and
  writing it into the skill afterwards, is what v3.65 did for the
  cache builder and is allowed only when the rule was learned during
  the build. This one was learned before it, so v3.55's order applies.

---

Written September 21, 2026 with Anthropic's Claude Fable 5.1.
