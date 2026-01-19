import requests
import simplekml
import numpy as np
import time
import json
import os
import textwrap
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import griddata
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
#          SCENARIO CONFIGURATION
# ==========================================
# ==========================================
#          SCENARIO CONFIGURATION
# ==========================================
SCENARIOS = {
    # --- HISTORICAL BASELINE ---
    "New York City (Aug 1948)": {
        "id": "nyc_1948",
        "date": "1948-08-26",
        "lat_range": range(45, 37, -1),   # EXPANDED: Down to 37N (captures DC/Baltimore)
        "lon_range": range(-80, -70, 1), 
        "focus_val_min": 24,              
        "description": "Historical Baseline (Pre-AC Era). 100F+ Temps.",
        "briefing": "THE PRE-COOLING ERA. A massive heatwave hit the Northeast US. In an era before widespread AC, "
        "New Yorkers slept on fire escapes. This serves as our 'Historical Baseline'—survivable by the young, lethal to the vulnerable.\n\n" 

        "Station Records: NYC 29.5°C, Philadelphia 28.7°C.\n" 
        "Regional Map Peak: ~26.0°C.\n\n"
        
        "SOURCE: NOAA; NY Times Archives"
    },

    "Midwest Torch (July 1954)": {
        "id": "st_louis_1954",
        "date": "1954-07-14",
        "lat_range": range(42, 34, -1),   
        "lon_range": range(-94, -86, 1), 
        "focus_val_min": 26.0,              
        "description": "All-time state record (117°F). Deaths outnumbered births.",
        "briefing": "THE MIDWEST TORCH. East St. Louis hit 47.2°C (117°F), a record that still stands today. "
        "The combination of extreme air temperature and river valley humidity created conditions that overwhelmed the era's limited infrastructure.\n\n" 
        
        "Station Record: East St. Louis 117°F (Air Temp).\n" 
        "Regional Map Peak: ~30.0°C (Wet Bulb Estimate).\n\n"
        
        "SOURCE: Illinois State Water Survey"
    },

    "LA Inferno (Sept 1955)": {
        "id": "la_1955",
        "date": "1955-09-01",
        "lat_range": range(35, 32, -1),   # Southern California Bight
        "lon_range": range(-120, -116, 1), 
        "focus_val_min": 22.0,            # Lower threshold for Dry Heat detection  
        "description": "The 'Forgotten Disaster'. 946 deaths. 110°F.",
        "briefing": "THE COASTAL SURPRISE. A massive high-pressure ridge parked over the West Coast. Downtown LA hit 110°F (43°C), and temps stayed above 100°F for a week. "
        "With almost no air conditioning in 1955, the mortality (946 deaths) exceeded most earthquakes, exposing the deadly 'adaptation gap' of coastal cities.\n\n"
        
        "Station Record: Los Angeles 110°F (Air Temp).\n"
        "Regional Map Peak: ~26.5°C (Wet Bulb).\n\n"
        
        "SOURCE: LA Almanac; WeatherBug"
    },

    "The Heat Index Event (July 1966)": {
        "id": "st_louis_nyc_1966",
        "date": "1966-07-12",
        "lat_range": range(42, 37, -1),   # The "Heat Corridor"
        "lon_range": range(-91, -73, 2),  # Spanning St. Louis (-90) to NYC (-74)
        "focus_val_min": 25.0,              
        "description": "The event that created the Heat Index metric.",
        "briefing": "THE ORIGIN STORY. A massive heat dome bridged the Midwest and East Coast simultaneously. "
        "The sheer misery of high humidity in St. Louis combined with urban heat in NYC caused mass mortality, forcing the NWS to invent the 'Heat Index' to explain why 95°F felt like 105°F.\n\n"
        
        "Station Records: St. Louis 106°F, NYC 103°F.\n"
        "Regional Map Peak: ~29.0°C.\n\n"
        
        "SOURCE: National Weather Service"
    },

    "UK Heat Wave (June 1976)": {
        "id": "uk_1976",
        "date": "1976-06-26",
        "lat_range": range(55, 48, -1),
        "lon_range": range(-5, 5, 1),
        "focus_val_min": 18.0,
        "description": "The Great Drought. Water rationing and 20% excess deaths.",
        "briefing": "THE DROUGHT TRAP. One of the driest summers in UK history. While absolute temperatures (35.9°C) seem modest, " 
        "the compound stress of drought led to 20% excess mortality.\n\n" 
        
        "Station Record: London 21.5°C.\n"
        "Regional Map Peak: ~20.0°C.\n\n"

        "SOURCE: Met Office; ONS"
    },

    "US Heat Wave (July 1980)": {
        "id": "us_1980",
        "date": "1980-07-15",
        "lat_range": range(40, 30, -2),   # EXPANDED: Down to 30N (captures Dallas/Jackson)
        "lon_range": range(-98, -85, 2),  # EXPANDED: West to -98W (captures Dallas)
        "focus_val_min": 24.0,
        "description": "1,700+ deaths. The 'Billion Dollar' heat disaster.",
        "briefing": "THE RUNAWAY HIGH. A massive high-pressure ridge stalled over the central US. Memphis hit 108°F (42°C). " 
        "It caused >1,700 deaths and $20 billion in agricultural losses.\n\n" 
        
        "Station Records: Memphis 28.8°C, Kansas City 28.5°C.\n"
        "Regional Map Peak: ~28.0°C.\n\n"

        "SOURCE: NOAA; Karl & Quayle (1981)"
    },

    "Athens Heat Wave (July 1987)": {
        "id": "athens_1987",
        "date": "1987-07-27",
        "lat_range": range(41, 36, -1),   # EXPANDED: Up to 41N (captures Thessaloniki)
        "lon_range": range(20, 26, 1),
        "focus_val_min": 23.0,
        "description": "1,300+ deaths. The Urban Heat Island wake-up call.",
        "briefing": "THE CONCRETE TRAP. A week-long heatwave turned Athens into a kiln. The concrete city retained heat overnight, " 
        "denying physiological recovery. ~1,300 deaths forced a complete overhaul of Greek infrastructure.\n\n" 
        
        "Station Record: Athens 25.7°C.\n"
        "Regional Map Peak: ~24.0°C.\n\n"

        "SOURCE: Metaxas et al. (1991)"
    },

    # --- MODERN ERA ---
    "Chicago Heat Wave (July 1995)": {
        "id": "chicago_1995",
        "date": "1995-07-13",
        "lat_range": range(50, 30, -2),   
        "lon_range": range(-100, -80, 2), 
        "focus_val_min": 24.0,
        "description": "The 'silent killer' event. High mortality at lower thresholds.",
        "briefing": "A TRAGEDY OF VULNERABILITY. Wet bulbs hovered in the 'Red Zone'. Lack of AC and the 'Urban Heat Island' effect " 
        "proved fatal for the elderly. CDC records confirm 739 excess deaths in 5 days.\n\n" 

        "Station Record: Chicago (Midway) 28.3°C.\n"
        "Regional Map Peak: ~29.4°C (Corn Belt Humidity Pool).\n\n"

        "SOURCE: CDC; Klinenberg (2002)"
    },

    "Europe (The Great Mortality - Aug 2003)": {
        "id": "europe_2003",
        "date": "2003-08-10",
        "lat_range": range(53, 40, -2),   # EXPANDED: Up to 53N (captures Berlin)
        "lon_range": range(-5, 15, 2),    
        "focus_val_min": 22.0,
        "description": "The event that changed Europe. 70,000+ excess deaths.",
        "briefing": "VULNERABILITY VS EXPOSURE. With <2% AC adoption and aging demographics, this 'moderate' wet-bulb heat became " 
        "the deadliest natural disaster in modern European history.\n\n" 

        "Station Record: Rome 25.2°C, Paris 24.1°C.\n"
        "Regional Map Peak: ~25.7°C.\n\n"

        "SOURCE: Robine et al. (2008); INSERM"
    },

    "Russia Heat Wave (July 2010)": {
        "id": "russia_2010",
        "date": "2010-07-29",
        "lat_range": range(64, 48, -2),
        "lon_range": range(25, 55, 2),
        "focus_val_min": 20.0,              
        "description": "55,000+ excess deaths. Smoke and stagnation.",
        "briefing": "THE CONTINENTAL TRAP. A 'blocking high' stalled over Russia. The sheer duration (weeks) + toxic smoke from peat fires " 
        "caused 55,000 excess deaths, proving that 'safe' wet bulbs are lethal if sustained.\n\n" 
        
        "Station Record: St. Petersburg 23.4°C, Moscow 22.8°C.\n"
        "Regional Map Peak: ~25.2°C.\n\n"
        
        "SOURCE: Barriopedro et al. (2011)"
    },

    # --- ACCELERATION PHASE ---
    "India/Pakistan (May 2015)": {
        "id": "india_pak_2015",
        "date": "2015-05-24",
        "lat_range": range(36, 5, -2),
        "lon_range": range(55, 96, 2),
        "focus_val_min": 24.0,              
        "description": "3,500+ deaths. The prequel to the modern crisis.",
        "briefing": "THE MASS CASUALTY SIGNAL. Before the 2024 Heat Belt, this event killed ~3,500 people. "
        "Roads melted in Delhi. It established the lethal trend for South Asia: pre-monsoon heat + high humidity.\n\n"

        "Station Records: Bhubaneswar 29.2°C, Dhaka 28.0°C.\n"
        "Regional Map Peak: ~30.0°C (Coastal Andhra Pradesh).\n\n"
        
        "SOURCE: IMD; CNN Reports"
    },

    "Iran Bandar Mahshahr (July 2015)": {
        "id": "iran_2015",
        "date": "2015-07-31",
        "lat_range": range(34, 22, -1),
        "lon_range": range(44, 58, 1),    
        "focus_val_min": 24.0,              
        "description": "The Warning Shot. Heat Index 74°C.",
        "briefing": "THE NEAR BREACH. Before 2024, this was the record holder. Bandar Mahshahr hit a Heat Index of 74°C (165°F). "
        "The map illustrates the 'Coastal Resolution Gap':\n\n"

        "Station Record: Bandar Mahshahr 34.6°C (Near-Theoretical Limit).\n"
        "Regional Map Peak: ~31.5°C (Grid Average).\n\n"

        "SOURCE: Pal & Eltahir (2016)"
    },

    "SE Asia Super El Nino (April 2016)": {
        "id": "se_asia_2016",
        "date": "2016-04-12",
        "lat_range": range(25, 10, -2),   
        "lon_range": range(95, 110, 2),   
        "focus_val_min": 24.0,              
        "description": "Super El Niño event. Records broken across Thailand/Laos.",
        "briefing": "THE EL NINO SPIKE. A powerful El Niño superimposed on global warming triggered the longest heatwave in 65 years. "
        "Thailand consumed record power; schools closed.\n\n"
        
        "Station Record: Bangkok 30.2°C.\n"
        "Regional Map Peak: ~29.0°C.\n\n"
        
        "SOURCE: WMO; Thai Met Dept"
    },    

    "Japan Heat Wave (July 2018)": {
        "id": "japan_2018",
        "date": "2018-07-23",
        "lat_range": range(40, 32, -2),   
        "lon_range": range(130, 145, 2),  
        "focus_val_min": 24.0,              
        "description": "Declared a 'Natural Disaster'. 1,000+ deaths.",
        "briefing": "THE DEMOGRAPHIC TRAP. Kumagaya hit 41.1°C air temp. Despite high-tech infrastructure, over 1,000 people died, "
        "highlighting the vulnerability of aging populations to wet-bulb stress.\n\n"
        
        "Station Record: Kumagaya 28.0°C.\n"
        "Regional Map Peak: ~27.5°C.\n\n"
        
        "SOURCE: JMA; Ibithaj et al. (2020)"
    },

    "Europe Heat Wave (July 2019)": {
        "id": "europe_2019",
        "date": "2019-07-25",
        "lat_range": range(53, 42, -2),   # EXPANDED: Up to 53N (captures Amsterdam)
        "lon_range": range(0, 15, 2),     
        "focus_val_min": 24.0,              
        "description": "Records shattered. France hits 46°C.",
        "briefing": "THE ACCELERATION. Paris broke its all-time record. Unlike 2003, mortality was lower due to adaptation, " 
        "but the *intensity* proved the climate had fundamentally shifted.\n\n"
        
        "Station Record: Paris 23.9°C (Dry Heat Event).\n"
        "Regional Map Peak: ~24.5°C.\n\n"
        
        "SOURCE: Meteo France; WWA"
    },   

    "Siberia Arctic Breach (June 2020)": {
        "id": "siberia_2020",
        "date": "2020-06-20",
        "lat_range": range(72, 60, -2),   
        "lon_range": range(125, 145, 2),  
        "focus_val_min": 18.0,            # LOWER THRESHOLD for Arctic
        "description": "38°C (100°F) in the Arctic Circle.",
        "briefing": "PLANETARY STATE SHIFT. Verkhoyansk hit 38°C, the highest temperature ever recorded north of the Arctic Circle. "
        "While wet-bulb stress was low (dry heat), the *anomaly* was +18°C above normal, triggering massive peat fires and permafrost melt.\n\n"
        
        "Station Record: Verkhoyansk 38.0°C (Air).\n"
        "Regional Map Peak: ~23.0°C (Wet Bulb).\n\n"
        
        "SOURCE: WMO; Copernicus"
    },

    "Pacific NW Heat Dome (June 2021)": {
        "id": "pnw_heat_dome",
        "date": "2021-06-28",
        "lat_range": range(60, 40, -2),   
        "lon_range": range(-135, -110, 2),
        "focus_val_min": 24.0,              
        "description": "Extreme anomaly in high latitudes.",
        "briefing": "THE 1-IN-1000 YEAR EVENT. Lytton, BC broke records (49.6°C). The rapid onset shocked the unacclimatized population. " 
        "Combined death toll estimated at over 1,200.\n\n"
        
        "Station Record: Portland 27.3°C.\n"
        "Regional Map Peak: ~26.0°C.\n\n"
        
        "SOURCE: BC Coroners Service; CDC"
    },

    "China Yangtze Basin (Aug 2022)": {
        "id": "china_2022",
        "date": "2022-08-20",
        "lat_range": range(34, 26, -2),   
        "lon_range": range(102, 123, 2),  # EXPANDED: 102E (Chengdu) to 123E (Shanghai)
        "focus_val_min": 24.0,              
        "description": "The 70-day mega-heatwave. Industrial shutdown.",
        "briefing": "SYSTEMIC FAILURE. The Yangtze river dried up, cutting hydropower to the very region needing AC. " 
        "The event caused a massive industrial shutdown and reports of significant excess mortality.\n\n" 
        
        "Station Record: Wuhan 29.5°C.\n"
        "Regional Map Peak: ~30.0°C.\n\n"
        
        "SOURCE: World Weather Attribution (WWA)"
    },

    # --- CURRENT CRISIS ---
    "Amazon 'Boiling River' (Sept 2023)": {
        "id": "amazon_2023",
        "date": "2023-09-25",
        "lat_range": range(2, -10, -2),   
        "lon_range": range(-70, -55, 2),  
        "focus_val_min": 24.0,              
        "description": "Ecological collapse. River temperatures hit 39°C.",
        "briefing": "THE BIOSPHERE LIMIT. A severe drought heated the Rio Negro to 39°C. Mortality was ecological: 150+ river dolphins boiled alive. " 
        "Indigenous communities faced critical water shortages.\n\n"
        
        "Station Record: Tefé 28.5°C.\n"
        "Regional Map Peak: ~27.9°C.\n\n"
        
        "SOURCE: Mamirauá Institute"
    },

    "Rio 'Heat Index 59' (Nov 2023)": {
        "id": "rio_2023",
        "date": "2023-11-18",
        "lat_range": range(-20, -25, -1),   
        "lon_range": range(-45, -40, 1),    
        "focus_val_min": 24.0,              
        "description": "The 'Taylor Swift' heatwave. Heat Index 59.7°C.",
        "briefing": "THE CULTURAL LIMIT. A massive humidity dome over Rio drove the Heat Index to 59.7°C. "
        "The death of a fan at a major concert forced the industry to recognize heat as a mass-casualty threat.\n\n"
        
        "Station Record: Marambaia 29.5°C.\n"
        "Regional Map Peak: ~28.5°C.\n\n"
        
        "SOURCE: INMET; Local Authorities"
    },

    "Mali/Sahel (April 2024)": {
        "id": "mali_2024",
        "date": "2024-04-03",
        "lat_range": range(22, 4, -1),
        "lon_range": range(-17, 10, 1),
        "focus_val_min": 24.0,              
        "description": "The forgotten heatwave. Temps hit 48.5°C.",
        "briefing": "THE EQUATORIAL TRAP. Bamako, Mali saw temperatures of 48.5°C. Gabriel Touré Hospital reported 102 deaths in just 4 days. " 
        "Total regional excess mortality likely exceeded 3,000.\n\n"
        
        "Station Record: Kayes 28.9°C.\n"
        "Regional Map Peak: ~28.6°C.\n\n"
        
        "SOURCE: Gabriel Touré Hospital; WWA"
    },

    "The Asian Heat Belt (Delhi/Gulf - May 2024)": {
        "id": "delhi_heat_wave",
        "date": "2024-05-29",
        "lat_range": range(35, 5, -3),    
        "lon_range": range(40, 110, 3),   
        "focus_val_min": 24.0,              
        "description": "A trans-national event affecting 1 Billion people.",
        "briefing": "THE INVISIBLE DISASTER. A 'Heat Belt' stretched 5,000km from Riyadh to Bangkok. This visualization reveals a continuous "
        "corridor of lethal wet-bulb potential overlaying the world's densest population centers.\n\n"
        
        "Station Record: Kolkata 31.6°C (Biological Breach).\n"
        "Regional Map Peak: ~31.0°C.\n\n"
        
        "SOURCE: IMD; WWA; Local Reports"
    },

    "Persian Gulf (July 2024)": {
        "id": "persian_gulf_2024",
        "date": "2024-07-17",
        "lat_range": range(35, 20, -2),   
        "lon_range": range(45, 60, 2),    
        "focus_val_min": 24.0,              
        "description": "Breaching the theoretical limit.",
        "briefing": "THE BLACK SWAN. Stations recorded 35°C Wet Bulb. Remarkably, mortality was minimal due to " 
        "near-universal air conditioning. This illustrates the 'Adaptation Gap': money bought survival in a lethal environment.\n\n"
        
        "Station Record: Dubai 31.4°C.\n"
        "Regional Map Peak: ~31.5°C.\n\n"
        
        "SOURCE: NOAA; Raymond et al." 
    },

    "Australia Heat Dome (Dec 2024)": {
        "id": "australia_heat_dome", 
        "date": "2024-12-19",
        "lat_range": range(5, -60, -4),   
        "lon_range": range(-180, 180, 4), 
        "focus_val_min": 24.0,              
        "description": "Peak heating in the Southern Hemisphere.",
        "briefing": "SOUTHERN HEMISPHERE MAX. While the Australian interior baked in extreme *dry* heat (45°C+), the lethal *wet-bulb* peak "
        "shifted north into the tropical convergence zone. The humidity trap over Java created higher physiological stress than the Outback.\n\n"
        
        "Station Record: Jakarta 27.2°C (Wet Bulb Peak).\n"
        "Regional Map Peak: ~25.5°C (Northern Australia).\n\n"
        
        "SOURCE: BOM; Health Dept" 
    },

    "Pakistan Heat Wave (June 2025)": {
        "id": "pakistan_2025",
        "date": "2025-06-22",
        "lat_range": range(34, 23, -2),   # EXPANDED: Down to 23N (captures Karachi 24.9N)
        "lon_range": range(66, 76, 2),    
        "focus_val_min": 24.0,              
        "description": "The 'Unlivable' Summer. Heat Index 55°C+.",
        "briefing": "THE THERMODYNAMIC TRAP. Heat trough + Monsoon moisture. Local NGOs estimated 1,500+ excess deaths in Sindh province alone, "
        "as hospitals were overwhelmed by kidney failure cases.\n\n"
        
        "Station Record: Karachi 28.7°C.\n"
        "Regional Map Peak: ~29.0°C.\n\n"
        
        "SOURCE: NDMA; Edhi Foundation"
    },

    "US Grid-Stress Heat Dome (June 2025)": {
        "id": "us_grid_2025",
        "date": "2025-06-25",
        "lat_range": range(45, 30, -2),   
        "lon_range": range(-95, -70, 2),  
        "focus_val_min": 24.0,
        "description": "Infrastructure failure event. 255 million affected.",
        "briefing": "THE GRID TRAP. A heat dome spanned from Chicago to Atlanta. Energy demand shattered records, forcing rolling blackouts. "
        "It proved that in a fully adapted society, the grid itself is the point of failure.\n\n"
        
        "Station Record: St. Louis 29.1°C.\n"
        "Regional Map Peak: ~29.0°C.\n\n"
        
        "SOURCE: NOAA; NERC"
    },

    "Amazon Tipping Point Drought (Sept 2025)": {
        "id": "amazon_drought_2025",
        "date": "2025-09-15",
        "lat_range": range(5, -15, -2),   
        "lon_range": range(-75, -50, 2),  
        "focus_val_min": 24.0,
        "description": "Failure of the 'Flying Rivers'. Historic low water.",
        "briefing": "ECOLOGICAL COLLAPSE. Following the 2023 drought, 2025 pushed the basin past the tipping point. "
        "Major tributaries like the Madeira hit historic lows. The rainforest temporarily became a net carbon source.\n\n"
        
        "Station Record: Manaus 28.2°C.\n"
        "Regional Map Peak: ~28.0°C.\n\n"
        
        "SOURCE: INPE; MapBiomas"
    }
}

