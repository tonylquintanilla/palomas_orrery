# Handoff Addendum -- Phase 1 results + Uranus cleanup round
Session: provenance Phase 1 (items 36-39 + Uranus tilt sign)
Date: May 30, 2026

---

## PART A -- Phase 1 provenance: DONE (sourcing), pending Tony apply + re-scan

web_search sourcing complete; Gemini Mode 7 cross-check done. Line numbers
are from the /mnt/project/ snapshot -- LOCATE BY CONTENT, live files may differ.
The spacecraft file was flagged not-current; verify against live before editing.

### Item 36 -- Neptune magnetosphere -- CONFIRM, no fact change
47 deg tilt, 0.55 R_N offset. All sources agree (web + Gemini).
Comment to add above the magnetosphere string:
    # Source: Ness et al. (1989) Science 246:1473 -- Voyager 2 magnetometer;
    # offset tilted dipole inclined 47 deg to rotation axis, displaced 0.55 R_N
    # from center. Confirmed NASA "30 Years Ago: Voyager 2 Explores Neptune" (2024).

### Item 39 -- Uranus magnetosphere string -- CONFIRM values, FIX 59/60 split
Axial tilt 97.77 deg (exact), rotation 17h 14m, offset 0.3 R_U.
Magnetic tilt is the contested one -- see Part B item U1 (same issue, code+string).
Comment to add:
    # Source: Ness et al. (1986) Science 233:85 -- Voyager 2 magnetometer.
    # Dipole-vs-rotation tilt: abstract states 60 deg; refined value commonly
    # cited ~59 deg (58.6 deg). Dipole offset 0.3 R_U (~1/3 radius). Axial tilt
    # 97.77 deg (NASA Uranus fact sheet). Sidereal rotation 17h 14m.

### Item 37 -- Orion lunar-flyby note -- FACT ISSUE (stale-plan timeline)
Confirmed: Apollo 13 record 400,171 km / 248,655 mi; max distance ~406,771 km;
closest lunar approach ~6,545 km. As-flown dates: launch Apr 1, max-distance AND
closest approach BOTH Apr 6 2026 (~23:07 UTC), splashdown Apr 10.
DRAFT BUG: note narrates Apr 7 / Apr 11 = pre-flight plan, ~1 day late.
Fix = re-derive timestamps from OEM/Horizons (fetched), not hand-edit. Date
label should read Apr 6. Verify against live file -- may already be fixed.

### Item 38 -- Orion reentry note -- CONFIRM mostly, FIX FBC altitude
FBC parachutes 26,500 ft (~8 km) <-- draft ~11 km was ~3 km too high.
Both web (NASA parachute fact sheet) and Gemini independently land on 26,500 ft.
Drogues 25,000 ft (~7.6 km); mains 9,500 ft (~2.9 km); entry interface ~122 km;
reentry ~11.2 km/s (~25,000 mph). Comment:
    # Source: NASA Orion parachute fact sheet (nasa.gov, 2017) + as-flown
    # Artemis II (NASA, Apr 2026). FBC parachutes 26,500 ft (~8 km), drogues
    # 25,000 ft (~7.6 km), mains 9,500 ft (~2.9 km). Entry interface ~122 km at
    # ~11.2 km/s (~25,000 mph). As-flown: launch Apr 1, flyby/max-dist Apr 6,
    # splashdown Apr 10, 2026.

### Gemini Mode 7 -- claims NOT adopted (fetched primary wins over recalled)
- Gemini attributed "58.6 deg explicit" to Ness 1986; the abstract I retrieved
  says 60 deg. Provenance of 58.6/59 is real but not "explicit in source."
- Gemini's reentry-speed story (skip-vs-direct trajectory swap to fall just shy
  of Apollo 10's record) is UNSOURCED -- looks confabulated. Use plain ~11.2 km/s,
  no causal narrative.
- Offset 0.33 vs 0.3 R_U: primary says 0.3.

### Tony's remaining step
Re-run provenance_scanner.py locally AFTER edits, confirm Tier-1 drops 4 -> 0.
(Cannot run in-container: snapshot has no data/provenance_exceptions.json, so an
in-container run over-reports 4 -> 15. Confirmation is Tony-side.)

