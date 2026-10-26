<!-- Doc-Kind: hand | Coordination note: Tony's ruling of Oct 26 that the orrery's stale "set manual scale" and "MB per frame" hover sentences come out as a class; the class counted by file at HEAD; what the build session must check first. Zero code. -->
# Coordination note: the stale manual-scale and file-size sentences come out, as a class

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 26, 2026

Built on orrery 5398439591f35979c4df1791e25477ac37119b01 at
https://github.com/tonylquintanilla/palomas_orrery (branch main); the
gallery is not touched (its HEAD at the time, 9223cd165422bf2616715e65ca59410b8245f9e5).
Read live with git ls-remote on the morning of Oct 26. No code was
changed in this session.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION NOTE (zero code). Opens a ledger item at the next
records patch (next free handle; L-490 was the newest minted on Oct 26
morning). Companion to provenance-discipline 2.34 (Uncited Goes to the
Ledger, Not the Bin; A patch predicts the scanner's change) and
orrery-coding-conventions 1.11 (the opening view: the farthest thing
drawn plus 20 percent).

## 1. What prompted it

Tony, Oct 26, 11:23: "we are near the end of the symbols slice and we
still have over 100 tier 1 in the orrery. Are these missing sources
really tier 1?"

Read from PROVENANCE_AUDIT.md at 5398439: the gate path reads 0 Tier-1
by name; the whole tree reads 276, orrery 112. Of the orrery's 112,
shell_configs.py holds 35 and idealized_orbits.py 24. Reading the
flagged lines, about eleven of shell_configs.py's 35 are not factual
claims at all but a number with a unit inside a stale instruction:
"SET MANUAL SCALE OF AT LEAST 0.05 AU TO VISUALIZE" and "2.4 MB PER
FRAME FOR HTML." The first kind is obsolete: since Tony's ruling of
Oct 18-19 (Settled on Where We Are) every orrery view opens on the
farthest thing drawn, shell or orbit, plus 20 percent, so nobody sets
a manual scale to see a shell. The second kind is a note about the
size of an exported animation frame, written for the author, not a
fact about a body.

## 2. Tony's ruling, Oct 26, 11:30

Asked whether the stale manual-scale and file-size sentences should
come out of the hovers as a class, in a small patch at the next
convenient session: "Yes."

The ruling is the removal of the two sentence classes from the
orrery's visitor-facing hover and info text. It is not a licence to
add them to provenance_exceptions.json: stale words are removed, not
excepted.

## 3. The class, counted by name at 5398439

Found by grep for "MANUAL SCALE" and "MB PER FRAME" in .py files
outside documentation/. The count is of LINES; a few lines carry two
sentences.

**Manual-scale instructions (about 110 lines).** By file:
info_dictionary.py 58; shell_configs.py 35; jupiter 5; earth, mercury,
neptune, saturn, uranus 4 each; asteroid_belt, eris, planet9, pluto 3
each; mars, venus 2 each; moon 1 (all *_visualization_shells.py).
Forms seen: "SET MANUAL SCALE TO AT LEAST n AU TO VISUALIZE", "USE
MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY", "SELECT MANUAL SCALE OF AT
LEAST n AU TO VISUALIZE", "***SET MANUAL SCALE TO n AU TO SEE ...***",
"**USE A MANUAL SCALE OF AT LEAST 1500 AU TO SEE THE FULL ORBIT**",
"***PLOT WITH MANUAL SCALE AT LEAST 4 AU***", and "Vizualize at a
manual scale of 0.005 AU."

**File-size notes (about 85 lines).** By file: shell_configs.py 26;
saturn, jupiter 8 each; neptune, uranus 7 each; pluto 6; eris 5;
asteroid_belt 4; planet9 2; info_dictionary.py 7 ("HTML VISUALIZATION
21.9 MB PER FRAME FOR ALL SHELLS AND MOONS", "HTML: ~22 MB per frame").

**Not in the class, and left alone:** code comments in
palomas_orrery.py (4), shared_utilities.py, spacecraft_encounters.py
and save_utils.py that discuss manual scale as a mode; the label
"Manual Scale (Light-Years):" in star_visualization_gui.py, which is a
control, not a hover; worksheet_checker.py's own pattern (line 997)
and test_worksheet_checker.py's fixture (lines 530-531), which exist
to recognise this class and must keep their sample text.

## 4. What the build session checks before editing (Claude's reading)

- **A sentence that carries both an instruction and curation.** Many
  info_dictionary.py lines say what to plot WITH, not only what scale
  to set: "SET MANUAL SCALE TO 170 AU TO PLOT THE COMPLETE TRAJECTORY.
  PLOT WITH JUPITER AND SATURN." The scale half is obsolete; the
  "plot with" half is the orrery's form of the website's companions
  rule (interactive-exhibit 1.25) and is curation worth keeping. The
  patch strips the scale words and keeps the companions where a line
  has both, or brings Tony the list of such lines if the split is not
  clean. Removing words a person wrote is his call where the words
  carry meaning (A Simple Error a Check Finds Is Fixed and Reported:
  "not simple").
- **Consumers of these strings.** save_utils.py line 145 says lines of
  the form "***SET MANUAL SCALE TO 170 AU...***" "are useful" to
  something; read what it does with them before removing them, and
  grep for any other code that keys on the asterisked form. Check All
  Parallel Pipelines applies: a string read by more than one consumer
  is edited once and every consumer is confirmed.
- **The hover still reads.** A removed sentence in the middle of a
  paragraph can leave a dangling "<br><br>" or a one-word line; the
  pre-test's render of a few shells is the check, with a before and
  after of one Pluto, one Venus and one spacecraft hover in the
  handoff.
- **The scanner's change, predicted by name, not by total.** The patch
  states which Tier-1 findings it expects to clear: those display
  strings whose only numeric claim was a removed sentence. A string
  that also holds a real claim ("about 10 to 30 kilometers") stays
  Tier-1 and is not this patch's business. The whole-tree total differs
  between machines; the names do not.
- **Encoding.** ASCII and LF, by safe-file-editing 1.14; some of these
  files have carried non-ASCII before.

## 5. Sequence

After slice 2's comets, as its own small orrery session: the
agentic-pre-test on a throwaway copy, one patch, the maintenance run,
Tony's look at three hovers in the orrery, commit and push. The ledger
item opened for it records the class by file (section 3) so the patch
can be checked against a list and not a count.

## 6. Tony-action rollup

- **(do)** Commit this note with your next push.
- **(do)** When the session runs: the patch, the maintenance run, a
  look at three hovers, push.
- **(decide)** Any line where the scale instruction and the
  "plot with" advice cannot be split cleanly: the session brings the
  list.

Written October 26, 2026 with Anthropic's Claude Fable 5.1.
