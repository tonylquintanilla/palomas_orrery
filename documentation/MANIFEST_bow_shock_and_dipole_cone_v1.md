MANIFEST: Bow Shocks (8 bodies) + Uranus Dipole-Sweep Cone + Spin Axis
Tony Quintanilla, PE | Claude Opus 4.8 | v1 | June 2, 2026
Authored this session for implementation NEXT session. Build, then handoff.

================================================================================
0. PURPOSE AND STATUS
================================================================================
This manifest is the authoritative build spec for two pieces of work, designed
and verified this session but NOT yet applied to the shell files:

  MOVEMENT 1 (mechanical, Mode 2): a shared bow-shock shape builder, plus eight
    per-file edits that route every planetary bow shock through it. Four bodies
    already have inline bow shocks (Mercury/Venus/Earth/Mars); four giants get
    new ones (Jupiter/Saturn/Uranus/Neptune). Includes a Neptune magnetopause
    value fix surfaced by the nest-check.

  MOVEMENT 2 (new geometry, Mode 1 / design-first): the Uranus magnetic-dipole
    sweep cone, plus a visual spin-axis line as proof of concept. Scope kept
    OPEN -- shared-builder-across-tilted-dipoles is a candidate, not committed.

The shared shape function is WRITTEN AND VERIFIED this session (anchor-exact +
conic-verified; see Section 2). Everything else is mapped but not yet edited.

Build order next session: Movement 1 first (it is mechanical and fully
specified), Tony's Mode-5 visual check, THEN Movement 2 as a design conversation.

================================================================================
1. DECISIONS LOCKED THIS SESSION (do not re-litigate; build to these)
================================================================================
SHAPE: real conic section, the literature-standard form
         r(a) = L / (1 + e*cos a),  L = standoff*(1+e),  focus at planet center,
         a = polar angle from the sunward (-X) axis.
       - This is the published model (Trotignon et al. 2006; Edberg et al. 2008;
         Masters et al. 2008 / Went et al. 2011; Simon Wedlund et al. 2022).
       - Default eccentricity e = 1.05 (marginally hyperbolic; matches fitted
         values: Mars e~1.03-1.05, Saturn e~1.05, general e~1.02-1.06).
       - Chosen OVER a heuristic flank-gain fudge specifically because the conic
         has NO invented parameter -- e and L are sourceable. (Fetched-vs-Recalled
         applied to geometry: the fudge was recalled-style; the conic is cited.)
       - Caveat (Verigin et al. 2003): a pure conic diverges far downstream, so
         it is accurate from nose THROUGH terminator -- which is the rendered
         range. Acceptable for an illustrative orrery.

EARTH: standoff value stays 15 R_E (textbook value, already carries in-code
       cite). ADD a tooltip note that measured-nominal range is ~11-14 R_E
       (Nature Comms 2016) / ~13.5 in the Shue-model lineage. Earth uses the
       CONIC shape like every other body -- it is NOT special-cased to the
       legacy paraboloid in the render. (The paraboloid path exists only as the
       one-time extraction regression test, already green -- see Section 2.)

MARS: keep 1.5 R_M (classic Slavin value; modern MAVEN-era mean is ~1.59-1.6,
      both defensible; Tony chose to keep the existing 1.5).

NEPTUNE MAGNETOPAUSE: fix the rendered magnetopause sunward_distance 34 -> 26.5
      R_N. The 34 was mistakenly the BOW-SHOCK number (34.9); the magnetopause
      was 26.5 (Ness et al. 1989). Required so the new 34.9 shock nests OUTSIDE
      the magnetopause (ratio ~1.32, physical). Separate edit, own cite.

CO-TOGGLE: each bow shock is its own legend entry "X: Bow Shock", independently
      toggleable -- matches the established Earth/Venus convention. NOT grouped
      with the magnetosphere.

INFO MARKER: single info marker per shock at the nose, via create_info_marker
      factory. Hover text MUST carry standoff in km AND AU (AU convention).

CONE (Movement 2): shared builder create_dipole_sweep_cone(tilt_deg, ...),
      Uranus-first as the anchor instance. Half-angle = magnetic DIPOLE TILT
      (Uranus 59 deg), NOT spin-axis obliquity (98 deg). Cone vertex OFFSET from
      planet center (Uranus 0.3 R_U; Neptune 0.55 R_N) -- the dipole is shifted,
      sourced Ness 1986/1989. Built about the spin axis from
      orient_to_planet_pole('Uranus'). SCOPE KEPT OPEN: whether to instantiate
      for Earth/Jupiter/Neptune too is a Tony convergence call next session.

