# HANDOFF -- Provenance Phase 1 (v17)
Tony Quintanilla, PE | Claude | May 30, 2026

SCOPE: This handoff covers PHASE 1 ONLY of the provenance plan -- factual
verification of Tier-1 items 36-39 + the Uranus tilt sign. It is NOT the full
plan and NOT the full shell-consolidation backlog. The remaining provenance
phases and all other open consolidation work from v16 are unaffected and still
live -- carry v16 forward for those. This document supersedes v16 only for the
four Phase 1 items (36-39) and the two pieces that spun out of them into the
deferred list (Artemis II redo, Uranus rendering cleanup). Everything else in
v16 stands.

Numbered "v17" for sequence continuity; the name is provenance-Phase-1, not a
new master handoff.

---

## SESSION SUMMARY

Phase 1 of the provenance plan: factual verification of Tier-1 items 36-39 +
Uranus tilt sign. web_search sourcing (fetched) + Gemini Mode 7 cross-check.

Outcome: 1 item closed (Neptune), 1 ready to apply (Uranus citation), 2 items
promoted to the deferred list because the right fix is larger than a citation:
Artemis II (redo presets, not patch prose) and Uranus rendering cleanup.

Key discovery: the Artemis II encounter dict fuses fetched and recalled data
behind misleading provenance tags. That moved it from "fix the string" to
"redo the presets from traceable sources" -- a new-session piece of work.

---

## PHASE 1 STATUS

### Item 36 -- Neptune magnetosphere -- CLOSED (Tony applied, Claude verified)
neptune_visualization_shells.py. `# Source:` comment added at lines 589-590,
immediately above `magnetosphere_text` (claim the audit flagged at line 590).
Inside the 30-line lookback, in the `# Source:` form the scanner recognizes.
Verified in the uploaded file (1719 -> 1722 lines, +3). Values were already
correct (47 deg, 0.55 R_N); the finding was a lookback false-negative -- the
real citation sat ~134 lines away at 455-456, outside the window, plus an
in-string "Source:" that the scanner does not count (wrong form).
ACTION REMAINING (Tony): re-run provenance_scanner.py locally with
data/provenance_exceptions.json; confirm the Neptune Tier-1 finding clears.

### Item 39 -- Uranus magnetosphere citation -- READY TO APPLY
uranus_visualization_shells.py. Same lookback issue as Neptune: claim at
line 515 is cited in-string (line 520) and in distant comments (440, 547),
but needs a `# Source:` comment within lookback of 515. Values correct.
Add immediately above the `description = (` block (~line 514):

    # Source: Ness et al. (1986) Science 233:85 -- Voyager 2 magnetometer.
    # Dipole-vs-rotation tilt: abstract states 60 deg; refined value commonly
    # cited ~59 deg (58.6 deg). Dipole offset 0.3 R_U (~1/3 radius). Axial tilt
    # 97.77 deg (NASA Uranus fact sheet). Sidereal rotation 17h 14m.

NOTE: this is citation-placement only and is independent of the 59/60
inconsistency, which is part of the deferred Uranus round (D-URANUS U1 below).
This citation can be applied now to clear the Tier-1 finding; the 59/60 value
decision happens in the render session. (If you prefer, defer this too and do
all Uranus edits in one session -- either is fine. Applying now closes the
audit item sooner.)

### Items 37, 38 -- Artemis II -- PROMOTED TO DEFERRED (see D-ARTEMIS)
Not patched. The prose fixes (Apr 7->6, FBC 11->8 km, splashdown Apr 11->10)
are correct, but the deeper problem is provenance: the dict was authored
entirely by Claude 4.6 (Apr 2, pre-flight) and its data is untraceable.
Decision: redo presets from traceable sources, not patch the prose.

### Tier-1 confirmation (Tony, after applying)
Re-run provenance_scanner.py locally. Expected: Neptune clears; Uranus clears
if citation applied; the two Artemis II findings (lines 237, 268) remain until
the redo. Cannot run in-container: snapshot has no data/provenance_exceptions.json,
so an in-container run over-reports (4 -> 15) by un-suppressing accepted residuals.

### Gemini Mode 7 -- claims checked, three NOT adopted (fetched beats recalled)
- Gemini attributed "58.6 deg explicit" to Ness 1986; the retrieved abstract
  says 60 deg. Provenance of 58.6/59 is real but not "explicit in source."
- Gemini's reentry-speed story (skip-vs-direct trajectory swap to fall just shy
  of Apollo 10's record) is unsourced -- looks confabulated. Use plain figure.
