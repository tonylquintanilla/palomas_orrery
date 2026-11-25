<!-- Doc-Kind: hand | Part 1 report of the L-533 last-day brief: how every path still flying gets its span's last day, what it costs, the comets, the capture craft, the 27 boxes before and after, the "ended" fact, and the planted cases. No code was changed. -->
# L-533 (ESCAPADE): Part 1 report, every path to its span's last day

Built on f054d1f580ac70c27a1a6c8d681cd661026e8460 at
https://github.com/tonylquintanilla/palomas_orrery and
b2d9eaa66ed33ec93fc2bbcbdc5b85d5b872e043 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (both
branch main, read 2026-11-25; Tony's two folders equal them, his run
record copy edited). No code changed; this file is the only new one.
Written November 25, 2026 by one Claude Code session (Claude Opus 5.5)
working from documentation/COORD_L533_last_day_brief_20261125.md.

Skills read: gallery-cache-builder 1.23 (whole); horizons-orbital-
mechanics 1.20 (How a Path's Events Are Found, with A Comet on an Open
Path); agentic-pre-test 1.4 and safe-file-editing 1.15 by their headers,
to be read whole before Part 2. The as-built page's section A Spacecraft
Is Fetched by Its Plan, read.

## The claim

The brief agrees with the code. The fix is one more question to JPL per
path, the span's last day asked as an ended mission's already is, and
asked once on the first night for the 27 that lack it. Two cases need a
rule of their own: the Voyagers, whose JPL data ends at the very first
minute of their last day, and the two craft orbiting a planet, whose
last day will one day sit inside the date window.