SPIN AXIS: add a visual spin-axis line through the planet figure as proof of
      concept (Uranus first). It is just the orient_to_planet_pole vector drawn
      as a line; pairs naturally with the cone (the cone's spine IS this axis).
      Tony's idea this session; logged as design-first.

================================================================================
2. THE SHARED FUNCTION (VERIFIED -- paste verbatim)
================================================================================
Append to planet_visualization_utilities.py, AFTER create_magnetosphere_shape
and BEFORE create_sphere_points (or at end-of-file before the _old function --
placement is cosmetic). ASCII-only, LF endings.

VERIFICATION DONE THIS SESSION (test artifacts in /home/claude/, re-runnable):
  - Paraboloid path (eccentricity=None) reproduces Earth's legacy 900-point
    cloud BYTE-FOR-BYTE: max abs diff 0.0 on x, y, z. This is the extraction
    regression proof. It has passed; it need not ship in the render.
  - Conic path (e=1.05): nose pinned at exactly -standoff; flank opens
    monotonically; all points finite; no asymptote blow-up (swept to 0.92 of
    the asymptote angle).
  - NOTE FOR MODE 5: the conic flank at e=1.05 is MUCH wider than the legacy
    paraboloid (max flank rho ~6.9e-3 vs ~1.1e-3 for Earth params). This is
    physically correct (marginal hyperbola flares toward its Mach-cone
    asymptote) and is the "doesn't choke past the terminator" behavior Gemini
    predicted -- but the new shocks WILL look substantially more flared than the
    old paraboloids. Tony's eyes decide if that reads well or wants the 0.92
    asymptote factor capped earlier. FLAGGED so it does not surprise.

--- BEGIN FUNCTION ---
# ============================================================================
# Bow shock shape generator (shared)
#
# Extracted June 2026 with Anthropic's Claude Opus 4.8 from the duplicated
# inline bow-shock blocks in mercury/venus/earth/mars _visualization_shells.py
# (four near-identical copies; see protocol "extract duplicated rendering into
# the source module"). Single source of truth for all planetary bow shocks.
#
# Geometry: surface of revolution about the -X (sunward) axis, nose sunward,
# flaring anti-sunward. Caller rotates to the real Sun direction via
# rotate_to_sunward() and offsets to center -- this function returns body-frame
# point clouds only, exactly as the original inline blocks did.
#
# Two shape modes:
#   eccentricity is None (DEFAULT) -> reproduces the original paraboloid
#       formula byte-for-byte: rho = width * (1 + sin(phi)) / 2. Used only as
#       the one-time extraction regression test (Earth legacy). NOT used in the
#       delivered render -- all bodies render via the conic path below.
#   eccentricity = e               -> standard conic-section model used
#       throughout the planetary bow-shock literature:
#           r(theta) = L / (1 + e*cos(theta)),  L = standoff * (1 + e)
#       focus at planet center, theta measured from the sunward (-X) axis.
#       (Trotignon et al. 2006; Edberg et al. 2008; Masters et al. 2008 /
#       Went et al. 2011; Simon Wedlund et al. 2022). Typical fitted
#       eccentricities are marginally hyperbolic: Mars e ~ 1.03-1.05,
#       Saturn e ~ 1.05, general e ~ 1.02-1.06. e = 1.05 is the illustrative
#       default. (A pure conic diverges far downstream -- Verigin et al. 2003 --
#       but is accurate from the nose through the terminator, the rendered
#       range.)
# ============================================================================

def create_bow_shock_shape(standoff, width, n_phi=30, n_theta=30,
                           eccentricity=None):
    """
    Generate body-frame point cloud for a bow shock surface of revolution.

    Parameters:
        standoff (float): subsolar nose distance from body center, in AU
                          (the physical, sourced quantity). Conic nose sits
                          exactly here.
        width (float): legacy paraboloid flank scale in AU. Used ONLY on the
                       paraboloid path (eccentricity=None). Ignored on the
                       conic path, where flank flare is set by eccentricity.
        n_phi, n_theta (int): grid resolution (legacy default 30x30).
        eccentricity (float or None): None -> legacy paraboloid (regression
                       test only); a float (typ. ~1.05) -> conic-section model
                       (the delivered shape).

    Returns:
        tuple: (x, y, z) lists in the body frame, nose toward -X.
    """
    import numpy as np

    bx, by, bz = [], [], []

    if eccentricity is None:
        # ---- Legacy paraboloid path: byte-for-byte the original formula ----
        for i_phi in range(n_phi):
            phi = (i_phi / (n_phi - 1)) * np.pi  # front half only
            x = -standoff * np.cos(phi)
            rho = width * (1 + np.sin(phi)) / 2
            for i_theta in range(n_theta):
                theta = (i_theta / (n_theta - 1)) * 2 * np.pi
                bx.append(x)
                by.append(rho * np.cos(theta))
                bz.append(rho * np.sin(theta))
        return bx, by, bz

    # ---- Conic-section path: r(a) = L / (1 + e*cos a), focus at center ----
    # 'a' is the polar angle from the sunward (-X) axis. a=0 -> nose at
    # r=L/(1+e)=standoff (sunward). Sweep a from 0 toward the asymptote to open
    # the flank; cap before the asymptote so the surface stays finite.
    e = float(eccentricity)
    L = standoff * (1.0 + e)  # so that r(0) = L/(1+e) = standoff exactly

    if e >= 1.0:
        a_asymptote = np.arccos(-1.0 / e)
        a_max = a_asymptote * 0.92  # MODE-5 KNOB: lower to cap flank flare
    else:
        a_max = np.pi  # ellipse: closes, no asymptote

    for i_phi in range(n_phi):
        a = (i_phi / (n_phi - 1)) * a_max
        r = L / (1.0 + e * np.cos(a))
        x = -r * np.cos(a)        # nose at -standoff (a=0)
        rho = r * np.sin(a)
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta - 1)) * 2 * np.pi
            bx.append(x)
            by.append(rho * np.cos(theta))
            bz.append(rho * np.sin(theta))

    return bx, by, bz
