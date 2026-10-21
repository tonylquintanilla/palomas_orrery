<!-- Doc-Kind: hand | Brief for one build session: the close patch for the design talks of Oct 20, then the Sun's and Earth's 39 citations given their web addresses (L-456), each re-opened before it goes on its row; then the drawer-order rule; then, if the evening allows, the Sun's fourteen hover and tooltip pairs (L-191). -->
# Brief: the talks' close patch, then the 39 addresses (L-456)

Built on orrery 6a8d04c (the "talks" push, 2026-10-21 08:40) at
https://github.com/tonylquintanilla/palomas_orrery and gallery
30db99f ("daily run 10-21-26") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Run
`git ls-remote` on both at the start; if either has moved, read its
newest handoff and Where We Are before building, and build on the new
HEAD.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Written October 21, 2026 by Anthropic's Claude Fable 5.1,
in a coordination session, for a Claude Opus build session. Follows
`HANDOFF_design_talks_20261020.md` (the talks, pushed) and
`HANDOFF_L456_source_list_20261020.md` (the panel, pushed).

## 1. Read this first

- Both L-456 patches are run and pushed (orrery 23f7088, gallery
  4778944). interactive-exhibit 1.18 is reinstalled; confirm the loaded
  copy reads 1.18 before exhibit work. provenance-discipline 2.32 and
  provenance-cross-check 1.1 are confirmed by earlier sessions; the
  manifest at 6a8d04c expects them.
- Tony's latest run record is
  `documentation/WHERE_WE_ARE_10-18-26_1326_run_record.md` at 6a8d04c
  (the session of 10-20, from line 2540 on). Read it before the close
  patch: it holds his phone look, the drawer-order ruling and his notes
  on the Gemini worksheets.
- Two worksheets are in hand, both medium tier:
  `documentation/worksheets/worksheet_gemini4_medium_l456_sun_20261020.md`
  (pushed, 16 Sun works) and
  `worksheet_gemini4_medium_L456_earth_20261021.md` (23 Earth works;
  Tony saves it into `documentation/worksheets/` from this
  coordination session's attachment; if it is not there, ask him for
  it before the Earth half).
- *The Earth worksheet's pre-flight FAILED.* The prompt asks Gemini to
  open arXiv:2202.11533 and quote one sentence. Gemini reported it as a
  Gaia lensed-quasar paper by Jalan and others. The page is Lamy,
  Gilardy and Llebaria, "Observations of the Solar F-corona from
  Space" (opened 2026-10-21 by Claude Fable 5.1; the Sun worksheet
  reported it correctly the day before). So that run did not open its
  pre-flight page. Its 23 rows are LEADS: addresses to try, nothing
  more. Every row of both worksheets is re-opened here anyway (the
  Slice Relay, provenance-cross-check 1.1), so this changes no step;
  it changes what the review file says about the return.
- Tony's ruling of 2026-10-21 on how to proceed: no Gemini re-run, no
  full GPT pass. This session re-opens everything; a short GPT prompt
  goes out afterwards only for the works that did not open (section 4).

## 2. Job 1: the close patch for the design talks (orrery)

The first thing built, before any address work, so the rulings reach
the ledger. One patch, built on 6a8d04c, by section anchors
(ledger-and-session-records 1.21), carrying:

- The ledger lines in `HANDOFF_design_talks_20261020.md`, section 3,
  by handle: L-401, L-411, L-412, L-363, L-434, L-239, L-224, L-356,
  L-375, L-454, L-413, and the "method or Tony's?" item for the next
  talk.
- The Where We Are update in that handoff's section 4.
- From Tony's run record of 10-20 (not in that handoff): his phone
  look at the panel ("excellent, well organized"); the Dziewonski and
  Anderson link not opening, expected until E5 gets its address; the
  drawer-order rule (section 5 below), recorded on L-363 or a new item
  and marked as method for interactive-exhibit 1.19; Gemini's Sun
  worksheet filed; Murray (1989)'s scan in `papers/`
  (`1989A&A...218..325M.pdf`, gitignored; read it through the device
  mount), its galactic axes in section 7 as direction cosines, to
  check against the pole figures cited through Liu, Zhu and Hu; the
  Roche limit book's section number (S12: the contents page puts the
  Roche zone at 4.8, not 4.6).
- L-191's measurement at fcd191e9 is already on the ledger: five pairs
  differ in content, nine are byte-identical. No new line needed.
- Not in this patch: nothing from jobs 2 to 4, which get their own
  close.

Tony runs it, the maintenance run, commits and pushes. Then job 2
builds on that new HEAD.

## 3. Job 2: the 39 addresses, re-opened and written (orrery, then the website by the Daily Run)

