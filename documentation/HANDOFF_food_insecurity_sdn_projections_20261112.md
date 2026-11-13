<!-- Doc-Kind: hand -->
# Handoff: Sudan food insecurity -- adding IPC's two projection periods

Built on 1b473350 at https://github.com/tonylquintanilla/palomas_orrery
(design talk, 2026-10-19). Re-checked at c67d9c6d (2026-11-12): the four
food-insecurity files (food_insecurity_generator.py,
scenarios_food_insecurity.py, earth_system_common.py,
earth_system_controller.py) are byte-identical at both SHAs, so
everything below still holds at c67d9c6d. Gallery repo not touched.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION (zero code).
Supersedes: nothing.
Companions: HANDOFF_food_insecurity_build_v2.md and
MANIFEST_food_insecurity_sudan_v2.md (the original Sudan build, built
on 03630ae).
Ledger: L-001 (the food-insecurity track). This handoff picks up what
L-001 lists as deferred: "the Jun-Sep / Oct-Jan projections remain
deferred per original scope."

---

## What Tony asked

2026-10-19: "can we update the earth science sudan food insecurity
visualization to the latest available data? note that google is
migrating their google earth app from the desktop to the cloud."

## What Tony decided

- 2026-10-19: "yes, i agree, add the october-january map beside the
  period 1 map." The newer map goes BESIDE the February-May map as a
  second layer in the menu. It does not replace it.
- 2026-10-19: "period 2?" Claude recommended adding June-September as
  well, as a third layer. Tony's answer was a request for this handoff,
  not a yes or no. **Tony-action (decide), first item next session:**
  confirm the third layer (June-September) or drop it. The rest of
  this handoff assumes three layers. If he drops it, skip everything
  marked [Jun-Sep].

## What was found (checked 2026-10-19, against IPC's own pages and files)

- **There is no newer IPC map of Sudan than the one the layer uses.**
  IPC's Sudan country page lists the February 2026 analysis (analysis
  period 2026-02-01 to 2027-01-31) as its newest. The layer is built
  from that analysis's Special Report, published 3 June 2026, which is
  in the repo at data/IPC_Sudan_Acute_Food_Insecurity_Feb2026_Jan2027_Special_Report.pdf.
- **The layer draws only the first of that analysis's three periods.**
  IPC's names for them, and ours:
  - "Current": February-May 2026. The layer draws this one. All 228
    features in data/IPC_SD_A_87143417_2026-06-22.geojson carry
    from_date 2026-02-01 and thru_date 2026-05-31.
  - "Projected 1": June-September 2026, the lean season (the months
    before the harvest, when food stocks run lowest). Ended 30 Sept.
  - "Projected 2": October 2026-January 2027, the harvest season. Today
    falls in this one. It is the most recent IPC classification for
    Sudan.
  The file's own header (properties.period_details) lists all three
  periods, but its features hold only the first.
- **IPC's alert of 12 October 2026 carries nothing to map.** It warns of
  rising famine risk in Greater Darfur and Greater Kordofan. It has no
  map and no counts of people by phase. It is not used. (UN News,
  2026-10-12; WHO's release, republished by allAfrica 2026-10-13.)
- **The two projection periods cover only part of Sudan.** Special
  Report page 1: findings for June-September and October-January "are
  limited to areas (56 localities and IDP settlements) where new data
  were available or could be reasonably extrapolated to similar nearby
  areas. A full nationwide projection analysis was not possible due to
  data gaps." And: "Caution is therefore advised when comparing figures
  across analysis periods, as geographic coverage differs
  significantly." Page 28: the 56 areas hold "nearly 8.3 million people
  out of the total population of Sudan (47.5 million)." Shown alone,
  either projection leaves 139 of 195 areas blank. That is why Tony
  ruled for beside, not instead.

## Figures the next session will transcribe (read in the report, 2026-10-19)

Transcribe these from the report's own words. Never compute a total
from the GeoJSON's parts (earth-system-pipeline skill, "Transcribe,
don't sum"). Re-read each at its page before it becomes a constant with
a # Source: line. Page numbers are the PDF's own page count, as a PDF
viewer shows them, the same count the generator's existing citations
use (its key drivers on page 6). The report's printed footers run one
higher; do not mix the two.

October 2026-January 2027 (page 28):
- "an estimated 4.9 million people (59 percent of the analysed
  population) will remain in Crisis or worse conditions (IPC Phase 3 or
  above). This includes over 71,000 people in Catastrophe (IPC Phase
  5), 1.7 million in Emergency (IPC Phase 4), and 3 million in Crisis
  (IPC Phase 3)."
- Coverage: 56 of 195 units, "nearly 8.3 million people out of the
  total population of Sudan (47.5 million)."
- Risk of Famine (page 26): "13 areas and IDP settlements are confirmed
  with a risk of Famine during this period." Beliel (South Darfur) is
  the one area at risk in June-September that is not at risk in
  October-January, "because of expected overall improvement of food
  security conditions based on the expected benefits of the harvest
  season."
- Acute malnutrition was not projected for this period (page 29 box):
  "the second projection was not completed due to the extended
  timeframe, and significant uncertainty."

[Jun-Sep] June-September 2026:
- Phase 5 "is expected to increase from 135,000 to about 200,000 people
  in North Darfur, South Darfur, South Kordofan and West Kordofan. A
  risk of Famine has been detected in 14 areas" (page 3).
- The report's June-September population page (headed "ACUTE FOOD
  INSECURITY ... JUNE - SEPTEMBER 2026") gives the Phase 3+, Phase 4
  and Phase 3 totals for the 56 areas. NOT YET READ: the next session
  reads that page and transcribes from it.
