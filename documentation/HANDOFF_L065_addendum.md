# HANDOFF ADDENDUM -- L-065 teaser fixes + record correction

Tony Quintanilla, PE | Claude Opus 4.8 | 2026-06-25

Base SHA: 26e6be94ff03db4387da4a12fa5cc1c1934cc911 (branch main)
  Round trip confirmed (HEAD == this) after your europe_2026 push.
Follows Mode-5: KMZ wet-bulb contours + station pins rendered correct.
Two change sets below. CHANGE SET A is verified (render smoke 8/8).

================================================================================
CHANGE SET A -- earth_system_generator.py  (teaser + the [TO-FETCH] leak)
Three reported teaser issues + two hidden parallel-pipeline leaks of the same
placeholder. The briefing flows to THREE consumers (KMZ intel card, teaser
annotation, mobile briefing); fixing only the teaser would have left two.
================================================================================

A1. run_scenario -- producer-level peak fill (covers all three consumers).
    After the `if not values: raise ...` guard, insert:

    # Fill the regional wet-bulb peak from the fetched grid before ANY briefing
    # consumer renders it -- KMZ intel card, Plotly teaser, and mobile briefing all
    # read scenario['briefing']. Producer-level substitution: no consumer sees raw
    # [TO-FETCH]. (generate_plotly_teaser keeps its own guard for standalone calls.)
    if '[TO-FETCH]' in scenario.get('briefing', ''):
        scenario['briefing'] = scenario['briefing'].replace('[TO-FETCH]', f"{max(values):.1f}")

A2. generate_plotly_teaser -- standalone guard (Studio re-render path).
    After `print("Building Plotly Teaser...")`, insert:

    if briefing and values:
        briefing = briefing.replace('[TO-FETCH]', f"{max(values):.1f}")

A3. generate_plotly_teaser -- FULL wrapped briefing (fixes overflow + shows the
    SOURCE/ATTRIBUTION that was being dropped; fixes the false-click note).
    Replace the old annotation-text block:

      was:
        brief_lines = briefing.split('\n\n')
        brief_text = brief_lines[0] if brief_lines else briefing
        brief_text += "<br><br><i>Click 3D Earth for full visualization in Google Earth</i>"

      now:
        import textwrap
        # Render the FULL briefing -- station records, SOURCE and ATTRIBUTION
        # included -- word-wrapped so it stays inside the box. (Peak already
        # substituted upstream, before the mobile-briefing builder too.)
        wrapped = [textwrap.fill(ln, width=90) if ln.strip() else '' for ln in briefing.split('\n')]
        brief_text = '<br>'.join(wrapped).replace('\n', '<br>')
        brief_text += "<br><br><i>A 3D Google Earth version (KMZ) is also available.</i>"

A4. generate_plotly_teaser -- kill the duplicate title at the colorbar.
    Trace 1 has name=title and the legend wasn't suppressed, so Plotly drew a
    legend entry (the title) over the colorbar. In update_layout add:

        annotations=annotations,
        showlegend=False

VERIFICATION (render smoke on the real generate_plotly_teaser, 8/8):
  source (Met Office) visible ........ PASS
  attribution (Climate Central) ...... PASS
  NO [TO-FETCH] in either path ....... PASS
  peak auto-injected from grid ....... PASS
  no false 'Click 3D Earth' .......... PASS
  KMZ note present ................... PASS
  legend suppressed (no dup title) ... PASS
  wrapped (<br>, stays in box) ....... PASS
  run_scenario sub before all 3 consumers (L94 < L102 < L117) ... PASS
  py_compile ......................... OK

================================================================================
CHANGE SET B -- scenarios_heatwaves.py europe_2026  (record correction)
From primary-source confirmation of your steps 3-4. NOT yet applied -- one
editorial decision for you (see temporal note).
================================================================================

Step 4 (stations) -- the confirm step earned its keep:
  - UK: Met Office (primary, 24 Jun) now lists a NEW provisional June record of
    36.1C at GOSPORT. Wiggonholt 35.8C beat the OLD record but is no longer THE
    record. Our pin note "UK June record" is now wrong. Recommend:
      pin:  {"name": "Gosport UK", "lat": 50.79, "lon": -1.13, "air_temp_c": 36.1,
             "note": "UK June record (provisional)"},   # Source: Met Office, 2026-06-24
      briefing line: "...UK 36.1C (Gosport, prov. June record); Spain 43.7C
             (Tama, Cantabria); Portugal 42.7C (Pinhao)."
  - Spain: AEMET (primary, 23 Jun) CONFIRMS 43.7C at Tama (Liebana), new Cantabria
    absolute record (prev 43.5C). Pin stands as-is. Upgrade source comment to
    "# Source: AEMET Cantabria, 2026-06-23" (primary, not via-CNN).
  - Portugal: Pinhao 42.7C still secondary (Mappr/IPMA). Keep provisional, or
    confirm against IPMA. Flagged, not blocking.

Step 3 (attribution) -- what to actually do: nothing to chase live. "At least 5x
  more likely" is corroborated and dated (Climate Central Climate Shift Index,
  reported 22-24 Jun 2026). Make it read as a dated transcription, not a live
  claim we maintain:
      "...rated this heat at least 5x more likely due to human-caused climate
       change (Climate Central CSI, as reported 24 Jun 2026); EU Copernicus C3S /
       WMO note Europe is warming about twice the global average."
  WATCH still stands: a published WWA rapid study supersedes this if/when it lands.

TEMPORAL NOTE (your call): the grid snapshot is 21 Jun (the wet-bulb field day),
  but Gosport 36.1C was set ~24 Jun. The air-temp pins are the DOME's peak records
  (20-24 Jun), not the 21-Jun instant -- the briefing's "Station Records" framing
  already reads that way. Recommend updating to Gosport 36.1C and treating pins as
  dome records. Alternative: keep Wiggonholt 35.8C noted "(prov.; later exceeded)"
  to stay strictly on the 21-Jun framing. Either is honest; pick the frame.

================================================================================
TONY-SIDE STEPS
================================================================================
  1. Apply CHANGE SET A (re-render gives correct teaser; [TO-FETCH] now auto-fills
     in teaser AND KMZ card from the fetched grid -- no hand-edit needed).
  2. Decide CHANGE SET B temporal frame; apply the UK pin + briefing + attribution
     edits and the AEMET source upgrade.
  3. Re-run earth_system_generator.py -> regenerate europe_2026 teaser + KMZ.
  4. provenance_scanner.py with exceptions file -> Tier-1 = 0 (numbers changed).
  5. Mode-5: eyeball the new teaser (briefing in-box, source visible, one title,
     no dead click-text) and the KMZ card (peak filled, no [TO-FETCH]). Close L-065.

LEDGER: L-065 section-H append:
  - BUILD 2026-06-25 (on 26e6be9): teaser fixes (full wrapped briefing w/ source +
    attribution; showlegend=False removes dup title; KMZ-note reword) and a
    producer-level [TO-FETCH] peak fill in run_scenario covering KMZ card + teaser
    + mobile (two parallel-pipeline leaks caught beyond the visible teaser).
    Record correction: UK pin -> Gosport 36.1C (Met Office primary); AEMET source
    upgraded. Container gate 8/8. DONE after Mode-5 re-render.