Checked against the brief: the 27 short paths and their days short,
read again from the served index at b2d9eaa6, match the brief's list
exactly (7 ended at their last day; 27 still flying, 1 to 7 days
short). JPL asked today: Voyager 1 answers 2100-01-01 00:00 TDB and
refuses 00:01 ("No ephemeris for target "Voyager 1 (spacecraft)" after
A.D. 2100-JAN-01 00:00:00.0000 TD"); ESCAPADE-Gold answers 2027-09-10
00:01 and 00:02 TDB.

## 1. How the last moment is asked, and on which nights

WHAT "THE SPAN'S LAST DAY" MEANS HERE. A plan's span ends on a day
(`"end": "2027-09-10"`). `_plan_span` turns it into an instant, that
day's 00:00 on JPL's clock, and every backbone, event and tail question
stops there. The box prints a day on UTC (`servedDay`, the nearest
minute), and 00:00 TDB is 23:58:51 UTC the evening before. So a point
at that instant prints as the day before: Gold would read "9
September". The brief's own close expects "10 September 2027", so the
last day is asked inside the day, as an ended mission's is: its first
two minutes on UTC, 00:00 and 00:01 (00:01 and 00:02 on JPL's clock).
`fetch_path_last_day` does exactly that today, for an ended path only.

THE CHANGE (`tools/gallery_cache_builder.py`):
- `fetch_path_last_day` asks every path's last day, flying or ended;
  its "{} for a path still running" goes.
- WHERE JPL'S DATA ENDS AT THE DAY'S FIRST MINUTE (the Voyagers, the
  only two: their span's end is the orrery's far stop, 2100-01-01,
  which JPL's end meets to the minute), JPL refuses the two minutes. On
  that refusal, read by JPL's own words ("No ephemeris ... after"), the
  builder asks the one instant JPL holds, the span's end as
  `_plan_span` gives it, 2100-01-01 00:00 TDB, which the backbone's
  stop already asks every whole fetch. Nothing is asked past JPL's
  data that is not refused; nothing past it is served. A refusal of any
  other kind raises as now.
- THE FIRST NIGHT (the heal). A path is fetched whole only when its
  plan is new; otherwise only its tail. So with the change alone, the
  27 would get their last day only when the orrery next remakes each
  plan (the comets' are 30 days old today; the spacecraft's on about
  Dec 4; ESCAPADE's about Dec 18), and the new check would be red until
  then. So on a tail night, a path whose saved points hold none on its
  span's last day (a saved key starting with the span's end day) is
  asked its last day too. The saved points are kept between nights, so
  it is asked once and then not again until a plan is new.
- A LAST-DAY QUESTION JPL DOES NOT ANSWER fails the object as any of
  its questions does: the path is served last-good and held by name
  (L-553 (a held body turns the night red)), and the night's check
  accepts it by its hold.

WHAT IT COSTS IN QUESTIONS TO JPL:
- The first night after the push: 27 more questions, and 2 more for
  the Voyagers' refusal and fallback; 29 in all, each a two-minute
  table.
- Every night after: none more.
- Each whole fetch (a plan made again, about every 30 days a path): one
  more question (three for a Voyager). About 29 a month across the 27.

The points served grow by two a path (one for a Voyager). The
backbone's thinning cannot remove them: they are merged after it, as an
event's window is.

## 2. The 13 comets on open paths

Their span ends a year after the day their plan was made, clipped to
JPL's data: all 13 today end 2027-10-26, their plans made 2026-10-26.
Their last day is that day. The plan is made again when 30 days old, so
the last day steps forward about a month at each remaking (to the
remaking day plus a year), and the whole path is fetched again then,
the last day with it, for one question more. Between remakings it does
not move, so "to a year after today" in their box (COMET_SPAN_WORDS) is
up to 30 days less than a year; that was so before this build too, and
the words already say "or less". If the orrery remakes the comets
before the push, their after-day below is the new plan's end, not 26
October 2027.

## 3. Juno and BepiColombo, the capture craft

Today nothing in the fine layer moves. The fine layer covers the date
window only (to 2027-02-22 for both), and its two tests (each served
point held out; JPL's own in-between points) look only inside it. The
new last point (Juno 2028-09-02, BepiColombo 2027-04-10) is outside, and
the positions file keeps the plan's points outside the fine span, so it
passes through untouched.

ONE GAP THE BUILD WOULD OPEN, and its fix in the plan. When the window
reaches the span's end (BepiColombo's from about 2027-01-12, Juno's in
mid-2028), the fine layer stops at the last whole day before the end
(`capture_span`), leaving about a day between its last point and the
new last-day pair with no fine points and no loop's reach. A minute
there would be worked out along a straight chord across a day of loops
around Mercury, so the box would print a figure far smaller than its
real miss, which A Capture Craft's Box Never Claims Less Than Its Miss
forbids. Today that minute is past the last served point and reads
"This mission ended" (section 5). The plan: those days join
`no_figure_days`, so they print no distance, the L-553 rule ("A day
with no fine points and no loop's reach prints no distance"). Running
the fine layer to the very end instead is a larger change; not
proposed.

## 4. What each of the 27 boxes reads, before and after

Two places in each box carry the day: the path sentence ("... as far as
<day>.") and the source line ("from <first> UTC to <day> UTC"). No other
words change. Before is the served index at b2d9eaa6; after is the
span's end day, except the Voyagers.

| path | before | after |
|---|---|---|
| solar_orbiter | 19 November 2030 | 20 November 2030 |
| wierzchos | 25 October 2027 | 26 October 2027 |
| atlas_2024_g3 | 24 October 2027 | 26 October 2027 |
| escapade_blue | 10 September 2027 | 12 September 2027 |
| juice | 19 July 2031 | 21 July 2031 |
| borisov_2025_v1 | 23 October 2027 | 26 October 2027 |
| borisov_2i | 23 October 2027 | 26 October 2027 |
| escapade_gold | 7 September 2027 | 10 September 2027 |
| panstarrs_2025_r3 | 23 October 2027 | 26 October 2027 |
| voyager_1 | 29 December 2099 | 31 December 2099 |
| oumuamua | 22 October 2027 | 26 October 2027 |
| europa_clipper | 29 August 2034 | 3 September 2034 |
| mcnaught | 21 October 2027 | 26 October 2027 |
| osiris_apex | 17 March 2030 | 22 March 2030 |
| tsuchinshan_atlas | 21 October 2027 | 26 October 2027 |
| voyager_2 | 27 December 2099 | 31 December 2099 |
| bepicolombo | 4 April 2027 | 10 April 2027 |
| atlas_3i | 19 October 2027 | 26 October 2027 |
| c2025_k1 | 19 October 2027 | 26 October 2027 |
| c2025_k1_b | 19 October 2027 | 26 October 2027 |
| c2025_k1_d | 19 October 2027 | 26 October 2027 |
| west | 19 October 2027 | 26 October 2027 |
| juno | 26 August 2028 | 2 September 2028 |
| lucy | 6 March 2033 | 13 March 2033 |
| new_horizons | 24 December 2049 | 31 December 2049 |
| parker_solar_probe | 24 December 2029 | 31 December 2029 |
| psyche_spacecraft | 17 February 2029 | 24 February 2029 |

THE VOYAGERS READ 31 DECEMBER 2099, NOT 1 JANUARY 2100. JPL's data for
both ends at 2100-01-01 00:00 on its own clock, which is 23:58:51 UTC on
31 December 2099, and the box prints UTC days. Not one UTC minute of 1
January 2100 exists in JPL's data. This is the only day in the table
that differs from the plan's span. The orrery's own rule for a JPL end
in a day's first minutes (`path_plan.jpl_limit`) would make their span
end 2099-12-31; it does not apply because the far stop is never refused.
That is orrery code and out of scope; the box reads the same day
either way.

## 5. One fact: "This mission ended on ..." for a craft still flying

Confirmed from the code. The box says it whenever the minute shown is
after the path's last served point (`render_spacecraft.build_spacecraft_
traces`: `ended = at is None and epoch_jd > rows[-1][0]`). Nothing asks
whether the mission ended; `mission_end` only picks the day printed. So
for a craft still flying it is false, and it would also print, in the
source line, "to the day the mission ended".

No date reaches it today. A room's minute is held to the served window
(2026-08-28 to 2027-02-21 in today's index), and the earliest last
served point of a craft still flying is BepiColombo's, 2027-04-04. A
room opened now always shows now, before every last point. Only a
shared link's minute (?at=) can reach it, from about 2027-01-06 for
BepiColombo as served today; after this build, from about 2027-01-12,
when the window's end (about 88 days after the build) reaches 10 April
2027.

Words proposed, Tony's to approve, not built. For a craft whose entry
has no mission_end and whose path has ended before the minute shown:
- Opening: "JPL's path for it stops on 10 April 2027. The marker is
  where it was that day."
- Distance, after the figure: " on the last day of JPL's path"
  (in place of " on its last day").
- Path sentence: "Its path is solid all the way, since the day shown
  is after JPL's path ends, from 21 October 2018 to 10 April 2027."
- Source line: keeps ", as far as JPL's data runs" (in place of ", to
  the day the mission ended").
Where JPL's sheet says when its path turns to prediction, L-554 (JPL's
sentence when a path is a prediction) would add that sentence; held
for that item.

## 6. The planted cases, by name, and where each runs

In the builder's offline suite, `tools/test_gallery_cache_builder_
offline.py` (620 checks at the base):
- "every path still flying ends on its span's last day": a whole fetch
  of the stand-in Voyager 1 plan ends in the span's last day. Planted
  fault: the old rule, the last day asked only for an ended path; the
  backbone stops short and the check fails.
- "a night asks a missing last day once": a saved path without its last
  day, same plan; the first night asks the tail and the last day, the
  next night the tail alone. Planted fault: the heal off; still short.
- "JPL's data ending at the day's first minute": the fake JPL refuses
  any stop past the span's end instant, in JPL's words, as Voyager 1
  does; the last point is that instant, nothing served past it. Planted
  fault: no fallback; the path fails and is held.
- "nothing asked past the span", restated: no backbone, event or tail
  stop passes the span's end instant (the Voyagers' lesson, kept), and
  the last-day question never passes the day's first two UTC minutes.
  The existing planted fault (the span's end taken as it stands) kept.
- "a capture craft's last day prints no distance": the window meeting
  the span's end; the days between the fine layer and the last point
  are in `no_figure_days`. Planted fault: not marked; the check fails.

The nightly check, in `documentation/smoke_solar_system_figures.js`
(part 7, the "Solar System figures" row of the gallery maintenance run,
which the night runs): today it holds the last day for an ended mission
only (`endedIssue`). It becomes every path's: the served index's end and
the positions file's last point, each on its span's last day by JPL's
clock or at its first minute (the Voyagers), each path printed by name
with the day its box reads and the count ("Paths at their span's last
day (34 of 34): ..."); red, by name, when one is short or past; a held
path accepted by its named hold. Planted, inside the check, before it
is trusted: Gold at 2027-09-07 01:49 against 2027-09-10 fails; a point
on the day after the span fails; Voyager 1 at 2100-01-01 00:00 passes.

Then the dry run against JPL that fetches the 27 and prints each one's
span end beside its last point, and the rest of Part 2 as briefed.

## Owed, outside this build

- The orrery's own drawing (path_drawing.py) adds the website's
  last-day pair to an ended path only, so the desktop orrery's dashed
  line will still stop at its last 7-day point. Orrery code; recorded on
  L-533 at the close.
- The Voyagers' span on the orrery's side (section 4). Recorded, not
  proposed.
