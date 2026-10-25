<!-- Doc-Kind: hand | Coordination note: Tony's rulings of Oct 24, evening, on the four decisions in the slice 2 words draft (L-443, L-470), recorded as they are made, before the next records patch. -->
# Coordination note: the four decisions in the slice 2 words

Tony Quintanilla, PE | Claude Opus 5.5 | October 24, 2026, evening

Built on orrery 206f96c988569496d9cf12b9e3e45d73e61132d4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 96173b88e4da9661fcfe3a389a96c6bab19b60cc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION NOTE (zero code). The decisions are those of
`WORDS_L443_slice2_draft_20261024.md` ("Four decisions"), put to Tony in
chat one at a time. The next records patch carries them into the ledger.

## 1. C/2025 K1's record (L-470)

The orrery's entry asks for record 90004912, which JPL has given to
another comet, PANSTARRS (C/2025 B1), so the orrery draws the wrong comet
today. The comet's newest fit is 90004925. Its designation returns four
records (the comet and its pieces B, C, D). Asked as DES=1004075 (JPL's
permanent number for the comet), JPL returned exactly that newest fit
(`CHECK_L443_slice2_sources_20261024.md`, section C).

Tony, Oct 24, 17:15: "B and what do we do with the pieces. We normally
used a record number only when the id did not work as intended maybe
because of the pieces?"

- Ruled: B, ask by JPL's permanent number, 1004075.
- The pieces need nothing: each entry asks by its own designation
  (C/2025 K1-B, -C, -D), and each returns one record, the right one.
  Their comments carry old record numbers (B's "Rec #90004913") and
  are corrected in the same orrery patch.
- Why a record number was pinned: after the break-up the designation
  returned four records, so the entry was switched to a record number
  (the designation line is still there, commented out).
- For horizons-orbital-mechanics, Which Record Serves a Body: a comet
  whose designation also matches its own pieces is asked by JPL's
  permanent number for it.

## 2. BepiColombo's arrival date

ESA's pages: "late 2025" (its science site, out of date); "December
2026" (its mission page); "will enter orbit around Mercury on 21
November 2026" and "MPO and Mio will separate from each other on 9-10
December 2026" (its arrival news, updated 3 September 2026). A dated
sentence goes stale after November 21.

Tony, Oct 24, 17:20: "B for Bepi Colombo."

- Ruled: no date in the description: "launched in October 2018 to study
  Mercury from orbit." The drawn path carries the timing.

## 2a. A room for C/2025 K1 and its pieces (new idea)

Tony, Oct 24, 17:20: "And for the comet can we create our first comet
room for its pieces?"

- It fits the room rule of Oct 22 (a room is for a body with more than
  its symbol). A new ledger item in the next records patch; a design talk
  before code; proposed after slice 2 draws the comets, since the room
  needs each piece's path.

## 3. Juno's planned part

Tony, Oct 24, evening: "Confirmed in Juno."

- Ruled: Juno is drawn by ruling 6 of
  `DESIGN_L443_slice2_rulings_20261023.md`, to where JPL's data ends
  (2028-SEP-02), solid to today and dashed after. The description says
  nothing about when the mission ends.

## 4. The word "Hyperbolic"

(to come)

## 5. How the orrery handles C/2025 K1 and its pieces

Tony, Oct 24, evening: "As to the comet and its pieces, how does the
orrery handle this? Does it need an update?"

Read in `celestial_objects.py`, `palomas_orrery.py`,
`orbital_param_viz.py`, `orbital_period.py` and `test_orbit_markers.py`
at 206f96c. The orrery has four entries, the comet and pieces B, C, D,
each with its own checkbox; the pieces sit indented under the comet.

It needs an update, in the next orrery patch:
- The comet: asked for record 90004912 (now PANSTARRS, C/2025 B1).
  Changed to 1004075, asked as DES=1004075; (decision 1).
- `orbital_period._is_small_body` and its test in
  `test_orbit_markers.py` name 90004912 as the reason a record number
  counts as a small body. Both move to the new id; the test is rerun.
- The pieces: asked by designation, and right. Their comments name old
  record numbers (90004913 is now Borisov, C/2025 B2); corrected to
  90004926, 90004927, 90004928.
- Words removed, by the rule that an unsourced claim comes out: the
  break-up "~Oct 16" and "Icarus Feb 2026" (NASA says about a month
  after perihelion, images of Nov 8 to 10; STScI gives no date); "This
  record is Fragment A ... same SPK-ID" (no page or record says so);
  piece C "still bound" and "Return period ~13 million years" (JPL gives
  e = 0.999994 with sigma 3.1e-05, which cannot tell bound from
  escaping). The checkbox's "Fragment C (bound! e=0.99999)" goes with
  them. The theskylive links fail; replaced by the NASA page.
- Kept: the fixed 0.33 AU perihelion in the view-scaling special cases
  (`palomas_orrery.py`, `orbital_param_viz.py`). JPL gives QR =
  0.33421 AU; the special case is keyed on the name, which does not
  change.

## 6. The orrery's date list matches the website

Tony, Oct 24, 17:26: "And the orrery's object list for served windows
should be updated to match the website."

- Read as: the dates beside each spacecraft and comet in the orrery's
  object list, and the windows the orrery fetches, are the ones the
  website serves: a spacecraft's JPL span read from its refusals; a
  comet's window by the ruling of
  `COORD_L443_comet_span_ruling_20261024.md`.
- Today they are typed by hand, 51 labels, and several are stale
  against JPL's spans read today: Juno 2028-9-30 (JPL 2028-09-02),
  Psyche 2029-06-26 (2029-02-11), New Horizons 2029-12-31 (2050-01-01),
  Europa Clipper 2031-02-07 (2034-09-03), BepiColombo 2027-4-7
  (2027-04-11), Parker 2029-1-31 (2030-01-01), OSIRIS APEX 2030-3-1
  (2030-03-22), C/2025 K1 2025-04-08 to 2029-12-31.
- By method, the orrery reads them from the same plan the website uses
  (`data/path_plans.json`), not a second typed copy, so they cannot go
  stale again. It is L-476's work, after build B, which writes the
  plans the orrery would read.

Written October 24, 2026 with Anthropic's Claude Opus 5.5.