- Offset 0.33 vs 0.3 R_U: primary (Ness 1986) says 0.3.
Convergence (locked): Neptune 47/0.55; Uranus 97.77 axial, 17h14m rotation;
Artemis as-flown launch Apr 1, flyby/max-dist BOTH Apr 6, splashdown Apr 10;
Apollo 13 record 400,171 km; FBC 26,500 ft (both sources independently).

---

## DEFERRED LIST

### D-ARTEMIS -- Artemis II preset redo (supersedes Phase 1 items 37/38)
File: spacecraft_encounters.py, 'Artemis II' dict (3 entries: Earth departure,
lunar closest approach, reentry/splashdown).

WHY REDO, NOT PATCH: the dict fuses three provenance classes behind one
misleading `'source': 'NASA/JSC'` / `'date_source': 'horizons'` stamp:
  - FETCHED (pipeline): position geometry always from Horizons. For the lunar
    entry tagged date_source='horizons', the override block in palomas_orrery.py
    (~L1426) replaces dict date + dist_km with values resolve_encounter_time()
    derives from the Horizons trajectory. So dict date '2026-04-07' and
    dist_km 8900 are DEAD PLACEHOLDERS for that entry -- editing them is cosmetic.
  - RECALLED (Claude 4.6, Apr 2, pre-flight): every `note` string -- TCB times,
    "Apr 7 23:06", FBC "11 km", "Apr 11" splashdown, "Apollo 13 record",
    CubeSat names, "manual piloting demo". None fetched, none overridden,
    rides to hover text verbatim. This is what the audit flags (L237, L268).
  - AUTHORITATIVE (as-entered, NOT overridden): the two date_source='authoritative'
    entries (Earth departure, reentry). Their date AND dist_km are live --
    reentry '2026-04-11' and dist_km 6493 are real and the date is wrong (Apr 10).

CRITICAL UNKNOWN to resolve FIRST (render-in-the-loop):
  Does the Horizons override actually FIRE for the lunar entry? The override
  keys on date_source=='horizons' (palomas_orrery.py L1426) but
  resolve_encounter_time()'s own docstring says it activates on
  'derive_from_horizons': True (spacecraft_encounters.py L589) -- and the
  Artemis II dict has NEITHER... it has date_source='horizons' only. Confirm
  which key gates the override. The override sits in a try/except that swallows
  failures (L1462) and prints [HypOsc] on success. So:
    RENDER the encounter, WATCH THE CONSOLE.
    - See "[RESOLVE] Deriving Moon closest approach for -1024..." and
      "[HypOsc] Using spacecraft encounter epoch" -> override fires, date/dist
      are pipeline-sourced, placeholder is harmless.
    - DON'T see them -> override silently failed, the Apr-7 placeholder is what
      renders, and date_source='horizons' is decorative. That is a renderer bug
      to fix before any preset redo means anything.
  This console check is the single most informative step -- it tells you which
  half of the fused dict is actually real.

REDO METHOD (new session):
  1. Render encounter; confirm [RESOLVE]/[HypOsc] fire (above).
  2. Geometry/date/dist for the lunar entry: take from pipeline output.
  3. Earth departure + reentry entries (authoritative): set date/dist from
     pipeline render or fetched NASA solution -- they are NOT auto-overridden.
  4. Event chronology (TCB/RTCB times, separation, parachute sequence,
     CubeSat deploys, records): FETCH from NASA post-mission report via
     web_search + Gemini cross-check. Horizons does not carry narrative.
  5. Rewrite notes with PER-FIELD provenance, no fused source stamp. Three
     visible origins: pipeline (geometry), fetched report (chronology),
     static (framing). Confirmed values: as-flown launch Apr 1, flyby Apr 6
     (~23:07 UTC), splashdown Apr 10; max dist ~406,771 km; closest lunar
     approach ~6,545 km; Apollo 13 record 400,171 km; FBC 26,500 ft (~8 km),
     drogues 25,000 ft, mains 9,500 ft, entry interface ~122 km.
  6. Re-run provenance_scanner.py; confirm L237/L268 findings clear.

STRUCTURAL FOLLOW-ON (separate, larger -- its own design session):
  Renderer composes encounter notes from resolved values + a narrative
  template, so numbers can never be stored as stale prose again. This is the
  "unify the pipeline, make the seam structural" move. Do NOT fold into the
  redo under time pressure -- design it as its own conversation.

### D-URANUS -- Uranus rendering cleanup (one session, render-in-the-loop)
File: uranus_visualization_shells.py (+ orrery_rendering.py for U2).
Render the full Uranian system FIRST; U2 and U3 resolve by eye.

