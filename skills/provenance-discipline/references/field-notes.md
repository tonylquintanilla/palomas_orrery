# Field Notes (provenance-discipline reference)

Lessons, not rules. Opened from provenance-discipline when a scanner
count or an audit result surprises you, or before reporting a value as
unverified. Moved here from provenance-discipline 2.26 on 2026-10-08
(L-418), word for word.

## Field Notes

- **A missing annotation is not missing verification.** The absence of a
  `# Cross-checked:` line means no ANNOTATION. It does not mean no work.
  Verification lands in several places the annotation grammar does not
  count: a `Resolved:` leg naming the returned verdict that caused an
  edit, a `Record:` leg pointing at a source record in `documentation/`,
  a `Review-note:` block carrying an independent read, and a convergence
  report filed after a dispatch. A row can carry all four and still show
  no cross-check. Before reporting a value as unverified, read the
  block's other legs and look for its source record. Say which claim is
  being made -- "carries no cross-check annotation" and "has not been
  verified" are different statements, and the first said carelessly is
  heard as the second. (Origin, 2026-08-27: a session reported seven of
  the Sun's constants as lacking cross-checks in a way that read as
  unverified. Two of the seven were the most-worked rows in the file --
  `ALFVEN_SURFACE_RADII` had a three-model pilot dispatch behind it, and
  `HELMET_CUSP_RADII` rested on a paper Tony retrieved from NASA ADS
  himself. The annotations were absent because the earlier legs had been
  correctly stripped, which is A Cross-Check Retires working, not a gap.)

- **An evidence artifact is filed AS RECEIVED.** House style -- ASCII
  rules, naming conventions, header blocks -- applies to code and to
  documents we author. It does NOT apply to a document whose entire value
  is that someone else wrote it. A session took Tony's uploaded Gemini
  worksheet, converted its LaTeX to ASCII, stripped the markdown escaping,
  added a header block and a provenance note it wrote itself, and filed
  the result labelled as the Gemini worksheet. Tony caught it: "you have
  created a parallel unsourced worksheet not made by gemini." The corpus
  settled the question -- the existing GPT worksheet carries 115
  non-ASCII bytes and the earlier Gemini one 37, so there was no
  consistency to fix, only an assumed one. Reformatting an evidence file
  destroys the property that makes it evidence.
- **Unverified and true is still unverified -- do not over-confess.** Asked
  whether it had fabricated a `(Gemini worksheet)` annotation, a session
  gave an accurate account of its method (it had pattern-matched an
  adjacent annotation's shape without checking), then concluded from that
  the CONTENT was fabricated, called it cite-to-clear, and offered to
  strip the annotation. The recovered worksheet proved all three
  specifics it believed it had invented were true. Acting on the
  self-report would have deleted a real citation. Separate the two
  findings: the METHOD was wrong and is worth fixing; whether the CONTENT
  is wrong is a different question with its own evidence. An
  over-confession is as much a calibration failure as a denial, and it is
  more persuasive because it sounds like rigor.
- **Three wrong-paper citations survived into Batch 1 files**, each
  plausible enough to pass a reading. Mercury's crust cited "Pei" -- a
  mis-parsed GIVEN name read as a surname, so the author did not exist.
  Mercury's crust cited Sori 2018 for 35 km when Sori 2018 gives 26 --
  the cited paper REFUTED the value it was cited for. Eris's core cited
  Glein et al. for 875 K; Glein is a real author of a real paper on
  methane isotope geochemistry, but that paper does not contain 875 K,
  which comes from a different 2023 Science Advances paper. Three
  distinct ways to be wrong while looking right: a name that is not a
  name, a source that contradicts you, and a real author cited for
  someone else's number.
- A citation can be self-contradictory and still read as authoritative.
  Saturn's Hill sphere carries `# Source: ... ~91 million km / ~151
  Saturn radii confirmed` -- but 91 Mkm is ~1,510 R_S, so the two halves
  of the "confirmed" pair are a factor of ten apart, and neither matches
  the drawn value. The word "confirmed" over an internally inconsistent
  pair is cite-to-clear caught in the wild.
- **Verify the anchor SHA exists before trusting a document built on it.**
  An outbound prompt arrived anchored to a commit that was not in the
  repo -- it had been written but not pushed. The "does not exist"
  reading was correct at the moment of the check and resolved on push:
  the SHA round trip working exactly as designed, with the one failure
  mode honest and visible. Two repos in play makes this routine rather
  than exotic -- a HEAD that looks wrong may be the OTHER repo's HEAD.
  Check both before concluding anything.

- The scanner took ~10 sessions and multiple Gemini cross-checks to
  harden -- treat scanner changes as shared-CI changes with family-wide
  ripple (extending the unit vocabulary once exposed a pre-existing
  Tier-1 in star_notes.py that had been invisible).
- Fingerprint truncation was a prior scanner bug (fixed); if suppression
  behaves oddly, check fingerprints before assuming a data problem.
- Naive sums of source files can contradict the source's own published
  totals (overlapping units double-count). Transcribe headline figures;
  never compute them from parts unless the source says the parts sum.
  The full discipline for human-cost data is in earth-system-pipeline.
- Derive from known quantities; don't estimate manually.
- **The scanner scans itself, so editing provenance_scanner.py nudges its
  own self-scan numbers.** Adding a new module-level dict or descriptive
  string constant to the scanner (e.g. MODULE_DOMAIN_MAP, DOMAIN_LABELS)
  gets picked up as a claim-shaped unit in provenance_scanner.py's own
  audit entry, same as in any other file. This is correct behavior, not a
  bug -- but before assuming a total-findings delta after a scanner change
  means a real citation gap appeared somewhere in the project, check
  whether the scanner's own new code is the source of the delta first.
  (Observed July 2026: a report-formatting-only change to
  provenance_scanner.py shifted its total findings by +2, both new,
  correctly landing in the no-action tiers -- verified by diffing the
  before/after audit line by line, not by trusting the summary count.)
- **Multiple copies of PROVENANCE_AUDIT.md can exist and silently
  diverge -- verify which one you're reading.** The committed root-level
  file can go stale relative to a fresh scan (a small drift was observed
  directly: a committed doc claimed a different Tier-1 count than an
  immediate live re-run). Separately, an archived copy can sit elsewhere
  in the repo (e.g. under documentation/) dated months earlier. `cd`-ing
  into a subdirectory mid-session and not verifying `pwd` before reading
  "PROVENANCE_AUDIT.md" again is enough to silently read the wrong copy
  and draw a confidently wrong conclusion from it -- a real, self-caught
  near-miss this session. When precision matters (triage, before-citing
  a count), prefer a fresh live scan over any committed copy, and confirm
  the working directory before reading a same-named file a second time.