- Trend (page 30): in the 56 areas, Phase 3 or above rises "from 60
  percent to 67 percent" between February-May and June-September, then
  declines "to 59 percent" in October-January.

## What the next session builds

Mode: existing code, so targeted edits by patch (safe-file-editing).
Layers: data -> generator -> scenario list -> controller check -> docs.

1. **Data (Tony first).** Two new IPC Mapping Tool GeoJSON files in
   data/, from the same analysis (ID 87143417, "Acute Food Insecurity
   Analysis - SD February 2026"). Open each and confirm its features'
   from_date and thru_date match the period before building on it.
   Then look at how a projection file marks the 139 areas it did not
   analyse: absent from the file, present with no phase, or present
   with a flag. That decides how those areas are drawn. The generator
   already has NOT_ANALYSED_RGB (white) and INADEQUATE_EVIDENCE_RGB
   (grey), both sampled from the report's page 7 legend.
2. **Generator: make the period-specific constants per scenario.**
   These are written for February-May only, at module level in
   food_insecurity_generator.py:
   - DEFAULT_GEOJSON (line 54)
   - NATL_TOTAL_POP, NATL_PHASE3PLUS, NATL_PHASE4,
     NATL_PHASE5_CATASTROPHE (lines 122-125)
   - PERIOD_LABEL (line 192)
   - the national-summary sentence built at about line 370, which
     reads "Sudan, current period (February - May 2026)"
   The phase colours and labels, the 20-percent rule, the key drivers
   (page 6), the Middle East line, the restraint sentence and the
   citation are the same report for all three periods and stay shared.
   A projection's national card needs a coverage line, transcribed from
   page 1 or page 28, so the reader sees that 139 areas were not
   analysed. Its numbers describe the 56 areas, never all of Sudan.
3. **Scenario list.** Add one dict per new period to SCENARIOS in
   scenarios_food_insecurity.py. Each scenario_id must start with
   food_insecurity_ : the controller finds the layers by that prefix
   (data/food_insecurity_*_blockbuster.kmz). The existing
   food_insecurity_sdn stays as it is, so its KMZ filename and the
   gallery card that links to it do not change.
4. **Risk of Famine.** The generator already reads each area's
   risk_of_famine field (line 263). Confirm against page 26 that the
   October-January file flags 13 areas and that Beliel is not among
   them. [Jun-Sep] 14 areas.
5. **Phase 5 dots (L-069, the hidden Catastrophe reveal)** are drawn
   from each area's phase5_population, so they should carry over per
   period with no new code. Check that they do.
6. **Pre-test and look.** agentic-pre-test before anything is handed
   over; then KMZ byte checks; then Tony opens each layer in Google
   Earth Pro on the desktop and on his phone. His eyes close it.
7. **Close.** Ledger patch: L-001 records the rulings above and the new
   layers; Where We Are moves.

Skills this work fires: earth-system-pipeline (1.2),
provenance-discipline (2.36), safe-file-editing (1.14),
agentic-pre-test (1.3), ledger-and-session-records (1.23).

## Google Earth: recorded, not in this slice

- Google ends support for Google Earth Pro on the desktop on 25 June
  2027. Copies already installed keep working with no further updates;
  downloads stop after that date (Android Authority, updated after 8
  July 2026).
- Google Earth on the web imports KML and KMZ, but its own KML import
  guide lists "Screen and photo overlays" as unsupported. Those are our
  fixed title card and legend card. Polygons and their fill colours,
  folders, network links and pop-up balloons are listed as supported;
  some fields within them "may not be fully supported." Limits: 10,000
  features and 250,000 vertices per import. Sudan's layer has about
  230 features.
- The phone app is not being retired, and the layer's cards have been
  confirmed on iOS before (L-001).
- The redesign for the web version is its own job, after this slice.
  The next session's ledger patch records it as one new item under the
  Earth System track (capture on first mention). It was not recorded on
  2026-10-19.

## Track sequencing

Tony's ruling of 2026-10-07, on L-001: the Earth System track "is
central but behind the orrery website build." His request of
2026-10-19 picks up this one slice. The next session's Where We Are
update says so, and does not move the rest of the track.

## Tony-actions, all in one place

- **(decide)** June-September as a third layer: yes or no.
- **(do)** On the IPC Mapping Tool (ipcinfo.org), open the same Sudan
  analysis as in June ("Acute Food Insecurity Analysis - SD February
  2026") and download the GeoJSON twice: once with June-September 2026
  selected [Jun-Sep], once with October 2026-January 2027 selected.
  Save both into the orrery's data\ folder and commit and push in
  GitHub Desktop. Not done as of c67d9c6d.
- **(do)** After the build: open each new layer in Google Earth Pro on
  the desktop and on the phone.

## Sources

- IPC Sudan country page: https://www.ipcinfo.org/ipcinfo-website/where-what/eastern-africa/sudan/en/
- IPC Sudan Special Report, February 2026-January 2027: https://www.ipcinfo.org/fileadmin/user_upload/ipcinfo/docs/IPC_Sudan_Acute_Food_Insecurity_Feb2026_Jan2027_Special_Report.pdf
- IPC map, Sudan February-May 2026 with projections: https://www.ipcinfo.org/ipc-country-analysis/details-map/en/c/1163315/?iso3=SDN
- UN News, 12 October 2026: https://news.un.org/en/story/2026/10/1168577
- allAfrica / WHO, IPC Sudan alert: https://allafrica.com/stories/202610130125.html
- Android Authority, Google Earth Pro desktop retirement: https://www.androidauthority.com/google-earth-pro-desktop-sunset-3685256/
- Google Earth KML import guide: https://support.google.com/earth/community-guide/307322063/google-earth-kml-import-guide?hl=en

---

Session written November 2026 with Anthropic's Claude Opus 5.5.