U1 -- 59/60 inconsistency (code says both)
  Comments say 59, live code renders 60:
    59 deg: L5 (top docstring), L440 (#Source), L547 (#Source), L555 (inline)
    60 deg: L446 hover ("nearly 60" -- already hedged, OK), L459 docstring,
            L503 magnetic_tilt_deg=60 (LOAD-BEARING -- drives geometry), L515 hover
  Sourced: refined ~59 (58.6); "nearly 60" is outreach rounding.
  Recommended: L503 -> 59 (source of truth), update L459 docstring, soften L515
  to "nearly 60 degrees" (match L446); 59-deg comments then correct. Keeping 60
  everywhere is also defensible -- pick ONE; current state (neither) is the bug.

U2 -- Magnetosphere tilt SIGN (render check, not literature)
  Magnitude verified (59-60). Sign = lean direction, set by code convention in
  rotate_to_sunward() Step 1 (orrery_rendering.py ~L232): +tilt leans dipole +Y,
  -tilt leans -Y in the YZ plane. Literature cannot decide sign; only the render.
  CAVEAT: absolute azimuth is rotation-phase-dependent (~17h spin, no epoch phase
  tracked), so sign is partly conventional. Physically checkable:
    1. Magnetotail trails ANTI-sunward (must hold regardless of phase)
    2. Dipole sits ~59-60 deg off the ROTATION axis (correct reference)
    3. Lean consistent with how rotation axis/poles are drawn
  Render: Uranus body-centered (799), magnetosphere + poles on, Sun identifiable.
  Camera: look straight DOWN THE X AXIS (bow-shock-to-tail line) -- tilt is in
  the YZ plane, so down-X shows lean face-on, zero foreshortening. up = rotation
  axis. Tail points sunward -> sunward-rotation bug (not sign). Tail correct but
  dipole mirrors expectation -> flip L503 to negative; magnitude stays.
  NOTE: magnetosphere path is INDEPENDENT of the 105-deg axial fudge (U3) --
  separate transforms (correcting an earlier session note that implied they interact).

U3 -- 105-deg axial tilt fudge (Tony: legacy, pre-osculating-orbits)
  THREE sites use uranus_tilt = 105 deg instead of nominal 97.77 deg:
    L629, L759 (docstring), L1010 (inline "best fit empirically").
  Docstring L759 confirms: "empirically determined to match satellite orbit
  alignment." Tony's context: best-fit to MEAN-parameter moon positions, from
  before satellites migrated to osculating orbits. The reference 105 was fitted
  to has changed -> alignment status UNKNOWN until rendered. L759/L772
  "equatorial-to-ecliptic conversion" note reads as post-hoc rationale for an
  eyeballed number.
  Options:
    1. Derive tilt from IAU pole orientation (RA/Dec -> ecliptic), same frame
       the osculating moons resolve in. Most correct/self-consistent. Cost:
       geometry refactor; confirm the moons' actual resolved frame and match.
    2. Re-fit the fudge to osculating moons. Cheap, re-arms the magic-number
       trap (normalization of deviance). RESIST.
    3. Render full system first, decide nothing. Still aligns -> docs-only.
       Off -> evidence for Option 1.
  Recommended: Option 3 -> Option 1 if off. Trust the render over code structure.

U4 -- Copy-paste "Saturn" comments (cosmetic)
  L651 "around Saturn's rotational axis", L769 "Saturn's ring parameters" --
  cloned from the Saturn module. Fix comment text while in the file for U3.

Suggested sequence: render full system -> judge U2 (sign) + U3 (105 alignment)
by eye -> apply U1 (pick one value, propagate) -> derive (Option 1) if U3 off
-> fix U4 comments -> re-render to confirm -> smoke-test if hover data changed.

---

## CARRIED CONVENTIONS (unchanged, for reference)
- Uploads > project snapshot. Locate edits by content; line numbers drift.
- # Source: comments must sit within scanner lookback (30 lines for display
  strings) and use the `# Source:` form -- in-string prose and distant comments
  do not count. (Item 36 root cause.)
- Fetched (pipeline/web_search) beats recalled (Claude/Gemini memory). Tag
  per-field provenance; never fuse origins behind one source stamp. (D-ARTEMIS.)
- Render wins over code reading. Watch the console for swallowed-exception
  prints. (Override-fires check, D-ARTEMIS.)
- Tier-1 confirmation re-run is Tony-side (needs data/provenance_exceptions.json).
