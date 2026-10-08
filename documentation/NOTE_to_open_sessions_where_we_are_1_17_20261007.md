<!-- Doc-Kind: hand | Relay note, October 7, 2026: tells the open Opus sessions that ledger-and-session-records went to 1.17 and how Where We Are is now edited. Paste into each session. -->
# Note to an open session: Where We Are has changed, and so has the ledger skill

Built on orrery 8653ef1b at https://github.com/tonylquintanilla/palomas_orrery,
by the Fable 5.1 ledger-sweep session. Pushed at: the SHA Tony gives
you with this note, or read it yourself with `git ls-remote`.

## What changed, in one paragraph

Tony's page, `documentation/WHERE_WE_ARE.md`, has a new shape, and the
rules for editing it are in ledger-and-session-records **1.17** (L-422).
The copy of that skill loaded in your conversation is older; a reinstall
is not visible to a running session, so do NOT wait for one. Read
`skills/ledger-and-session-records/SKILL.md` from the repo at HEAD, the
section "Where We Are -- Tony's page", and work from that text. Check
first that HEAD's `PROJECT_INSTRUCTIONS.md` reads v3.85 and the skill
reads 1.17; if either does not, Tony has not pushed yet -- stop and say
so rather than building against the old page.

## The four rules your closing patch must follow

1. **Edit the page by section, at each section's own anchor.** Never
   rewrite the whole page. Two sessions closing the same day then each
   change their own lines. (patch_L418_2 rewrote it whole and erased the
   Horizons design session's lines; that is the founding case.)
2. **Nothing below the marker.** The page ends with the line
   `--- Your run record below this line`. Everything under it is
   Tony's run record. No patch touches it, and no anchor may sit in it.
3. **Every ledger handle on the page carries a short label in
   parentheses** -- "L-421 (the typed facts)", never a bare L-421. The
   same in your handoff and in chat.
4. **Each fact once.** The READ THIS FIRST box is the page. The
   sections are: the box; one line on the marks; The road; Settled;
   Signals; Waiting on you (design talk, decisions, not urgent); Where
   the details are; then the marker. There is no "Right now" and no
   "Next three steps" any more; what you would have put there goes in
   the box, once. Keep the lines above the marker under 130.

## Two things about your records

- Tony saves the page with his run record as a timestamped copy
  (`documentation/WHERE_WE_ARE_<m-d-yy>_<hhmm>_run_record.md`, flat in
  documentation/). Before your close writes the ledger, read his latest
  copy: his verdicts beside the test lines are the primary record, and
  you quote them from there, naming the copy, instead of re-pasting.
- An item inside an ordered list (the Sun's slice L-412, Earth's list
  L-413, and lists like them) needs no RICE score. Items outside a list
  keep RICE.

## Please read back

In your next reply to Tony, say which version line you read in
`skills/ledger-and-session-records/SKILL.md` at HEAD. A reply that
does not name it is telling him you did not read it.