--- END FUNCTION ---

================================================================================
3. SOURCED STANDOFF DISTANCES (Gemini-cross-checked, blind pass)
================================================================================
All in planetary radii. Each gets a "# Source:" comment at the call site.
Cross-check verdict: 7 of 8 agreed independently; Earth was a value convention
(15 textbook vs 13.5 Shue) -- decided 15. No sourced number overturned.

  Mercury  1.96  # Winslow et al. 2013, MESSENGER (mp 1.45)
  Venus    1.4   # Shan et al. 2015, Venus Express (range 1.36-1.46; induced)
  Earth    15    # textbook (in-code cite); note range ~11-14 measured
  Mars     1.5   # Slavin classic (MAVEN-era mean ~1.59; kept 1.5 per Tony)
  Jupiter  82    # Joy et al. 2002 (mean ~84, sigma~16, highly variable)
  Saturn   27    # Went et al. 2011 / Sulaiman et al. 2016, Cassini
  Uranus   23.7  # Ness et al. 1986, Voyager 2 (mp 18.0; single flyby)
  Neptune  34.9  # Ness et al. 1989, Voyager 2 (mp 26.5; single flyby)

Confidence gradient (for tooltips): Earth/Jupiter/Saturn = many crossings;
Mercury/Venus/Mars = orbital missions; Uranus/Neptune = SINGLE Voyager-2 flyby,
single-epoch -- worth a tooltip word.

NEST-CHECK (each shock must sit outside rendered magnetopause sunward_distance):
  Jupiter 82 > 50 ok | Saturn 27 > 22 ok | Uranus 23.7 > 21 ok |
  Neptune 34.9 vs 34 -> FAIL until magnetopause fixed to 26.5 (see 4E).
  Earth/Mercury/Venus/Mars inner shocks already nest.

================================================================================
4. PER-FILE EDITS (Movement 1) -- bottom-up within each file
================================================================================
Line numbers are from THIS SESSION's uploads. RE-VERIFY against fresh uploads
before editing -- if Tony re-uploads, grep the anchors first (the protocol
staleness rule). Binary-mode (rb/wb) edits; py_compile each after.

Common pattern for the four bodies that ALREADY have a bow shock
(Mercury/Venus/Earth/Mars): replace the inline paraboloid block (the
bow_shock_x/y/z construction loop) with a single call:

    bx, by, bz = create_bow_shock_shape(
        standoff=STANDOFF * BODY_RADIUS_AU,
        width=WIDTH * BODY_RADIUS_AU,     # ignored on conic path; keep for signature
        eccentricity=1.05,
    )
    bow_shock_x = np.array(bx) ; bow_shock_y = np.array(by) ; bow_shock_z = np.array(bz)
    # then the EXISTING rotate_to_sunward + center-offset + Scatter3d + info marker
    # stays as-is. Only the shape construction is replaced.

Keep each file's existing rotate_to_sunward call, trace styling, legendgroup,
and info-marker call. ONLY the shape loop changes (plus the standoff value and
its Source comment).

