<!-- Doc-Kind: hand | Starting brief for the build session that runs the Oct 24 close patch, builds the L-482 Reset fix, and builds slice 2 of L-443. Tony opens the session with one line: read this file and start here. -->
# Starting brief: run the close, fix Reset in every room, build slice 2

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 24, 2026

Built on orrery 206f96c988569496d9cf12b9e3e45d73e61132d4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 96173b88e4da9661fcfe3a389a96c6bab19b60cc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote on the afternoon of Oct 24.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a BUILD SESSION. Written by a coordinating session that
changed no code. Tony was away from his machine when it was written, so
one records step is still owed and this brief begins with it.

## 0. Before anything: the state you are starting from

Three files are on Tony's machine and not yet in the repo. A session
linked to his computer reads them from his folders; an unlinked one
cannot see them and must ask Tony to attach them.

1. `patch_L481_3_session_close_20261024.py`, in the orrery ROOT folder,
   unrun. It is the close of the Oct 24 drawer-and-view session: it
   closes L-481 (readability) on Tony's look, re-homes three skill
   descriptions to L-443, and rewrites Where We Are. It was dry-run
   against the repo at 206f96c by the coordinating session and applied
   cleanly (two files edited, one new, the page at 128 lines above the
   run-record marker). Not slice 1's close; slice 1 closed on Oct 22.
2. `documentation/WHERE_WE_ARE_10-24-26_1140_run_record.md`, updated at
   2:27 pm on Oct 24 with Tony's afternoon look. The repo holds only
   its morning version. The ledger, once the close patch runs, quotes
   the afternoon's lines from it.
3. `documentation/COORD_L482_reset_all_rooms_20261024.md`, Tony's ruling
   on L-482 (section 2 below).

So the first check is: `git ls-remote` both repos. If the orrery is still
at 206f96c, the close has not been pushed. Then, before any build, hand
Tony the close in his order: open `patch_L481_3_session_close_20261024.py`
in VS Code and click Run (it asks nothing); run `ledger_index.py` (it
moves L-481 to the closed archive); move the patch to `documentation\`;
commit and push, with the run-record copy and the L-482 note in the same
commit. Read back the new SHA. Build on that, not on 206f96c. If the
orrery is already past 206f96c, read the close note
`documentation/HANDOFF_L481_session_close_20261024.md` and carry on.

Confirm the loaded interactive-exhibit reads 1.22 before any exhibit
work. Protocol v3.110 wrote that obligation; the session that bumped it
could not see its own reinstall.

Then read, in this order: `documentation/WHERE_WE_ARE.md`; the run
record copy above; the close note; the L-482 note; and
`documentation/DESIGN_L443_slice2_rulings_20261023.md`, the slice 2
design record. Slice 2 is designed. Its seven rulings are Tony's and
are not reopened here.

## 1. The ledger's open items this session touches

- L-443 (the objects to the website): slice 2 is its next slice. Its
  Gap, after the close patch: "slice 2's build, by
  DESIGN_L443_slice2_rulings_20261023.md, after the next design talk
  (L-482, L-461, L-465)." That talk has happened; see section 2. L-443
  also carries, parked from L-481, three descriptions for
  interactive-exhibit's next version (section 4).
- L-482 (whether the Sun and Earth rooms' All / none becomes Reset too):
  ruled, section 2.
- L-461 (pull matches push: the Daily Run checks that the orrery it
  pulled is the one Tony pushed): ruled "build with slice 2."
- L-465 (the Sun's axis): the orrery's own Sun-axis hover still types
  its rotation period and tilt; reading them from the served rows
  changes its words. A small orrery fix with no open question.

## 2. Build one, small: Reset in every room (L-482)

Tony's ruling, Oct 24, 15:26: "Yes all rooms should use the same Reset
button and no 'see more'."

What that means at gallery 96173b8 (from the L-482 note, which has the
line numbers): no room has a See more any more, so that half is already
true and the build only confirms it by reading. The top bar's one
button, `#sun-drawer-all`, reads Reset only in the Solar System room
(interactive.html near line 3637); in the Sun and Earth rooms it still
reads All / none and ticks or unticks every shell. Under the ruling it
reads Reset in every room that renders it, and does one thing: puts the
room back as it opened, its arrival state, read from the same place the
room read it at boot. One definition, not two. Walk both shell rooms
headlessly (tools/headless) and on the phone, as L-482's Gap asks.

Ride it in slice 2's website patch or deliver it first on its own: the
builder's call. Say which, and why, in one sentence.

## 3. Build two: slice 2 of L-443

By `DESIGN_L443_slice2_rulings_20261023.md`: the twelve spacecraft still
flying among the planets, and the fourteen comets on open or barely
closed paths, each drawn solid up to today and dashed after, by the one
path rule planned in the orrery. The design record's section 3 says
what the build decides by method; its section 2 names what was measured.

Build L-461 with it, as ruled: the Daily Run checks that the orrery it
pulled is the one Tony pushed.

L-476 (the orrery's own whole-path plots drawing by the same plan,
dashed after today) comes AFTER slice 2, by the Oct 23 design; it is
not this session's unless the design record says otherwise.

L-465 is a small orrery fix. If this session opens an orrery patch for
other reasons, include it and say so; if not, leave it on Where We Are's
list and say so. Do not open an orrery patch only for it.

## 4. The skill bump that rides with slice 2

Slice 2 bumps interactive-exhibit (1.22 -> 1.23). One Session, One Bump:
everything this session decides about that skill rides the one number.
It carries, besides slice 2's own conventions:

- the three descriptions parked on L-443 from L-481 (closed Oct 24): in
  the Solar System room each hover line after the name is a bullet,
  written `&#8226;` because Plotly 2.35.2 converts only eight named
  entities; every source line naming JPL Horizons carries
  https://ssd.jpl.nasa.gov/horizons/, which the i panel makes a link;
  each room's closing paragraph is a bulleted list, "the creator's
  daughter";
- the L-482 rule: one Reset button in every room, no See more in any.

The four steps travel in one commit: the version line, `skills_index.py`,
the protocol's version-history entry (v3.111, pushing v3.108 down into
`documentation/PROJECT_INSTRUCTIONS_HISTORY.md`), and the commit of all
three together. The session cannot verify its own reinstall; write the
obligation into the close for the next session to discharge.

## 5. How Tony wants the session run

- Plain speech in chat; one ask per message; project terms glossed on
  first use (the protocol's Register Rule).
- When the session is linked to his computer, deliver a patch by
  placing it in the repository's root folder, under its proper name,
  not as a download. A delivered patch is final (L-471): never replace
  one once it is in his folder; an addition is the next numbered patch.
- Before any complete file or agentic code: the agentic-pre-test skill,
  on a throwaway copy. Before any patch: safe-file-editing.
- Tony runs patches from VS Code's Run button and pushes from GitHub
  Desktop. Give him the steps in that form, in order, and read each
  push back with git ls-remote before building on it.
- The close: the ledger, Where We Are (edited by section, at its
  anchors, under 130 lines above the marker), a handoff with the
  anchor, and his run-record copy read before the close writes
  anything. His verdicts there are the primary record.

## 6. Tony-action rollup

- **(do)** The close, section 0, in order, before any build.
- **(do)** The phone look of the L-482 change and of slice 2, from the
  checklists the session gives.
- **(decide)** Nothing is open for decision at the start. If the build
  meets a case the design record does not express, bring the case, not
  the question.

Written October 24, 2026 with Anthropic's Claude Fable 5.1.