# ==========================================
#       EMBEDDED POPULATION DATABASE
# ==========================================
POPULATION_HUBS = {
    "nyc_1948": [
        {"name": "New York City (Station: 29.5°C)", "lat": 40.7128, "lon": -74.0060, "pop": 7800000}, 
        {"name": "Philadelphia (Station: 28.7°C)", "lat": 39.9526, "lon": -75.1652, "pop": 2000000},
        {"name": "Boston", "lat": 42.3601, "lon": -71.0589, "pop": 800000},
        # ADDED due to range expansion (South to 37N):
        {"name": "Baltimore", "lat": 39.2904, "lon": -76.6122, "pop": 950000},
        {"name": "Washington DC", "lat": 38.9072, "lon": -77.0369, "pop": 800000}
    ],

    "st_louis_1954": [
        {"name": "East St. Louis (Record: 117°F)", "lat": 38.6245, "lon": -90.1506, "pop": 80000},
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 850000}, # Higher pop in 1950s
        {"name": "Springfield", "lat": 39.7817, "lon": -89.6501, "pop": 100000}
    ],

    "la_1955": [
        {"name": "Los Angeles (Record: 110°F)", "lat": 34.0522, "lon": -118.2437, "pop": 2200000}, # 1950s pop
        {"name": "Long Beach", "lat": 33.7701, "lon": -118.1937, "pop": 250000},
        {"name": "Santa Monica", "lat": 34.0195, "lon": -118.4912, "pop": 75000},
        {"name": "Anaheim", "lat": 33.8366, "lon": -117.9143, "pop": 30000} # Disneyland opened 1955!
    ],

    "st_louis_nyc_1966": [
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 700000},
        {"name": "New York City", "lat": 40.7128, "lon": -74.0060, "pop": 7800000},
        {"name": "Philadelphia", "lat": 39.9526, "lon": -75.1652, "pop": 2000000},
        {"name": "Cincinnati", "lat": 39.1031, "lon": -84.5120, "pop": 500000},
        {"name": "Indianapolis", "lat": 39.7684, "lon": -86.1581, "pop": 500000}
    ],

    "uk_1976": [
        {"name": "London (Station: 21.5°C)", "lat": 51.5074, "lon": -0.1278, "pop": 6800000}, # 1976 est
        {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904, "pop": 1000000},
        {"name": "Southampton", "lat": 50.9097, "lon": -1.4044, "pop": 200000}
    ],

    "us_1980": [
        {"name": "Memphis (Station: 28.8°C)", "lat": 35.1495, "lon": -90.0490, "pop": 650000},
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 450000},
        {"name": "Kansas City", "lat": 39.0997, "lon": -94.5786, "pop": 450000},
        # ADDED due to range expansion (South to 30N, West to -98W):
        {"name": "Dallas", "lat": 32.7767, "lon": -96.7970, "pop": 900000},
        {"name": "Jackson (MS)", "lat": 32.2988, "lon": -90.1848, "pop": 200000}
    ],

    "athens_1987": [
        {"name": "Athens (Station: 25.7°C)", "lat": 37.9838, "lon": 23.7275, "pop": 3000000},
        {"name": "Patras", "lat": 38.2466, "lon": 21.7346, "pop": 150000},
        # ADDED due to range expansion (North to 41N):
        {"name": "Thessaloniki", "lat": 40.6401, "lon": 22.9444, "pop": 800000}
    ],

    "chicago_1995": [
        {"name": "Chicago (Station: 28.3°C)", "lat": 41.8781, "lon": -87.6298, "pop": 2700000},
        {"name": "Milwaukee", "lat": 43.0389, "lon": -87.9065, "pop": 570000},
        {"name": "Gary", "lat": 41.5934, "lon": -87.3464, "pop": 75000}
    ],    

    "europe_2003": [
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "pop": 2100000},
        {"name": "London", "lat": 51.5074, "lon": -0.1278, "pop": 8900000},
        {"name": "Milan", "lat": 45.4642, "lon": 9.1900, "pop": 1350000},
        {"name": "Rome (Station: 25.2°C)", "lat": 41.9028, "lon": 12.4964, "pop": 2800000},
        # ADDED due to range expansion (North to 53N):
        {"name": "Berlin", "lat": 52.5200, "lon": 13.4050, "pop": 3600000},
        {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "pop": 820000}
    ],   

    "russia_2010": [
        {"name": "Moscow", "lat": 55.7558, "lon": 37.6173, "pop": 11500000},
        {"name": "St. Petersburg (Station: 23.4°C)", "lat": 59.9311, "lon": 30.3609, "pop": 5400000}, # Added
        {"name": "Nizhny Novgorod", "lat": 56.3269, "lon": 44.0059, "pop": 1250000},
        {"name": "Voronezh", "lat": 51.6755, "lon": 39.2089, "pop": 1000000},
        {"name": "Helsinki", "lat": 60.1699, "lon": 24.9384, "pop": 650000} # Added context
    ],

    "india_pak_2015": [     # May 2015 Event
        {"name": "Karachi", "lat": 24.8607, "lon": 67.0011, "pop": 16000000},
        {"name": "Hyderabad (Pak)", "lat": 25.3960, "lon": 68.3578, "pop": 1700000},
        {"name": "New Delhi", "lat": 28.6139, "lon": 77.2090, "pop": 26000000},
        {"name": "Nagpur", "lat": 21.1458, "lon": 79.0882, "pop": 2400000},
        {"name": "Hyderabad (India)", "lat": 17.3850, "lon": 78.4867, "pop": 10000000},
        {"name": "Vijayawada", "lat": 16.5062, "lon": 80.6480, "pop": 1500000},
        {"name": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "pop": 8000000},
        {"name": "Bhubaneswar (Station: 29.2°C)", "lat": 20.2961, "lon": 85.8245, "pop": 1100000},
        {"name": "Dhaka (Station: 28.0°C)", "lat": 23.8103, "lon": 90.4125, "pop": 22000000}, # Added: Eastern Limit
        {"name": "Muscat", "lat": 23.5859, "lon": 58.4059, "pop": 1500000}   # Added: Western Limit
    ],

    "iran_2015": [
        # UPDATE: Added "(Station: 34.6°C)" to the name to flag the ERA5 data gap
        {"name": "Bandar Mahshahr (Station: 34.6°C)", "lat": 30.5583, "lon": 49.1983, "pop": 160000},
        
        {"name": "Ahvaz", "lat": 31.3183, "lon": 48.6706, "pop": 1100000},
        {"name": "Basra", "lat": 30.5081, "lon": 47.7835, "pop": 1300000},
        {"name": "Kuwait City", "lat": 29.3759, "lon": 47.9774, "pop": 3000000},
        {"name": "Doha", "lat": 25.2854, "lon": 51.5310, "pop": 650000},
        {"name": "Manama", "lat": 26.2285, "lon": 50.5860, "pop": 200000},
        {"name": "Dammam", "lat": 26.4207, "lon": 50.0888, "pop": 1200000},
        {"name": "Nasiriyah", "lat": 31.0580, "lon": 46.2573, "pop": 550000},
        {"name": "Liwa Oasis", "lat": 23.1323, "lon": 53.7966, "pop": 20000}
    ],

    "se_asia_2016": [
        {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018, "pop": 10000000},
        {"name": "Chiang Mai", "lat": 18.7061, "lon": 98.9817, "pop": 1200000},
        {"name": "Vientiane", "lat": 17.9757, "lon": 102.6331, "pop": 950000},
        {"name": "Phnom Penh", "lat": 11.5564, "lon": 104.9282, "pop": 2100000}
    ],

    "japan_2018": [
        {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503, "pop": 14000000},
        {"name": "Kumagaya (Station: 28.0°C)", "lat": 36.1473, "lon": 139.3886, "pop": 200000},
        {"name": "Nagoya", "lat": 35.1815, "lon": 136.9066, "pop": 2300000}
    ],

    "europe_2019": [
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "pop": 2100000},
        {"name": "Brussels", "lat": 50.8503, "lon": 4.3517, "pop": 1200000},
        {"name": "Frankfurt", "lat": 50.1109, "lon": 8.6821, "pop": 750000},
        {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "pop": 820000}
    ],

    "siberia_2020": [
        {"name": "Verkhoyansk", "lat": 67.5447, "lon": 133.3850, "pop": 1300},
        {"name": "Yakutsk", "lat": 62.0397, "lon": 129.7422, "pop": 300000}
    ],

    "pnw_heat_dome": [      # 2021 Event
        {"name": "Seattle", "lat": 47.6062, "lon": -122.3321, "pop": 737000},
        {"name": "Portland (Station: 27.3°C)", "lat": 45.5152, "lon": -122.6784, "pop": 650000},
        {"name": "Vancouver", "lat": 49.2827, "lon": -123.1207, "pop": 675000},
        {"name": "Lytton", "lat": 50.2333, "lon": -121.5833, "pop": 250}, 
        {"name": "Salem", "lat": 44.9429, "lon": -123.0351, "pop": 175000}
    ],

    "china_2022": [
        {"name": "Wuhan (Station: 29.5°C)", "lat": 30.5928, "lon": 114.3055, "pop": 11000000},
        {"name": "Chongqing", "lat": 29.5630, "lon": 106.5516, "pop": 15800000},
        {"name": "Nanjing", "lat": 32.0603, "lon": 118.7969, "pop": 8500000},
        # ADDED due to range expansion (East to 123E, West to 102E):
        {"name": "Shanghai", "lat": 31.2304, "lon": 121.4737, "pop": 26300000},
        {"name": "Chengdu", "lat": 30.5728, "lon": 104.0668, "pop": 16000000}
    ],

    "amazon_2023": [
        {"name": "Manaus", "lat": -3.1190, "lon": -60.0217, "pop": 2200000},
        {"name": "Tefé", "lat": -3.3542, "lon": -64.7115, "pop": 60000},
        {"name": "Coari", "lat": -4.0849, "lon": -63.1417, "pop": 85000}
    ],

    "rio_2023": [
        {"name": "Rio de Janeiro (Station: 29.5°C)", "lat": -22.9068, "lon": -43.1729, "pop": 6700000},
        {"name": "Sao Paulo", "lat": -23.5505, "lon": -46.6333, "pop": 12300000},
        {"name": "Santos", "lat": -23.9618, "lon": -46.3322, "pop": 430000}
    ],

    "mali_2024": [
        {"name": "Bamako", "lat": 12.6392, "lon": -8.0029, "pop": 2400000},
        {"name": "Kayes", "lat": 14.4469, "lon": -11.4445, "pop": 127000},
        {"name": "Segou", "lat": 13.4416, "lon": -6.2163, "pop": 130000},
        {"name": "Ouagadougou", "lat": 12.3714, "lon": -1.5197, "pop": 2500000},
        {"name": "Niamey", "lat": 13.5116, "lon": 2.1254, "pop": 1000000},
        {"name": "Kano", "lat": 12.0022, "lon": 8.5920, "pop": 4000000}
    ],

    "delhi_heat_wave": [        # May 2024 Event
        {"name": "Riyadh", "lat": 24.7136, "lon": 46.6753, "pop": 7600000},
        {"name": "Dubai", "lat": 25.2048, "lon": 55.2708, "pop": 3300000},
        {"name": "Kuwait City", "lat": 29.3759, "lon": 47.9774, "pop": 3100000},
        {"name": "Baghdad", "lat": 33.3152, "lon": 44.3661, "pop": 7100000},
        {"name": "Basra", "lat": 30.5081, "lon": 47.7835, "pop": 1300000},
        {"name": "Karachi", "lat": 24.8607, "lon": 67.0011, "pop": 16000000},
        {"name": "Lahore", "lat": 31.5204, "lon": 74.3587, "pop": 13000000},
        {"name": "Jacobabad", "lat": 28.2835, "lon": 68.4388, "pop": 200000},
        {"name": "New Delhi", "lat": 28.6139, "lon": 77.2090, "pop": 32000000},
        {"name": "Lucknow", "lat": 26.8467, "lon": 80.9462, "pop": 3800000},
        {"name": "Jaipur", "lat": 26.9124, "lon": 75.7873, "pop": 4000000},
        {"name": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "pop": 8200000},
        {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777, "pop": 21000000},
        {"name": "Kolkata (Station: 31.6°C)", "lat": 22.5726, "lon": 88.3639, "pop": 15000000},
        {"name": "Patna", "lat": 25.5941, "lon": 85.1376, "pop": 2500000},
        {"name": "Bhubaneswar", "lat": 20.2961, "lon": 85.8245, "pop": 1100000},
        {"name": "Dhaka", "lat": 23.8103, "lon": 90.4125, "pop": 22000000},
        {"name": "Chittagong", "lat": 22.3569, "lon": 91.7832, "pop": 5000000},
        {"name": "Yangon", "lat": 16.8409, "lon": 96.1735, "pop": 5500000},
        {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018, "pop": 10700000},
        {"name": "Ho Chi Minh City", "lat": 10.8231, "lon": 106.6297, "pop": 9000000}
    ],

    "persian_gulf_2024": [      # July 2024 Event
        {"name": "Dubai (Station: 31.4°C)", "lat": 25.276987, "lon": 55.296249, "pop": 3300000},
        {"name": "Doha", "lat": 25.2854, "lon": 51.5310, "pop": 2300000},
        {"name": "Bandar Abbas", "lat": 27.1832, "lon": 56.2666, "pop": 526000},
        {"name": "Abu Dhabi", "lat": 24.4539, "lon": 54.3773, "pop": 1450000}
    ],

    "australia_heat_dome": [
        {"name": "Jakarta (Station: 27.2°C)", "lat": -6.2088, "lon": 106.8456, "pop": 10500000}, # Added as the primary anchor
        {"name": "Darwin", "lat": -12.4634, "lon": 130.8456, "pop": 150000},
        {"name": "Alice Springs", "lat": -23.6980, "lon": 133.8807, "pop": 26000},
        {"name": "Mount Isa", "lat": -20.7256, "lon": 139.4927, "pop": 18000}
    ],

    "pakistan_2025": [
        {"name": "Jacobabad", "lat": 28.2835, "lon": 68.4388, "pop": 200000}, 
        {"name": "Sibi", "lat": 29.5448, "lon": 67.8764, "pop": 115000},
        {"name": "Karachi (Station: 28.7°C)", "lat": 24.8607, "lon": 67.0011, "pop": 14900000},
        {"name": "Sukkur", "lat": 27.7131, "lon": 68.8492, "pop": 500000}
    ],

    "us_grid_2025": [
        {"name": "Chicago", "lat": 41.8781, "lon": -87.6298, "pop": 2700000},
        {"name": "Washington DC", "lat": 38.9072, "lon": -77.0369, "pop": 700000},
        {"name": "Atlanta", "lat": 33.7490, "lon": -84.3880, "pop": 500000},
        {"name": "New York City", "lat": 40.7128, "lon": -74.0060, "pop": 8000000},
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 300000}
    ],

    "amazon_drought_2025": [
        {"name": "Manaus", "lat": -3.1190, "lon": -60.0217, "pop": 2200000},
        {"name": "Santarém", "lat": -2.4430, "lon": -54.7081, "pop": 300000},
        {"name": "Iquitos (Peru)", "lat": -3.7437, "lon": -73.2516, "pop": 480000},
        {"name": "Porto Velho", "lat": -8.7612, "lon": -63.9039, "pop": 540000}
    ]    
}

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ==========================================
#           GUI SELECTOR CLASS
# ==========================================
class MissionSelector:
    def __init__(self):
        self.selected_mission = None
        self.root = tk.Tk()
        self.root.title("Scenario Generator v5.2")
        self.root.geometry("450x500")
        
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 11), padding=10)
        
        lbl = tk.Label(self.root, text="Select Simulation Scenario", font=("Helvetica", 14, "bold"))
        lbl.pack(pady=15)

        self.listbox = tk.Listbox(self.root, height=12, font=("Helvetica", 11))
        self.listbox.pack(padx=20, pady=5, fill=tk.X)
        
        self.scenario_keys = list(SCENARIOS.keys())
        for name in self.scenario_keys:
            self.listbox.insert(tk.END, name)
            
        self.desc_label = tk.Label(self.root, text="Select a scenario to view details.", 
                                   fg="gray", wraplength=400)
        self.desc_label.pack(pady=10)
        
        self.listbox.bind('<<ListboxSelect>>', self.update_desc)

        btn = tk.Button(self.root, text="GENERATE GOOGLE EARTH KML LAYER", 
                        bg="#d1e7dd", fg="#0f5132", font=("Helvetica", 11, "bold"),
                        command=self.confirm_selection)
        btn.pack(pady=20, fill=tk.X, padx=50)

    def update_desc(self, event):
        selection = self.listbox.curselection()
        if selection:
            name = self.scenario_keys[selection[0]]
            desc = SCENARIOS[name]["description"]
            date = SCENARIOS[name]["date"]
            self.desc_label.config(text=f"{desc}\nTarget Date: {date}", fg="black")

    def confirm_selection(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a scenario.")
            return
        
        name = self.scenario_keys[selection[0]]
        self.selected_mission = SCENARIOS[name]
        self.root.destroy() 

    def run(self):
        self.root.mainloop()
        return self.selected_mission

# ==========================================
#             SYSTEM ENGINE
# ==========================================

def calculate_wet_bulb(T, RH):
    tw = (T * np.arctan(0.151977 * (RH + 8.313659)**0.5) +
          np.arctan(T + RH) - np.arctan(RH - 1.676331) +
          0.00391838 * (RH)**1.5 * np.arctan(0.023101 * RH) -
          4.686035)
    return tw

def get_cache_path(date_str):
    return os.path.join(DATA_DIR, f"weather_cache_{date_str}.json")

def load_cache(path):
    if os.path.exists(path):
        print(f"Loading database: {path}")
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_cache(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

def generate_popup_html(val, lat, lon):
    if val >= 31: 
        risk_color, risk_text = "#000000", "LETHAL (Vecellio et al.)"
        desc = "<b>UNCOMPENSABLE HEAT STRESS:</b><br>Core body temperature will rise continuously. Physiological cooling failed. Fatal without aggressive intervention."
    elif val >= 28: 
        risk_color, risk_text = "#800080", "EXTREME (Raymond et al.)"
        desc = "<b>CRITICAL RISK:</b><br>Heat stroke imminent for outdoor laborers. Society-wide cooling infrastructure required."
    elif val >= 26:
        risk_color, risk_text = "#FF0000", "HIGH RISK (Carter/Foster)"
        desc = "<b>SEVERE STRESS:</b><br>Continuous physical activity dangerous (Foster). Vulnerable hearts fail (Carter)."
    else:
        risk_color, risk_text = "#FFA500", "CAUTION"
        desc = "<b>ELEVATED STRESS:</b><br>Prolonged exposure may cause fatigue."

    percent = min(100, max(0, (val - 22) / (31 - 22) * 100))
    
    html = f"""
    <div style="font-family: Arial, sans-serif; width: 300px; padding: 10px;">
        <h2 style="margin: 0; color: {risk_color};">{val:.1f}°C</h2>
        <h4 style="margin: 0; color: #555;">WET BULB TEMPERATURE</h4>
        <hr>
        <p style="font-weight: bold; color: {risk_color};">{risk_text}</p>
        <p style="font-size: 13px;">{desc}</p>
        <div style="background-color: #ddd; height: 15px; width: 100%; border-radius: 5px; margin-top: 10px;">
            <div style="background-color: {risk_color}; height: 100%; width: {percent}%; border-radius: 5px;"></div>
        </div>
        <p style="font-size: 10px; color: #666; text-align: right;">Bio-Limit: 31°C (Vecellio et al.)</p>
    </div>
    """
    return html

def create_legend_card():
    filename = "legend_risk_index_cited.png"
    filepath = os.path.join(DATA_DIR, filename)
    fig = plt.figure(figsize=(3.2, 3.5), dpi=120)
    
    # ADJUSTED TRANSPARENCY: 0.7
    fig.patch.set_facecolor('white')
    fig.patch.set_alpha(0.7)
    
    ax = fig.add_subplot(111)
    ax.axis('off')
    
    legend_elements = [
        mpatches.Patch(color='#000000', label='> 31°C: Lethal (Vecellio)'),
        mpatches.Patch(color='#800080', label='28-31°C: Extreme (Raymond)'),
        mpatches.Patch(color='#FF0000', label='26-28°C: High Risk (Carter)'),
        mpatches.Patch(color='#FFA500', label='24-26°C: Caution (Foster)'),
        mpatches.Patch(color='#008000', label='< 24°C: Safe'),
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 0.93), frameon=False, fontsize=9)
    plt.text(0.5, 0.97, "Wet Bulb Bio-Limits", ha='center', va='center', transform=ax.transAxes, fontweight='bold', fontsize=11)
    
    citations = (
        "EVIDENCE BASE:\n"
        "1. Vecellio et al. (2022): 31°C uncompensable limit.\n"
        "2. Raymond et al. (2020): 28°C+ societal breakdown.\n"
        "3. Carter et al. (2023): Heart strain onset.\n"
        "4. Foster et al. (2021): Labor capacity loss."
    )
    plt.text(0.5, 0.05, citations, ha='center', va='bottom', transform=ax.transAxes, fontsize=7, color='#333', style='italic')
    
    plt.savefig(filepath, bbox_inches='tight', pad_inches=0.1, transparent=False)
    plt.close()
    return filename

def create_intel_card(mission):
    filename = f"{mission['date']}_intel_{mission['id']}.png"
    filepath = os.path.join(DATA_DIR, filename)
    
    fig = plt.figure(figsize=(4, 3.0), dpi=120) 
    
    # ADJUSTED TRANSPARENCY: 0.7
    fig.patch.set_facecolor('#f8f9fa')
    fig.patch.set_alpha(0.7)
    
    ax = fig.add_subplot(111)
    ax.axis('off')
    
    plt.text(0.05, 0.9, f"HEAT WAVE: {mission['id'].upper()}", transform=ax.transAxes, fontsize=10, fontweight='bold', color='#333')
    plt.text(0.05, 0.82, f"DATE: {mission['date']}", transform=ax.transAxes, fontsize=9, fontfamily='monospace', color='#555')
    plt.plot([0.05, 0.95], [0.78, 0.78], color='black', linewidth=1, transform=ax.transAxes)
    
    briefing = textwrap.fill(mission.get('briefing', "No intel available."), width=40)
    plt.text(0.05, 0.72, briefing, transform=ax.transAxes, fontsize=8, va='top', ha='left', color='#222')
    
    plt.text(0.05, 0.05, "METEO DATA: ERA5 Reanalysis via Open-Meteo API", 
             transform=ax.transAxes, fontsize=6, color='#777', style='italic')

    plt.savefig(filepath, bbox_inches='tight', pad_inches=0.1, transparent=False)
    plt.close()
    return filename

def create_pop_legend_card():
    filename = "legend_impact_pop.png"
    filepath = os.path.join(DATA_DIR, filename)
    
    fig = plt.figure(figsize=(2.5, 3.0), dpi=120)
    fig.patch.set_facecolor('white')
    fig.patch.set_alpha(0.8)
    
    ax = fig.add_subplot(111)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)

    # Red Circle (Megacity)
    c_mega = mpatches.Circle((5, 9), 1.5, facecolor='#ff000066', edgecolor='red', linewidth=1.5)
    ax.add_patch(c_mega)
    plt.text(5, 7.2, "Megacity (>5M)", ha='center', fontsize=7, fontweight='bold')

    # Orange Circle (Major)
    c_major = mpatches.Circle((2.5, 5), 1.2, facecolor='#ffa50066', edgecolor='orange', linewidth=1.5)
    ax.add_patch(c_major)
    plt.text(2.5, 3.5, "Major (>1M)", ha='center', fontsize=7)

    # Yellow Circle (Regional)
    c_reg = mpatches.Circle((7.5, 5), 0.9, facecolor='#ffff0066', edgecolor='#cccc00', linewidth=1.5)
    ax.add_patch(c_reg)
    plt.text(7.5, 3.5, "Region (>500k)", ha='center', fontsize=7)

    plt.text(5, 11, "Population Exposure", ha='center', fontweight='bold', fontsize=9)
    
    plt.savefig(filepath, bbox_inches='tight', pad_inches=0.1, transparent=False)
    plt.close()
    return filename


