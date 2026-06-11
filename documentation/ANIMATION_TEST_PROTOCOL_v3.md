# ANIMATION TEST PROTOCOL v3 -- 21/51 Through Phase 3 Session B

Tony Quintanilla, PE | Claude | June 11, 2026
Supersedes v2 (Phase 2 gate -- PASSED June 10) and the Session-A checklist
in HANDOFF_animation_phase3A.md (PASSED June 10).
Session B patch base: orrery repo HEAD a9f0ec4 | Patched: palomas_orrery.py,
shell_configs.py | Companion tools: measure_animation_html.py,
measure_perframe_elements.py (both in repo)

PURPOSE. Gate the per-frame element engine (Session B) in the live render.
Confirmed baselines on record: Phase 1 (fence, 88-94% reductions), Phase 2
(center-marker canon, N3/O5/O6a closed), Session A (wrapper retirement,
notices). Nothing in Session B touches those mechanisms except where stated.

WHAT SESSION B ADDED
1. Per-frame engine: rotation axis, dipole cone, and sun-direction indicator
   now REBUILD each frame at every eligible NON-CENTER body's position --
   eligibility = body animated + any of its shell checkboxes on (the same
   trigger as the center dispatch). Budget line prints at allocation:
   "[ANIMATION] Per-frame engine: K element groups, ~X KB/frame".
2. Greyed-out legend disclosure: every checked-but-unrendered shell gets a
   muted legend entry "<Body>: <Shell> (static plots only)" at the legend
   bottom. Console notices remain as developer diagnostics.

================================================================
SESSION B RENDER GATE
================================================================

B1. THE HEADLINE: Uranus rides with its axis (Sun-centered)
  Config: Sun-centered animation, Uranus checked, any Uranus shell checked
  (e.g. magnetosphere), ~29 frames, actual orbits on.
  [ ] Console: per-frame engine line reports 3 element groups, ~30 KB/frame.
  [ ] Rotation axis + dipole cone + sun-direction indicator RIDE Uranus
      through the animation (scrub the slider; they translate with the
      marker, orientation inertial -- the sideways axis holds its direction
      as Uranus moves).
  [ ] Indicator points toward the Sun marker at every scrubbed frame.
  [ ] Uranus's checked big shells (magnetosphere etc.): NOT rendered, but
      greyed legend entries present (see B4).
  [ ] No assert message in console (trace-count stability held).

B2. Earth non-center (faster mover)
  Config: Sun-centered, Earth + Moon checked, Earth magnetosphere checked.
  [ ] Earth's rotation axis + indicator ride Earth per frame (Earth has no
      dipole-cone entry -- only 2 groups expected in the console line).
  [ ] "Earth: Magnetosphere (static plots only)" greyed in legend.

B3. Sun as non-center body (planet-centered animation)
  Config: Earth-centered, Sun checked, any Sun shell checked.
  [ ] Sun's rotation axis rides the moving Sun marker.
  [ ] Sun-direction indicator for the Sun itself: SUPPRESSED (body at Sun
      position -- allocation-time constant; console may show the dispatch
      suppression line). Expected, by design rule 2(b).
  [ ] Sun's checked shells: greyed legend entries (supersedes the O2
      console-only state).

B4. Legend disclosure mechanics (the Finding-2 upgrade)
  [ ] Greyed entries sit at the LEGEND BOTTOM (legendrank), in Plotly's
      muted toggled-off style, with the italic "(static plots only)" note.
  [ ] Clicking a greyed entry: nothing renders (dataless). KNOWN WART: the
      entry text un-mutes until clicked again -- judge whether acceptable.
  [ ] Legend toggles for REAL traces unaffected.

B5. Payload measurement
  python measure_animation_html.py B1_export.html
  [ ] "Traces carried in frames" now lists the element-group traces
      alongside the markers.
  [ ] Frames payload ~= (markers + ~30 KB/frame per decorated body) x N --
      consistent with the budget console line. Record the numbers.

B6. Regression (engine inactive)
  Config: P1-style run, NO shells checked anywhere.
  [ ] No engine console line; no greyed entries; payload matches Phase 1/2
      numbers (zero overhead when unused).
  [ ] One static plot regression: nothing in Session B touches the static
      pipeline except shell_configs tags (inert metadata for static) --
      confirm a shells-on static plot renders unchanged.

================================================================
OBSERVATION LOG v3 (continue numbering)
================================================================
  O10. First impressions of the riding primitives: size, clutter,
       educational read (the half_len_frac knobs exist if scale is off).
  O11. Greyed-legend naming quality: the display names derive mechanically
       from checkbox keys ("Uranus: Core", "Sun: Gravitational") -- flag any
       that read wrong.
  O12. Scaling interactions: do riding elements get clipped by the cube
       (the Finding-1 class)? Concrete cases feed the Session-C
       consolidated auto-scale.
  O13. Free-form.

================================================================
RECORD FOR THE LEDGER / NEXT HANDOFF
================================================================
- B1-B6 pass/fail; O10-O13; payload numbers; new HEAD after push.
- On pass: 21/51 Session B render-confirmed; Session C scope stands
  (comet-tail trace-returning refactor + opt-in mode, sodium tail,
  hover disclosure sweep, consolidated auto-scale w/ Finding-1 cases).

Module updated: June 2026 with Anthropic's Claude Fable 5