---

## PART B -- URANUS CLEANUP ROUND (new session, all items together)

Render-gated (Mode 5) and file-gated -- do as one session with current files
uploaded. Render the full Uranian system FIRST; several items resolve by eye.

### U1 -- 59/60 inconsistency (code says both)
Comments say 59, live code renders 60. Split:
  59 deg: L5 (top docstring), L440 (#Source), L547 (#Source), L556 (inline)
  60 deg: L446 hover ("nearly 60" -- already hedged, OK), L459 docstring,
          L503 magnetic_tilt_deg=60 (LOAD-BEARING -- drives geometry), L515 hover
Sourced truth: refined ~59 (58.6), "nearly 60" is outreach rounding.
Recommended: make L503 = 59 (source of truth), update L459 docstring to match,
soften L515 to "nearly 60 degrees" (match L446), 59-deg comments then correct.
Keeping 60 everywhere is also defensible -- just pick ONE; current state (neither)
is the only thing actually wrong.

### U2 -- Magnetosphere tilt SIGN (render check, not literature)
Magnitude verified (59-60). Sign = direction of lean, set by code convention in
rotate_to_sunward() Step 1 (orrery_rendering.py L232+): +tilt leans dipole +Y,
-tilt leans -Y in the YZ plane. Literature cannot decide sign; only the render.
CAVEAT: absolute azimuth is rotation-phase-dependent (~17h spin, model tracks no
epoch phase), so sign is partly conventional. What IS physically checkable:
  1. Magnetotail trails ANTI-sunward (must hold regardless of phase)
  2. Dipole sits ~59-60 deg off the ROTATION axis (correct reference axis)
  3. Lean consistent with how rotation axis/poles are drawn
Render setup: Uranus body-centered (799), magnetosphere + poles on, Sun
identifiable. Camera: look straight DOWN THE X AXIS (bow-shock-to-tail line) --
tilt lives in YZ plane, so down-X shows lean face-on, zero foreshortening.
up = rotation-axis direction. If tail points sunward -> sunward-rotation bug, not
sign. If tail correct but dipole mirrors expectation -> flip L503 to negative.
NOTE: magnetosphere path is INDEPENDENT of the 105-deg axial fudge (U3) -- they
are separate transforms; correcting my earlier session note.

### U3 -- 105-deg axial tilt fudge (Tony: legacy, pre-osculating-orbits)
L629 and L759 use uranus_tilt = 105 deg instead of nominal 97.77 deg.
Docstring L759 confirms: "empirically determined to match satellite orbit
alignment." Tony's context: this was a best-fit to MEAN-parameter moon positions,
from before satellites migrated to osculating orbits. The reference 105 was
fitted to has since changed -> alignment status now UNKNOWN until rendered.
The L772 "equatorial-to-ecliptic conversion" note reads as post-hoc rationale for
an eyeballed number, not a real frame fact.
Options:
  1. Derive tilt from IAU pole orientation (RA/Dec -> ecliptic), same frame the
     osculating moons now resolve in. Most correct, self-consistent. Cost: geometry
     refactor; must confirm the moons' actual resolved frame and match it.
  2. Re-fit the fudge to osculating moons. Cheap, but re-arms the same magic-number
     trap (normalization of deviance). RESIST.
  3. Render full system first, decide nothing. If 105 still aligns -> docs-only
     cleanup. If off -> evidence for Option 1.
Recommended: Option 3 -> Option 1 if off. Trust the render over code structure.

### U4 -- Copy-paste "Saturn" comments (cosmetic)
L651 "around Saturn's rotational axis", L769 "Saturn's ring parameters" -- cloned
from the Saturn module. Geometry block was copied, not derived for Uranus. Fix
comment text while in the file for U3.

### Uranus session sequence (suggested)
Render full system -> judge U2 (sign) and U3 (105 alignment) by eye -> apply U1
(pick one value, propagate) -> Option 1 derive if U3 off -> fix U4 comments ->
re-render to confirm -> smoke-test if any data-content (hover) changed.