--- 4A. planet_visualization_utilities.py ---
ADD create_bow_shock_shape (Section 2). Add credit line to module docstring:
  "Module updated: June 2026 with Anthropic's Claude Opus 4.8 (shared
   create_bow_shock_shape extracted from 4 inline copies; conic-section model)."

--- 4B. mercury_visualization_shells.py ---
  Import L25: add create_bow_shock_shape to the utilities import tuple.
  Block ~L334-371: replace inline loop with shared call.
  Standoff L340: 15 -> 1.96.  # Source: Winslow et al. 2013, MESSENGER
  Width was 25; pass through (ignored on conic path).

--- 4C. venus_visualization_shells.py ---
  Import L30: add create_bow_shock_shape.
  Block ~L635-672: replace inline loop with shared call.
  Standoff L641: 15 -> 1.4.   # Source: Shan et al. 2015, Venus Express (induced)

--- 4D. earth_visualization_shells.py (REGRESSION-ANCHOR FILE) ---
  Import L44: add create_bow_shock_shape.
  Block L726-794: replace inline paraboloid loop with shared CONIC call
    (eccentricity=1.05). Earth now renders the conic like everyone else.
  Standoff L733: stays 15.  # Source: textbook ~15 R_E; measured nominal ~11-14
  Bow_shock_text L765-769: ADD a sentence noting measured nominal ~11-14 R_E.
  IMPORTANT: this is the body whose OLD output we extraction-tested against. The
    test (paraboloid path) already passed. Switching Earth to the conic CHANGES
    its render intentionally (per Tony's call) -- this is the one body whose
    visual will differ from the prior session by design. Tony Mode-5: confirm
    the conic Earth shock reads well.

--- 4E. mars_visualization_shells.py ---
  Import L32: add create_bow_shock_shape.
  Block ~L688-723: replace inline loop with shared call.
  Standoff L694: stays 1.5.  # Source: Slavin classic (MAVEN-era ~1.59)

--- 4F. jupiter_visualization_shells.py (NEW SHOCK) ---
  Import L25: add create_bow_shock_shape.
  Inside create_jupiter_magnetosphere (def L515): AFTER the magnetosphere
    traces, ADD a new bow-shock block following the Earth pattern:
      standoff = 82 * JUPITER_RADIUS_AU   # Source: Joy et al. 2002
      bx,by,bz = create_bow_shock_shape(standoff, width=standoff*1.6,
                                        eccentricity=1.05)
      -> rotate_to_sunward -> center offset -> Scatter3d
         name/legendgroup 'Jupiter: Bow Shock', hoverinfo='skip'
      -> create_info_marker at nose, color 'rgb(255,200,150)',
         hover text with km AND AU.
  No shell_configs.py change (builder returns all traces; dispatch confirmed).

--- 4G. saturn_visualization_shells.py (NEW SHOCK) ---
  Same as 4F. Standoff 27 * SATURN_RADIUS_AU. # Source: Went et al. 2011, Cassini
  legendgroup 'Saturn: Bow Shock'. Saturn e known ~1.05 (matches default).

--- 4H. uranus_visualization_shells.py (NEW SHOCK) ---
  Same as 4F. Standoff 23.7 * URANUS_RADIUS_AU. # Source: Ness et al. 1986, V2
  legendgroup 'Uranus: Bow Shock'.
  (Movement 2 cone + spin axis also land in this file -- separate edit.)

--- 4I. neptune_visualization_shells.py (NEW SHOCK + MAGNETOPAUSE FIX) ---
  TWO SEPARATE EDITS (Separate the Problems):
  (1) MAGNETOPAUSE FIX, L481: 'sunward_distance': 34 -> 26.5
        # Source: Ness et al. 1989, V2 -- magnetopause 26.5 R_N (34.9 was the
        #         bow-shock value, mistakenly used here). Required for nest.
      Update the inline comment too ("~34 Neptune radii" -> "~26.5 R_N mp").
  (2) NEW SHOCK block, standoff 34.9 * NEPTUNE_RADIUS_AU.
        # Source: Ness et al. 1989, Voyager 2
      legendgroup 'Neptune: Bow Shock'.
      Leave the existing comet-shape magnetosphere otherwise untouched.

--- DEAD-CODE ANNOTATION (Tony's standing instruction) ---
  While in each file, if the touched region reveals dead inline code (e.g. the
  Uranus dead rotate_points import from prior session), add a "# DEAD:" comment
  noting it. Do not remove -- that is the deferred dead-code sweep (D3). Just
  annotate so it is visible.

================================================================================
5. VERIFICATION PLAN (Movement 1) -- run before declaring done
================================================================================
  1. py_compile EVERY edited file (8 shell files + utilities).
  2. RUNTIME SMOKE TEST against the LIVE dispatch, not the per-body builders:
       - Resolve each body's magnetosphere builder via CUSTOM_SHELLS in
         shell_configs.py (builder string -> import -> call).
       - Call each builder; assert a trace with name 'X: Bow Shock' exists.
       - Assert the bow-shock point cloud is finite and non-empty.
       - Assert exactly one info marker per shock (cross symbol).
       - Neptune: assert magnetosphere sunward extent < bow-shock nose extent
         (the nest now holds).
     A smoke test of the per-body builder alone passes falsely -- exercise the
     dispatch path. (v3.24 lesson: data-content sweeps need a live-dispatch
     runtime test; py_compile is necessary, not sufficient.)
  3. xvfb agentic pre-test on palomas_orrery.py (SystemButtonFace sed swap).
  4. TONY MODE 5: the load-bearing check. Specifically:
       - Earth conic shock reads well (this render CHANGED by design).
       - Conic flank flare at e=1.05 is not too wide (0.92 knob if it is).
       - All four giants' shocks sit visibly OUTSIDE their magnetopauses.
       - Neptune shock nests correctly after the 34->26.5 fix.

================================================================================
6. MOVEMENT 2 (cone + spin axis) -- DESIGN-FIRST, not specced to code yet
================================================================================
Open as a conversation next session, AFTER Movement 1 + Mode 5. Decisions still
open (Tony's convergence calls):
  - Cone scope: Uranus-only, or shared create_dipole_sweep_cone across all
    tilted-dipole bodies (Earth 11.5, Jupiter 9.6, Neptune 47, Uranus 59;
    skip Saturn <0.01 and Mercury <0.1 as degenerate)?
  - Cone registration: own toggle vs grouped with the magnetosphere illustration?
  - Spin-axis line: every planet, or just the cone-bearing ones? Length? Style
    (the marker-symbol convention reserves cross for info; a line is fine)?
  - Cone surface vs wireframe vs translucent mesh -- a Mode-5 aesthetic call.
Verified inputs ready for the build:
  - Dipole tilts (Gemini-confirmed): Me <0.1, Earth 11.5, Jup 9.6, Sat <0.01,
    Ur 59, Nep 47. Sources per body (Ness 1986/1989 for the ice giants).
  - Vertex offsets: Uranus 0.3 R_U, Neptune 0.55 R_N (Ness; dipole is shifted).
  - Half-angle = DIPOLE TILT, not obliquity (double-confirmed: me + Gemini).
  - Producer: orient_to_planet_pole('Uranus') gives the spin axis (validated
    last session; obliquity already baked in).

================================================================================
7. OPEN LEDGER ITEMS TO CARRY (for v24 handoff after the build)
================================================================================
  - Item 24 (bow shocks): reframed -- NOT a pole-frame consumer. Sun-framed via
    rotate_to_sunward. Status after build: Earth/inner refactored, 4 giants
    added, Neptune mp fixed. CLOSE on Mode-5 sign-off.
  - N13 (Uranus tilt cone): Movement 2; scope OPEN.
  - NEW: spin-axis visual indicator (Tony, this session) -- candidate, design-
    first, pairs with cone.
  - NEW: conic-flare Mode-5 flag (0.92 asymptote knob).
  - Carried residues (D3 dead-code sweep, do not chase): dead rotate_points
    import in uranus_visualization_shells.py; third '105' at idealized_orbits.py
    L3699 (satellite mean-element fallback); Neptune ring-fudge cleanup (the
    commented-out orient_to_planet_pole transform, hand-fit 32/34 deg, U3 analog)
    -- gated on grep-confirming create_neptune_ring_system is on the live
    CUSTOM_SHELLS path before touching.
  - Conic shape is an ILLUSTRATIVE approximation accurate nose-through-terminator
    (Verigin caveat); not a deep-tail model. Stated for honesty.

================================================================================
8. PROVENANCE NOTE
================================================================================
Every standoff and tilt in this manifest is sourced to primary literature and
was independently cross-checked by Gemini (blind pass, no anchoring). The conic
SHAPE decision was made on a dedicated literature search, replacing an earlier
heuristic. No recalled-from-training numbers are embedded. Where a value rests
on a single Voyager-2 flyby (Uranus, Neptune), that caveat is explicit and
belongs in the tooltip. Earth's 15 is a textbook convention with the measured
range noted -- not presented as a precise fit.

Module credit line for every file touched in the build:
  "Module updated: June 2026 with Anthropic's Claude Opus 4.8"