def create_circle_polygon(lat, lon, radius_km):
    coords = []
    for angle in range(0, 361, 10):
        dx = radius_km * math.cos(math.radians(angle))
        dy = radius_km * math.sin(math.radians(angle))
        dlat = dy / 111.32
        dlon = dx / (40075 * math.cos(math.radians(lat)) / 360)
        coords.append((lon + dlon, lat + dlat))
    return coords

def run_pipeline(mission):
    date = mission["date"]
    mission_id = mission["id"]
    cache_path = get_cache_path(date)
    
    # --- CRASH FIX: Initialize variables ---
    spike_filename = "Not Generated"
    heat_filename = "Not Generated"
    impact_filename = "Not Generated"
    
    print(f"\n--- INITIALIZING SCENARIO: {mission_id.upper()} [{date}] ---")
    legend_file = create_legend_card()
    intel_file = create_intel_card(mission)
    pop_legend_file = create_pop_legend_card() 
    
    db = load_cache(cache_path)
    points_to_fetch = []
    all_points = [(lat, lon) for lat in mission["lat_range"] for lon in mission["lon_range"]]
    for lat, lon in all_points:
        if f"{lat}_{lon}" not in db: points_to_fetch.append((lat, lon))
            
    if points_to_fetch:
        print(f"Status: Missing {len(points_to_fetch)} points. Engaging download...")
        batch_size = 40
        current_lats, current_lons = [], []
        for i, (lat, lon) in enumerate(points_to_fetch):
            current_lats.append(lat)
            current_lons.append(lon)
            if len(current_lats) >= batch_size or i == len(points_to_fetch) - 1:
                try:
                    url = "https://archive-api.open-meteo.com/v1/archive"
                    params = {"latitude": ",".join(map(str, current_lats)), "longitude": ",".join(map(str, current_lons)),
                              "start_date": date, "end_date": date, "hourly": "temperature_2m,relative_humidity_2m", "timezone": "GMT"}
                    r = requests.get(url, params=params)
                    if r.status_code == 429: break
                    r.raise_for_status()
                    data = r.json()
                    if isinstance(data, dict): data = [data]
                    for j, loc_data in enumerate(data):
                        if "hourly" not in loc_data: continue
                        temps = np.array(loc_data["hourly"]["temperature_2m"])
                        rhs = np.array(loc_data["hourly"]["relative_humidity_2m"])
                        max_tw = float(np.max(calculate_wet_bulb(temps, rhs)))
                        db[f"{current_lats[j]}_{current_lons[j]}"] = max_tw
                    save_cache(cache_path, db)
                    current_lats, current_lons = [], []
                    time.sleep(1.5)
                except Exception: break
    
    # --- CRASH FIX: Check if database is empty ---
    if not db:
        messagebox.showerror("Data Error", f"No data retrieved for {date}.\nNote: ERA5 archive begins in 1940.")
        return

    print("Generating Bio-Corrected Spikes and Impact Layer...")
    
    # 1. SPIKES FILE
    spike_filename = os.path.join(DATA_DIR, f"{date}_spikes_{mission_id}.kml")
    kml_spikes = simplekml.Kml()
    kml_spikes.document.name = f"{mission_id} Spikes ({date})"
    
    screen_legend = kml_spikes.newscreenoverlay(name="Legend")
    screen_legend.icon.href = legend_file
    screen_legend.overlayxy = simplekml.OverlayXY(x=0, y=0.1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
    screen_legend.screenxy = simplekml.ScreenXY(x=0, y=0.1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)

    screen_intel = kml_spikes.newscreenoverlay(name="Scenario Intel")
    screen_intel.icon.href = intel_file
    screen_intel.overlayxy = simplekml.OverlayXY(x=0, y=1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
    screen_intel.screenxy = simplekml.ScreenXY(x=0, y=1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)

    # 2. IMPACT FILE
    impact_filename = os.path.join(DATA_DIR, f"{date}_impact_{mission_id}.kml")
    kml_impact = simplekml.Kml()
    kml_impact.document.name = f"{mission_id} Impact ({date})"

    screen_pop = kml_impact.newscreenoverlay(name="Population Legend")
    screen_pop.icon.href = pop_legend_file
    screen_pop.overlayxy = simplekml.OverlayXY(x=1, y=0.1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
    screen_pop.screenxy = simplekml.ScreenXY(x=1, y=0.1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)

    if mission_id in POPULATION_HUBS:
        for city in POPULATION_HUBS[mission_id]:
            pop = city['pop']
            
            # Dynamic Sizing & Coloring
            radius = math.sqrt(pop) / 75
            
            # KML Color Format: aabbggrr (Hex)
            if pop > 5000000:
                color_fill = "660000ff"  # Red (40% opacity)
                color_line = "ff0000ff"  # Red (100% opacity)
                scale_desc = "MEGACITY (>5M)"
            elif pop > 1000000:
                color_fill = "6600a5ff"  # Orange
                color_line = "ff00a5ff"
                scale_desc = "MAJOR HUB (>1M)"
            elif pop > 500000:
                color_fill = "6600ffff"  # Yellow
                color_line = "ff00ffff"
                scale_desc = "REGIONAL (>500k)"
            else:
                color_fill = "66ffffff"  # White
                color_line = "ffffffff"
                scale_desc = "LOCAL"

            poly = kml_impact.newpolygon(name=f"{city['name']} ({pop:,})")
            poly.outerboundaryis = create_circle_polygon(city['lat'], city['lon'], radius)
            poly.style.polystyle.color = color_fill
            poly.style.linestyle.color = color_line
            poly.style.linestyle.width = 2
            
            # Add description for click-intel
            poly.description = f"<b>{city['name']}</b><br>Population: {pop:,}<br>Class: {scale_desc}"
    
    kml_impact.save(impact_filename)

    # Populate Spikes
    min_val = mission["focus_val_min"]
    for key, val in db.items():
        if val < min_val: continue
        lat, lon = map(float, key.split('_'))
        pnt = kml_spikes.newpoint(name=f"{val:.1f}")
        pnt.coords = [(lon, lat)]
        pnt.description = generate_popup_html(val, lat, lon)
        
        height = (val - (min_val - 2)) * 15000 
        pnt.altitudemode = simplekml.AltitudeMode.relativetoground
        pnt.extrude = 1
        pnt.altitude = height
        
        if val >= 31: 
            pnt.style.iconstyle.color = "ff000000" 
            pnt.style.linestyle.color = "ff000000"
        elif val >= 28:
            pnt.style.iconstyle.color = "ff800080"
            pnt.style.linestyle.color = "ff800080"
        elif val >= 26: 
            pnt.style.iconstyle.color = "ff0000ff"
            pnt.style.linestyle.color = "ff0000ff"
        else:
            pnt.style.iconstyle.color = "ff00a5ff"
            pnt.style.linestyle.color = "ff00a5ff"
            
    kml_spikes.save(spike_filename)
    print(f"Saved Spikes: {spike_filename}")
    print(f"Saved Impact: {impact_filename}")

    # 3. HEATMAP FILE
    print("Generating Heatmap...")
    lats, lons, values = [], [], []
    for key, val in db.items():
        if val < 20: continue 
        lat, lon = map(float, key.split('_'))
        lats.append(lat)
        lons.append(lon)
        values.append(val)
    
    # --- CRASH FIX: Check if data exists for heatmap ---
    if lats:
        grid_lat = np.linspace(min(lats), max(lats), 300)
        grid_lon = np.linspace(min(lons), max(lons), 600)
        grid_x, grid_y = np.meshgrid(grid_lon, grid_lat)
        grid_z = griddata((lons, lats), np.array(values), (grid_x, grid_y), method='linear')
        
        img_name = f"{date}_heatmap_{mission_id}.png"
        img_path = os.path.join(DATA_DIR, img_name)
        
        dpi = 150
        fig = plt.figure(figsize=(10, 5), dpi=dpi, frameon=False)
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        levels = np.arange(20, 38, 1)
        ax.contourf(grid_x, grid_y, grid_z, levels=levels, cmap='inferno_r', alpha=0.35)
        ax.contour(grid_x, grid_y, grid_z, levels=levels, colors='black', linewidths=0.5, alpha=0.5)
        plt.savefig(img_path, transparent=True, bbox_inches='tight', pad_inches=0)
        plt.close()

        kml_heat = simplekml.Kml()
        kml_heat.document.name = f"{mission_id} Heatmap ({date})"
        ground = kml_heat.newgroundoverlay(name="Thermal Overlay")
        ground.icon.href = img_name
        ground.latlonbox.north = max(lats)
        ground.latlonbox.south = min(lats)
        ground.latlonbox.east = max(lons)
        ground.latlonbox.west = min(lons)
        
        heat_filename = os.path.join(DATA_DIR, f"{date}_heatmap_{mission_id}.kml")
        kml_heat.save(heat_filename)
        print(f"Saved Heatmap: {heat_filename}")
    else:
        print("Warning: Insufficient data for heatmap generation.")

    messagebox.showinfo("Success", f"Scenario Generated!\n\nFiles Created:\n1. {spike_filename}\n2. {heat_filename}\n3. {impact_filename}")

if __name__ == "__main__":
    app = MissionSelector()
    mission_config = app.run()
    if mission_config:
        run_pipeline(mission_config)