The rule (provenance-discipline 2.32, What a Visitor Reads, principle
1): the open copy's address goes on the row's `# Source:` line itself,
as an https address a visitor can open: a DOI as `https://doi.org/...`,
a bibcode as its ADS page; the `# Access:` line alone does not reach
the panel. The export carries the Source line word for word; the
gallery's Config mirror writes it into `data/objects_config.json` at
the Daily Run; the panel prints it as a link.

For each of the 39 works, in the order S1 to S16 then E1 to E23:

1. Find its rows in `constants_new.py` (one work can sit on several
   rows; the Sun's 16 works are 43 served citations, Earth's 23 are 29,
   measured at ca5339fd). `data/constants_export.json` says which rows
   are served.
2. Open the address the worksheet gives. Prefer, in order (The Access
   Standard): the publisher's open page or the DOI when it resolves to
   an open copy; arXiv; ADS; an agency page. A ResearchGate address is
   a last resort and usually refuses automated readers: try the DOI or
   the repository copy the worksheet also names (NTRS, NORA, PMC,
   Caltech, NOAA, JPL, IERS, IAU) first.
3. Confirm the title and authors as printed, and that the page says
   what the row cites it for. Where the worksheet corrected us, check
   the correction on the page before adopting it. Two are known:
   - E1: the 2020.0 north geomagnetic pole is in Table 3 of Alken et
     al. (2021), not Table 4 as our row says on its Source and Read
     lines (constants_new.py near line 1899; a Read line of
     2026-09-21 names Table 4, so two readers disagree; the page
     decides). Gemini's claim, not yet confirmed: the publisher's page
     rate-limited the coordination session.
   - E20: Gemini says Slavin et al. (1983)'s printed authors are
     Slavin, Tsurutani, Smith, Jones and Sibeck. Our row (near line
     2327) already names exactly those five, and already carries the
     NTRS address on its Source line. So nothing to correct; confirm
     on the page and move on. (The row's Access line says the Wiley
     pages are walled; the NTRS abstract is the copy opened.)
   - S12: the Roche zone is section 4.8 of Murray and Dermott, not
     4.6 (from the book's contents page; the chapter text is not open,
     so the row's section number changes and its access state is
     recorded honestly).
