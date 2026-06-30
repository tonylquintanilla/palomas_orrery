"""
scenarios_food_insecurity.py - Scenario registry for the IPC acute
food-insecurity KMZ layers (Earth System family).

One dict per analysis: the IPC GeoJSON source plus display metadata. The
food_insecurity_generator picker reads this list; the generator's run() builds
the dated KMZ for the selected scenario, naming outputs by scenario_id
(data/<scenario_id>_blockbuster.kmz). Structured to grow as IPC Mapping Tool
exports for other countries are sourced -- add a dict and drop the GeoJSON in
data/; the prefix food_insecurity_<iso3> keeps the family pickable by the
controller's --preload food_insecurity glob.

Stance carries over from food_insecurity_generator.py: synthesize nothing,
transcribe everything, attribute to IPC.

Module updated: June 2026 with Anthropic's Claude Opus 4.8
"""
import os

DATA_DIR = "data"

SCENARIOS = [
    {
        "name": "Sudan -- Acute Food Insecurity (current period)",
        "boundary_type": "food_insecurity",
        "scenario_id": "food_insecurity_sdn",
        "geojson": os.path.join(DATA_DIR, "IPC_SD_A_87143417_2026-06-22.geojson"),
    },
    # Future analyses (add when the IPC GeoJSON is sourced into data/):
    #   South Sudan          -> scenario_id "food_insecurity_ssd"
    #   Chad                 -> scenario_id "food_insecurity_tcd"
    #   Central African Rep. -> scenario_id "food_insecurity_caf"
    #   Ethiopia             -> scenario_id "food_insecurity_eth"
    # {
    #     "name": "South Sudan -- Acute Food Insecurity (current period)",
    #     "boundary_type": "food_insecurity",
    #     "scenario_id": "food_insecurity_ssd",
    #     "geojson": os.path.join(DATA_DIR, "IPC_SS_A_<id>_<date>.geojson"),
    # },
]
