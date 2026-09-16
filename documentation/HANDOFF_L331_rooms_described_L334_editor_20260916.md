# The rooms say what they show, and the store gets an editor next

Built on orrery `bfc1706b8b0f14ce28cee893381ca3d511fea9ce`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `bbf46429df4cccb4b2e0b7305056684081c67334`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

The session opened at orrery `d99d8db1` and gallery `b375cfe1`. The
orrery moved once, to `bfc1706b` (skills, protocol, generators, ledger).
The gallery moved twice: `744ad578` (the Sun's four hovers to the panel)
and `bbf46429` (every Sun and Earth feature described). Every HEAD was
read back with `ls-remote`. After Tony runs this session's last ledger
patch the orrery moves again; that SHA is his to report.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-16, one session in two halves
Type: DOCUMENTATION + BUILD.
Handles: L-331 (two builds, Mode 5 passed), L-334 (opened), and from the
first half L-332, L-273, L-333 and five closures.
Supersedes `HANDOFF_ledger_review_L331_L332_20260916.md`'s STILL OPEN and
rollup; everything else in it stands.

---

## STEP 0 -- before you do anything

1. `git status --porcelain` in both repositories. Expect nothing.
2. `git ls-remote` both. Expect gallery `bbf46429` and the orrery at the
   SHA Tony reports after `patch_L331_3_ledger_20260916.py`.
3. Version-check every skill at load. This session installed
   interactive-exhibit **1.3** and orrery-coding-conventions **1.9** and
   cannot verify the install. Confirm the loaded copies read 1.3 and 1.9
   before exhibit or hover work; if they read 1.2 and 1.8, stop.
4. `ledger_index.py` after the ledger patch: one run, `OK: 329`.

---

## WHAT HAPPENED IN THE SECOND HALF

**Tony's Mode 5 of `744ad578` found the real gap.** The four Sun hovers
had reached the panel and lost their citations, and Tony read them and
said what every hover in both rooms had in common: a name, a number,
and nothing about what the thing is. "This is information we previously
had." It was -- in the orrery's `*_info` strings, which never crossed
into the gallery.

**The shape was ruled in one exchange.** A served `description` for the
hover and a served paragraph for the panel, both from the orrery's text,
which Tony had already approved: "just go to the patch directly."

**Built and shipped as `bbf46429`.** 32 features and the two belts,
condensed from the named orrery strings. The panel field is `about`
because `detail` already carries the magnetosphere's equations. The
belts, magnetopause and bow shock lost their project vocabulary on the
way -- the magnetopause had reached 18 lines and needed to give back
two. Tony, Mode 5, both rooms: "correct."

**One correction on the way, worth keeping.** A first draft moved the
belts' plane-and-tilt sentence out of the hover into the panel. The
Earth geometry suite failed: it pins that the tilt is quoted with its
model and epoch, and that the hover says the ring lies in the
equatorial plane. That is content, not vocabulary -- the tilt is quoted
BECAUSE it is served (L-231). The sentence went back, in plain words,
and the suite's regexes moved to the new phrases.

**L-334 opened.** Tony wants an editor over the served store, the way
Studio sits over the static gallery: hover text, panel text, links,
which shells draw on arrival, the arrival scale. The ledger item carries
five design questions for the conversation before the build.

---

## VERIFIED VS CLAIMED

Verified inside the session:

- Every patch on a throwaway copy of the pushed tree, refusing a second
  run. The gallery patch: five suites and the full offline maintenance
  run, 7 of 7, with the cache builder suite and the Artifact 1 pin;
  the renderers and the page's inline script parse; a read of the
  finished hovers and panel records for six features.
- The residue of L-331, counted in the built hovers at `bbf46429`:
  "served" in the rotation axis and the Moon; "trusted" and
  "osculating" in the Moon; "FROZEN" in the terminator. All in
  `earth_geometry.js` or `render_orbits.py`, outside the served store.
- Both SHAs read back after each push; the live run 8 of 8 SERVED.

Claimed and NOT verified here:

- Every render. Tony ran both rooms on his phone after `bbf46429` and
  reported "correct." His word is in L-331.
- The skill install (STEP 0, item 3).

---

## THE LESSON

**Measure the whole set before describing the gap.** Tony reported four
hovers with no description. Building all of them and reading them
showed it was every hover in both rooms, and that the fix was a served
field rather than four sentences. The same move the morning made with
the ledger -- print every open item's Gap and check it -- applied to
the hovers: enumerate, then decide.

**A pin on wording is a pin on content in disguise, or it is noise.**
The geometry suite's regexes looked like they were protecting a phrase.
They were protecting a served number and a caveat about a plane. Read
what a failing pin is FOR before rewording past it; two of the three
here were content and stayed, the third was vocabulary and moved.

---

## STILL OPEN, in the order Claude would take them

1. **L-334, the editor** -- Tony's stated next need, and it changes who
   can maintain the rooms. Start with the five design questions in the
   ledger item, not with code. Question 1 (numbers locked) decides the
   shape of everything else. Claude's view: yes, build it now; the
   rooms are done and the store is stable.
2. **L-322, the unit field** -- the Store drift check prints FAIL on
   every live run because 13 pointers cannot be examined. Report-only,
   so nothing stops, but a red line nobody reads is a check that cannot
   fail. Clearing it makes drift a gate. Also what the editor's locked
   numbers would display.
3. **L-333** -- Tony decides: restamp both plan companions, or retire
   the critical-path one.
4. **L-331's residue** -- the four page-built hovers and the Moon's;
   whether they get a served `description` too (then L-334 reaches
   them). Cheap once L-334's shape is settled.
5. **Carried:** L-330 (the belts' shape), L-231 (Jupiter's room and its
   belt builder), L-273's gallery half, L-061, L-316/L-318 closures.

---

## TONY-ACTION ROLLUP

1. **(do)** ORRERY: run `patch_L331_3_ledger_20260916.py`, then
   `python ledger_index.py LEDGER_CONSOLIDATED.md` (expect OK: 329);
   commit, push, report the SHA. The maintenance run archives the
   patch itself.
2. **(do)** File this handoff to the orrery's `documentation/`. In the
   gallery, archive `patch_L331_1_sun_hovers_to_panel.py` and
   `patch_L331_2_what_you_are_looking_at.py` to `documentation/`.
3. **(decide)** L-334, question 1: are the numbers locked in the editor?
   Then questions 2 to 5, at the start of the next session.
4. **(decide)** L-333: restamp or retire.
5. **(decide)** Close L-318. Close L-316 after the desktop title and
   cross are looked at on their own.

---

Session written September 2026 with Anthropic's Claude Opus 5.