4. Write the address onto the Source line, and a `# Read:` line naming
   the place, the date and this session's model, with Gemini's leg
   named too where its quote matched the page (the Slice Relay: "that
   row's `# Read:` line names both readers").
5. Where no copy opens: leave the row as it is, record the work in the
   review file under "did not open", and it goes on TONY'S READING
   LIST (below) and, where even an address is unknown, to the GPT
   prompt (section 4). Do not write an address nobody opened (never
   build an address from memory; A `# Source:` over recalled data).

Tony's reading list (Tony, 2026-10-21: "if all else fails I can try to
open the papers myself and save them in papers/"; the rule is The Read
Field's second branch, provenance-discipline 2.32): one file,
`documentation/READING_L456_tony_<date>.md`, one row per work that
refused the session: the address to try, what to look for in it (the
section, table or sentence), and the number or wording the row expects.
He opens each in his browser, saves the PDF into the orrery's `papers/`
(gitignored; Murray (1989) is already there as
`1989A&A...218..325M.pdf`), and the next session reads it through the
device mount and writes the `# Read:` line with his name and date as
the reader. ADS pages, Wiley abstracts and ResearchGate are the usual
cases. The list is a file he opens at his machine, never a list in
chat.

Known hard cases, so they are not a surprise:
- S8, Murray (1989): ADS blocks automated readers. Tony's scan is in
  `papers/`; read it through the device mount; the row's address is
  the ADS abstract page
  (`https://ui.adsabs.harvard.edu/abs/1989A&A...218..325M/abstract`),
  which the row may carry once the paper has been read from the scan,
  since what was opened is the paper itself.
- S9, Hipparcos (ESA SP-1200): the volume PDF is open; section 1.5.3
  is on p. 91. If the PDF is too large to read whole, read that page
  range only.
- E5, PREM: the 1981 paper is walled; the Caltech record carries the
  abstract and the tabulation is open at GFZ and SOEST. The row keeps
  its citation and gains the open tabulation's address as the copy
  opened (The Access Standard: re-home to an accessible authority
  carrying the same result).
- E10, E11, E19, E22: the journal copies are walled. Gemini leaned on
  secondary papers (a 2010 precursor by the same authors; Nishida
  2000; Sibeck and Lin 2014). A secondary paper is not the work cited:
  if the primary does not open, the row's citation either moves to an
  open work that states the value (re-homing), or the row stays
  without an address and goes to GPT. Say which in the review.
- Six of Gemini's DOIs are wrapped in Google redirect addresses
  (`https://www.google.com/url?...q=https://doi.org/...`). Use the
  bare DOI from the worksheet's URL block.

Then: the orrery maintenance run (the constants export rewrites; the
gate stays 0 Tier-1 on the gate path, whole tree 280, and the patch
predicts the CHANGE, not the total); commit, push. The Daily Run's
Config mirror carries the addresses to the website; the "Source list"
check prints each feature's count of citations and links, which should
rise from 22 of 43 (Sun) and 9 of 29 (Earth) toward the full counts.
Tony's look: the Sun room and the Earth room, the i panel, tap a
link in each, including the inner core's Dziewonski and Anderson.

The review file: `documentation/REVIEW_L456_gemini4_worksheets_20261021.md`,
one section per worksheet: rows confirmed on re-opening, rows
corrected, rows that did not open, and how each return did against
the rules, the Earth return's failed pre-flight first.

## 4. Job 3: the GPT prompt for what did not open

Only after job 2, and only for the works that did not open AND whose
address is itself unknown (a work Tony can open from a known address
goes on his reading list instead, which is cheaper than a relay). Build it
from the ORIGINAL prompt rows
(`documentation/prompts/RELAY_L456_gemini_addresses_earth_20261020.md`
and the Sun's), not from Gemini's answers: legs are independent, or
they are one leg. Same shape as the Gemini prompts (the Slice Relay's
fixed shape), with a FRESH pre-flight page, not arXiv:2202.11533,
which both Gemini runs have now seen; pick any open arXiv abstract the
session opened itself today. Highest tier. Saved to
`documentation/prompts/RELAY_L456_gpt_addresses_<date>.md` for Tony to
carry. If every work opened in job 2, say so and skip this job.

## 5. Job 4: the drawer order (gallery; interactive-exhibit 1.19)

Tony's ruling, 2026-10-20 (his run record, the session of 10-20, and
in chat): in every room, each shell takes its place in the drawer at
the distance where it begins; "basically when we reach that shell's
distance, that is its place in the order." The Sun first, the order
listed for him to look at before it ships. Opus's reading of the Sun's
order by lower edge, to check against the served rows: chromosphere,
corona, Roche limit, zodiacal dust cloud, Alfven surface (the corona's
row took the streamer belt's old place at the top when the belt
joined it on 2026-10-20; that is what Tony saw).

This is method (the same answer next month for another room), so it
goes into interactive-exhibit as one rule at 1.19, one session one
bump, with its protocol entry (v3.107) and the manifest run. Confirm
the loaded copy reads 1.18 before touching the skill. The build reads
each room's drawer order from its rows' lower edges rather than from a
hand list, so a new shell lands in place by itself; the headless room
checks (tools/headless) assert the order per room.

If job 2 fills the evening, job 4 waits for the next session; say so
in the handoff.

## 6. Job 5, only if time remains: the Sun's fourteen pairs (L-191)

Tony's item, from the Fable coordination session of 10-20, with
Opus's correction carried in: the fourteen Sun shells in
`solar_visualization_shells.py` each have an `_info` string (the
checkbox tooltip) and an `_info_hover` string (the plot hover). At
fcd191e9, FIVE pairs differ in content (gravitational influence, Roche
limit, Alfven surface, corona, zodiacal dust; the last two on purpose,
the tooltip adding the panel's words), and NINE are byte-identical
(outer Oort, inner Oort, inner Oort limit, solar wind, termination
shock, chromosphere, photosphere, radiative zone, core). For the five,
show Tony the two texts side by side with the breaks stripped; he
picks the survivor, the default being the copy that prints from rows.
Then one string per shell, written in newlines, the twin deleted,
`<br>` derived at the Plotly boundary with `.replace('\n', '<br>')` as
the gas-giant configs already do; the Tk backstop in CreateToolTip
stays. The nine: keep one copy, delete the other, proved byte for
byte. Tony's look: each shell's tooltip and its plot hover, the same
words. The other 39 strings stay with their rooms.

## 7. Not this session

- The two Earth questions still open for a talk (L-375's website
  cone; L-454's device for edges that move) and the "method or
  Tony's?" question on reading an unsourced agency page one layer
  down. A talk session, not this one.
- L-459 (the monthly run) and L-266's link check: their own build.
- L-458 (the "report a problem" link): its own build, after its words
  list.

## 8. At the close

- Handoff `HANDOFF_L456_addresses_build_<date>.md`: what was built
  (verified, not claimed), the run order for Tony, the counts of
  citations with links before and after, by room, and which works are
  still without an address, by name.
- The review file (section 3).
- The close patch: ledger lines on L-456 (the addresses, by room,
  with the count), L-266 (nothing), L-363 or the drawer item (if job 4
  ran), L-191 (if job 5 ran); Where We Are by section; the skill bump
  and protocol entry if job 4 ran.
- Skill obligations that travel: interactive-exhibit 1.19 if bumped.
- "Where this leaves us", two or three lines in Where We Are's words.

Brief written October 21, 2026 with Anthropic's Claude Fable 5.1.
