<!-- Doc-Kind: hand | Coordination note: Tony's ruling of Oct 24 on L-482 (every room's top-bar button is Reset, and no room has a See more), from a talk-only session; closes the design question standing before slice 2. -->
# Coordination note: one Reset button in every room, and no See more anywhere

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 24, 2026

Built on orrery 206f96c988569496d9cf12b9e3e45d73e61132d4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 96173b88e4da9661fcfe3a389a96c6bab19b60cc at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote on the afternoon of Oct 24. The
session's close patch, `patch_L481_3_session_close_20261024.py`, was
dry-run against these same bytes in this session and applied cleanly
(two files edited, one new, Where We Are at 128 lines above the marker);
it is not yet run on Tony's machine, so the ledger at HEAD still shows
L-481 open and L-482 on the design-talk list.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION NOTE (zero code). Answers L-482 (whether the Sun and
Earth rooms' All / none becomes Reset too). Companion to
`DESIGN_L477_drawer_and_view_rulings_20261024.md` (the Solar System
room's ruling this one extends) and `HANDOFF_L481_session_close_20261024.md`
(which lists L-482 as the open question before slice 2).

## Tony's ruling, Oct 24, 15:26

Asked whether the Sun and Earth rooms' All / none should become Reset
as well: "Yes all rooms should use the same Reset button and no 'see
more'."

## What that means against the code at gallery 96173b8

- **See more.** Already true everywhere. Only the Solar System room
  ever had a See more / See fewer; L-477's build removed it (Tony, Oct
  24: "No 'see more' Let that be permanent"). The Sun and Earth rooms
  list their shells in one list with no hidden rows
  (`renderSunDrawer`, interactive.html near line 5018). Nothing to
  build for this half; the build session confirms it by reading, not
  by assuming, and the skill records the rule as applying to every room.
- **The button.** The top bar's one button is `#sun-drawer-all`
  (interactive.html line 1269). It reads Reset only when a room hands
  served rows to the drawer, which is the Solar System room
  (interactive.html near line 3637: "L-477: there the top bar's button
  is Reset, not All / none"). In the Sun and Earth rooms it still reads
  All / none and ticks or unticks every shell. Under this ruling it
  reads Reset in every room and does one thing: puts the room back as
  it opened.
- **What "as it opened" is, per room.** The Sun and Earth rooms open on
  their arrival block (interactive-exhibit, what a room opens on); the
  Solar System room's Reset already puts back what the room opened on
  (L-477). So Reset is one behaviour with one definition, the arrival
  state, read from the same place the room read it at boot. The build
  does not invent a second definition for the shell rooms.
- **Any other room with the shared chrome** (the Explorer, if it shows
  the button) follows the same rule: the ruling says all rooms. The
  build session checks which rooms render `#sun-drawer-all` and makes
  every one read Reset.

## What the next session does with it

1. Its records patch closes L-482 with the ruling above, in Tony's
   words, and takes it off Where We Are's design-talk list. That list
   then holds L-461 (pull matches push; already ruled "build with slice
   2") and L-465 (the Sun axis hover reading its period and tilt from
   the served rows; a small orrery build with no open question). Neither
   needs a talk, so nothing stands before slice 2.
2. The build, in the shared chrome: one button, Reset, every room; both
   shell rooms walked headlessly (tools/headless) and on the phone, as
   L-482's own Gap asks. interactive-exhibit fires (its loaded copy must
   read 1.22; the rule itself rides the skill's next bump, with slice 2,
   under One Session, One Bump). Small enough to ride in slice 2's
   website patch, or go first as its own; the build session's call.
3. Then slice 2, by `DESIGN_L443_slice2_rulings_20261023.md`.

## Tony-action rollup

- **(do)** When back at the machine, in this order: the close patch
  `patch_L481_3_session_close_20261024.py`, then `ledger_index.py`,
  move the patch to documentation/, commit and push with the updated
  run-record copy `WHERE_WE_ARE_10-24-26_1140_run_record.md`. Save this
  note in the orrery's documentation/ folder in the same commit.
- **(decide)** Nothing further. L-482 is ruled.

Written October 24, 2026 with Anthropic's Claude Fable 5.1.
