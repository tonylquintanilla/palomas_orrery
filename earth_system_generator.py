import requests
import re
import simplekml
import numpy as np
import time
import json
import os
import textwrap
import math
import zipfile
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.interpolate import griddata
import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
#          SCENARIO CONFIGURATION
# ==========================================
SCENARIOS = {
    "New York City (Aug 1948)": {
        "id": "nyc_1948", "date": "1948-08-26",
        "lat_range": range(45, 37, -1), "lon_range": range(-80, -70, 1), 
        "focus_val_min": 24,              
        "description": "Historical Baseline (Pre-AC Era). 100F+ Temps.",
        "briefing": "THE PRE-COOLING ERA. A massive heatwave hit the Northeast US. In an era before widespread AC, New Yorkers slept on fire escapes. This serves as our 'Historical Baseline'—survivable by the young, lethal to the vulnerable.\n\nStation Records: NYC 29.5°C, Philadelphia 28.7°C.\nRegional Map Peak: ~26.0°C.\n\nSOURCE: NOAA; NY Times Archives"
    },
    "Midwest Torch (July 1954)": {
        "id": "st_louis_1954", "date": "1954-07-14",
        "lat_range": range(42, 34, -1), "lon_range": range(-94, -86, 1), 
        "focus_val_min": 26.0,              
        "description": "All-time state record (117°F). Deaths outnumbered births.",
        "briefing": "THE MIDWEST TORCH. East St. Louis hit 47.2°C (117°F), a record that still stands today. The combination of extreme air temperature and river valley humidity created conditions that overwhelmed the era's limited infrastructure.\n\nStation Record: East St. Louis 117°F (Air Temp).\nRegional Map Peak: ~30.0°C (Wet Bulb Estimate).\n\nSOURCE: Illinois State Water Survey"
    },
    "LA Inferno (Sept 1955)": {
        "id": "la_1955", "date": "1955-09-01",
        "lat_range": range(35, 32, -1), "lon_range": range(-120, -116, 1), 
        "focus_val_min": 22.0,            
        "description": "The 'Forgotten Disaster'. 946 deaths. 110°F.",
        "briefing": "THE COASTAL SURPRISE. A massive high-pressure ridge parked over the West Coast. Downtown LA hit 110°F (43°C), and temps stayed above 100°F for a week. With almost no air conditioning in 1955, the mortality (946 deaths) exceeded most earthquakes, exposing the deadly 'adaptation gap' of coastal cities.\n\nStation Record: Los Angeles 110°F (Air Temp).\nRegional Map Peak: ~26.5°C (Wet Bulb).\n\nSOURCE: LA Almanac; WeatherBug"
    },
    "The Heat Index Event (July 1966)": {
        "id": "st_louis_nyc_1966", "date": "1966-07-12",
        "lat_range": range(42, 37, -1), "lon_range": range(-91, -73, 2),  
        "focus_val_min": 25.0,              
        "description": "The event that created the Heat Index metric.",
        "briefing": "THE ORIGIN STORY. A massive heat dome bridged the Midwest and East Coast simultaneously. The sheer misery of high humidity in St. Louis combined with urban heat in NYC caused mass mortality, forcing the NWS to invent the 'Heat Index' to explain why 95°F felt like 105°F.\n\nStation Records: St. Louis 106°F, NYC 103°F.\nRegional Map Peak: ~29.0°C.\n\nSOURCE: National Weather Service"
    },
    "UK Heat Wave (June 1976)": {
        "id": "uk_1976", "date": "1976-06-26",
        "lat_range": range(55, 48, -1), "lon_range": range(-5, 5, 1),
        "focus_val_min": 18.0,
        "description": "The Great Drought. Water rationing and 20% excess deaths.",
        "briefing": "THE DROUGHT TRAP. One of the driest summers in UK history. While absolute temperatures (35.9°C) seem modest, the compound stress of drought led to 20% excess mortality.\n\nStation Record: London 21.5°C.\nRegional Map Peak: ~20.0°C.\n\nSOURCE: Met Office; ONS"
    },
    "US Heat Wave (July 1980)": {
        "id": "us_1980", "date": "1980-07-15",
        "lat_range": range(40, 30, -2), "lon_range": range(-98, -85, 2),  
        "focus_val_min": 24.0,
        "description": "1,700+ deaths. The 'Billion Dollar' heat disaster.",
        "briefing": "THE RUNAWAY HIGH. A massive high-pressure ridge stalled over the central US. Memphis hit 108°F (42°C). It caused >1,700 deaths and $20 billion in agricultural losses.\n\nStation Records: Memphis 28.8°C, Kansas City 28.5°C.\nRegional Map Peak: ~28.0°C.\n\nSOURCE: NOAA; Karl & Quayle (1981)"
    },
    "Athens Heat Wave (July 1987)": {
        "id": "athens_1987", "date": "1987-07-27",
        "lat_range": range(41, 36, -1), "lon_range": range(20, 26, 1),
        "focus_val_min": 23.0,
        "description": "1,300+ deaths. The Urban Heat Island wake-up call.",
        "briefing": "THE CONCRETE TRAP. A week-long heatwave turned Athens into a kiln. The concrete city retained heat overnight, denying physiological recovery. ~1,300 deaths forced a complete overhaul of Greek infrastructure.\n\nStation Record: Athens 25.7°C.\nRegional Map Peak: ~24.0°C.\n\nSOURCE: Metaxas et al. (1991)"
    },
    "Chicago Heat Wave (July 1995)": {
        "id": "chicago_1995", "date": "1995-07-13",
        "lat_range": range(50, 30, -2), "lon_range": range(-100, -80, 2), 
        "focus_val_min": 24.0,
        "description": "The 'silent killer' event. High mortality at lower thresholds.",
        "briefing": "A TRAGEDY OF VULNERABILITY. Wet bulbs hovered in the 'Red Zone'. Lack of AC and the 'Urban Heat Island' effect proved fatal for the elderly. CDC records confirm 739 excess deaths in 5 days.\n\nStation Record: Chicago (Midway) 28.3°C.\nRegional Map Peak: ~29.4°C (Corn Belt Humidity Pool).\n\nSOURCE: CDC; Klinenberg (2002)"
    },
    "Europe (The Great Mortality - Aug 2003)": {
        "id": "europe_2003", "date": "2003-08-10",
        "lat_range": range(53, 40, -2), "lon_range": range(-5, 15, 2),    
        "focus_val_min": 22.0,
        "description": "The event that changed Europe. 70,000+ excess deaths.",
        "briefing": "VULNERABILITY VS EXPOSURE. With <2% AC adoption and aging demographics, this 'moderate' wet-bulb heat became the deadliest natural disaster in modern European history.\n\nStation Record: Rome 25.2°C, Paris 24.1°C.\nRegional Map Peak: ~25.7°C.\n\nSOURCE: Robine et al. (2008); INSERM"
    },
    "Russia Heat Wave (July 2010)": {
        "id": "russia_2010", "date": "2010-07-29",
        "lat_range": range(64, 48, -2), "lon_range": range(25, 55, 2),
        "focus_val_min": 20.0,              
        "description": "55,000+ excess deaths. Smoke and stagnation.",
        "briefing": "THE CONTINENTAL TRAP. A 'blocking high' stalled over Russia. The sheer duration (weeks) + toxic smoke from peat fires caused 55,000 excess deaths, proving that 'safe' wet bulbs are lethal if sustained.\n\nStation Record: St. Petersburg 23.4°C, Moscow 22.8°C.\nRegional Map Peak: ~25.2°C.\n\nSOURCE: Barriopedro et al. (2011)"
    },
    "India/Pakistan (May 2015)": {
        "id": "india_pak_2015", "date": "2015-05-24",
        "lat_range": range(36, 5, -2), "lon_range": range(55, 96, 2),
        "focus_val_min": 24.0,              
        "description": "3,500+ deaths. The prequel to the modern crisis.",
        "briefing": "THE MASS CASUALTY SIGNAL. Before the 2024 Heat Belt, this event killed ~3,500 people. Roads melted in Delhi. It established the lethal trend for South Asia: pre-monsoon heat + high humidity.\n\nStation Records: Bhubaneswar 29.2°C, Dhaka 28.0°C.\nRegional Map Peak: ~30.0°C (Coastal Andhra Pradesh).\n\nSOURCE: IMD; CNN Reports"
    },
    "Iran Bandar Mahshahr (July 2015)": {
        "id": "iran_2015", "date": "2015-07-31",
        "lat_range": range(34, 22, -1), "lon_range": range(44, 58, 1),    
        "focus_val_min": 24.0,              
        "description": "The Warning Shot. Heat Index 74°C.",
        "briefing": "THE NEAR BREACH. Before 2024, this was the record holder. Bandar Mahshahr hit a Heat Index of 74°C (165°F). The map illustrates the 'Coastal Resolution Gap':\n\nStation Record: Bandar Mahshahr 34.6°C (Near-Theoretical Limit).\nRegional Map Peak: ~31.5°C (Grid Average).\n\nSOURCE: Pal & Eltahir (2016)"
    },
    "SE Asia Super El Nino (April 2016)": {
        "id": "se_asia_2016", "date": "2016-04-12",
        "lat_range": range(25, 10, -2), "lon_range": range(95, 110, 2),   
        "focus_val_min": 24.0,              
        "description": "Super El Niño event. Records broken across Thailand/Laos.",
        "briefing": "THE EL NINO SPIKE. A powerful El Niño superimposed on global warming triggered the longest heatwave in 65 years. Thailand consumed record power; schools closed.\n\nStation Record: Bangkok 30.2°C.\nRegional Map Peak: ~29.0°C.\n\nSOURCE: WMO; Thai Met Dept"
    },    
    "Japan Heat Wave (July 2018)": {
        "id": "japan_2018", "date": "2018-07-23",
        "lat_range": range(40, 32, -2), "lon_range": range(130, 145, 2),  
        "focus_val_min": 24.0,              
        "description": "Declared a 'Natural Disaster'. 1,000+ deaths.",
        "briefing": "THE DEMOGRAPHIC TRAP. Kumagaya hit 41.1°C air temp. Despite high-tech infrastructure, over 1,000 people died, highlighting the vulnerability of aging populations to wet-bulb stress.\n\nStation Record: Kumagaya 28.0°C.\nRegional Map Peak: ~27.5°C.\n\nSOURCE: JMA; Ibithaj et al. (2020)"
    },
    "Europe Heat Wave (July 2019)": {
        "id": "europe_2019", "date": "2019-07-25",
        "lat_range": range(53, 42, -2), "lon_range": range(0, 15, 2),     
        "focus_val_min": 24.0,              
        "description": "Records shattered. France hits 46°C.",
        "briefing": "THE ACCELERATION. Paris broke its all-time record. Unlike 2003, mortality was lower due to adaptation, but the *intensity* proved the climate had fundamentally shifted.\n\nStation Record: Paris 23.9°C (Dry Heat Event).\nRegional Map Peak: ~24.5°C.\n\nSOURCE: Meteo France; WWA"
    },   
    "Siberia Arctic Breach (June 2020)": {
        "id": "siberia_2020", "date": "2020-06-20",
        "lat_range": range(72, 60, -2), "lon_range": range(125, 145, 2),  
        "focus_val_min": 18.0,            
        "description": "38°C (100°F) in the Arctic Circle.",
        "briefing": "PLANETARY STATE SHIFT. Verkhoyansk hit 38°C, the highest temperature ever recorded north of the Arctic Circle. While wet-bulb stress was low (dry heat), the *anomaly* was +18°C above normal, triggering massive peat fires and permafrost melt.\n\nStation Record: Verkhoyansk 38.0°C (Air).\nRegional Map Peak: ~23.0°C (Wet Bulb).\n\nSOURCE: WMO; Copernicus"
    },
    "Pacific NW Heat Dome (June 2021)": {
        "id": "pnw_heat_dome", "date": "2021-06-28",
        "lat_range": range(60, 40, -2), "lon_range": range(-135, -110, 2),
        "focus_val_min": 24.0,              
        "description": "Extreme anomaly in high latitudes.",
        "briefing": "THE 1-IN-1000 YEAR EVENT. Lytton, BC broke records (49.6°C). The rapid onset shocked the unacclimatized population. Combined death toll estimated at over 1,200.\n\nStation Record: Portland 27.3°C.\nRegional Map Peak: ~26.0°C.\n\nSOURCE: BC Coroners Service; CDC"
    },
    "China Yangtze Basin (Aug 2022)": {
        "id": "china_2022", "date": "2022-08-20",
        "lat_range": range(34, 26, -2), "lon_range": range(102, 123, 2),  
        "focus_val_min": 24.0,              
        "description": "The 70-day mega-heatwave. Industrial shutdown.",
        "briefing": "SYSTEMIC FAILURE. The Yangtze river dried up, cutting hydropower to the very region needing AC. The event caused a massive industrial shutdown and reports of significant excess mortality.\n\nStation Record: Wuhan 29.5°C.\nRegional Map Peak: ~30.0°C.\n\nSOURCE: World Weather Attribution (WWA)"
    },
    "Amazon 'Boiling River' (Sept 2023)": {
        "id": "amazon_2023", "date": "2023-09-25",
        "lat_range": range(2, -10, -2), "lon_range": range(-70, -55, 2),  
        "focus_val_min": 24.0,              
        "description": "Ecological collapse. River temperatures hit 39°C.",
        "briefing": "THE BIOSPHERE LIMIT. A severe drought heated the Rio Negro to 39°C. Mortality was ecological: 150+ river dolphins boiled alive. Indigenous communities faced critical water shortages.\n\nStation Record: Tefé 28.5°C.\nRegional Map Peak: ~27.9°C.\n\nSOURCE: Mamirauá Institute"
    },
    "Rio 'Heat Index 59' (Nov 2023)": {
        "id": "rio_2023", "date": "2023-11-18",
        "lat_range": range(-20, -25, -1), "lon_range": range(-45, -40, 1),    
        "focus_val_min": 24.0,              
        "description": "The 'Taylor Swift' heatwave. Heat Index 59.7°C.",
        "briefing": "THE CULTURAL LIMIT. A massive humidity dome over Rio drove the Heat Index to 59.7°C. The death of a fan at a major concert forced the industry to recognize heat as a mass-casualty threat.\n\nStation Record: Marambaia 29.5°C.\nRegional Map Peak: ~28.5°C.\n\nSOURCE: INMET; Local Authorities"
    },
    "Mali/Sahel (April 2024)": {
        "id": "mali_2024", "date": "2024-04-03",
        "lat_range": range(22, 4, -1), "lon_range": range(-17, 10, 1),
        "focus_val_min": 24.0,              
        "description": "The forgotten heatwave. Temps hit 48.5°C.",
        "briefing": "THE EQUATORIAL TRAP. Bamako, Mali saw temperatures of 48.5°C. Gabriel Touré Hospital reported 102 deaths in just 4 days. Total regional excess mortality likely exceeded 3,000.\n\nStation Record: Kayes 28.9°C.\nRegional Map Peak: ~28.6°C.\n\nSOURCE: Gabriel Touré Hospital; WWA"
    },
    "The Asian Heat Belt (Delhi/Gulf - May 2024)": {
        "id": "delhi_heat_wave", "date": "2024-05-29",
        "lat_range": range(35, 5, -3), "lon_range": range(40, 110, 3),   
        "focus_val_min": 24.0,              
        "description": "A trans-national event affecting 1 Billion people.",
        "briefing": "THE INVISIBLE DISASTER. A 'Heat Belt' stretched 5,000km from Riyadh to Bangkok. This visualization reveals a continuous corridor of lethal wet-bulb potential overlaying the world's densest population centers.\n\nStation Record: Kolkata 31.6°C (Biological Breach).\nRegional Map Peak: ~31.0°C.\n\nSOURCE: IMD; WWA; Local Reports"
    },
    "Persian Gulf (July 2024)": {
        "id": "persian_gulf_2024", "date": "2024-07-17",
        "lat_range": range(35, 20, -2), "lon_range": range(45, 60, 2),    
        "focus_val_min": 24.0,              
        "description": "Breaching the theoretical limit.",
        "briefing": "THE BLACK SWAN. Stations recorded 35°C Wet Bulb. Remarkably, mortality was minimal due to near-universal air conditioning. This illustrates the 'Adaptation Gap': money bought survival in a lethal environment.\n\nStation Record: Dubai 31.4°C.\nRegional Map Peak: ~31.5°C.\n\nSOURCE: NOAA; Raymond et al." 
    },
    "Australia Heat Dome (Dec 2024)": {
        "id": "australia_heat_dome", "date": "2024-12-19",
        "lat_range": range(5, -60, -4), "lon_range": range(-180, 180, 4), 
        "focus_val_min": 24.0,              
        "description": "Peak heating in the Southern Hemisphere.",
        "briefing": "SOUTHERN HEMISPHERE MAX. While the Australian interior baked in extreme *dry* heat (45°C+), the lethal *wet-bulb* peak shifted north into the tropical convergence zone. The humidity trap over Java created higher physiological stress than the Outback.\n\nStation Record: Jakarta 27.2°C (Wet Bulb Peak).\nRegional Map Peak: ~25.5°C (Northern Australia).\n\nSOURCE: BOM; Health Dept" 
    },
    "Pakistan Heat Wave (June 2025)": {
        "id": "pakistan_2025", "date": "2025-06-22",
        "lat_range": range(34, 23, -2), "lon_range": range(66, 76, 2),    
        "focus_val_min": 24.0,              
        "description": "The 'Unlivable' Summer. Heat Index 55°C+.",
        "briefing": "THE THERMODYNAMIC TRAP. Heat trough + Monsoon moisture. Local NGOs estimated 1,500+ excess deaths in Sindh province alone, as hospitals were overwhelmed by kidney failure cases.\n\nStation Record: Karachi 28.7°C.\nRegional Map Peak: ~29.0°C.\n\nSOURCE: NDMA; Edhi Foundation"
    },
    "US Grid-Stress Heat Dome (June 2025)": {
        "id": "us_grid_2025", "date": "2025-06-25",
        "lat_range": range(45, 30, -2), "lon_range": range(-95, -70, 2),  
        "focus_val_min": 24.0,
        "description": "Infrastructure failure event. 255 million affected.",
        "briefing": "THE GRID TRAP. A heat dome spanned from Chicago to Atlanta. Energy demand shattered records, forcing rolling blackouts. It proved that in a fully adapted society, the grid itself is the point of failure.\n\nStation Record: St. Louis 29.1°C.\nRegional Map Peak: ~29.0°C.\n\nSOURCE: NOAA; NERC"
    },
    "Amazon Tipping Point Drought (Sept 2025)": {
        "id": "amazon_drought_2025", "date": "2025-09-15",
        "lat_range": range(5, -15, -2), "lon_range": range(-75, -50, 2),  
        "focus_val_min": 24.0,
        "description": "Failure of the 'Flying Rivers'. Historic low water.",
        "briefing": "ECOLOGICAL COLLAPSE. Following the 2023 drought, 2025 pushed the basin past the tipping point. Major tributaries like the Madeira hit historic lows. The rainforest temporarily became a net carbon source.\n\nStation Record: Manaus 28.2°C.\nRegional Map Peak: ~28.0°C.\n\nSOURCE: INPE; MapBiomas"
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
        {"name": "Baltimore", "lat": 39.2904, "lon": -76.6122, "pop": 950000},
        {"name": "Washington DC", "lat": 38.9072, "lon": -77.0369, "pop": 800000}
    ],
    "st_louis_1954": [
        {"name": "East St. Louis (Record: 117°F)", "lat": 38.6245, "lon": -90.1506, "pop": 800000},
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 850000}, 
        {"name": "Springfield", "lat": 39.7817, "lon": -89.6501, "pop": 100000}
    ],
    "la_1955": [
        {"name": "Los Angeles (Record: 110°F)", "lat": 34.0522, "lon": -118.2437, "pop": 2200000}, 
        {"name": "Long Beach", "lat": 33.7701, "lon": -118.1937, "pop": 250000},
        {"name": "Santa Monica", "lat": 34.0195, "lon": -118.4912, "pop": 75000},
        {"name": "Anaheim", "lat": 33.8366, "lon": -117.9143, "pop": 30000} 
    ],
    "st_louis_nyc_1966": [
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 700000},
        {"name": "New York City", "lat": 40.7128, "lon": -74.0060, "pop": 7800000},
        {"name": "Philadelphia", "lat": 39.9526, "lon": -75.1652, "pop": 2000000},
        {"name": "Cincinnati", "lat": 39.1031, "lon": -84.5120, "pop": 500000},
        {"name": "Indianapolis", "lat": 39.7684, "lon": -86.1581, "pop": 500000}
    ],
    "uk_1976": [
        {"name": "London (Station: 21.5°C)", "lat": 51.5074, "lon": -0.1278, "pop": 6800000}, 
        {"name": "Birmingham", "lat": 52.4862, "lon": -1.8904, "pop": 1000000},
        {"name": "Southampton", "lat": 50.9097, "lon": -1.4044, "pop": 200000}
    ],
    "us_1980": [
        {"name": "Memphis (Station: 28.8°C)", "lat": 35.1495, "lon": -90.0490, "pop": 650000},
        {"name": "St. Louis", "lat": 38.6270, "lon": -90.1994, "pop": 450000},
        {"name": "Kansas City", "lat": 39.0997, "lon": -94.5786, "pop": 450000},
        {"name": "Dallas", "lat": 32.7767, "lon": -96.7970, "pop": 900000},
        {"name": "Jackson (MS)", "lat": 32.2988, "lon": -90.1848, "pop": 200000}
    ],
    "athens_1987": [
        {"name": "Athens (Station: 25.7°C)", "lat": 37.9838, "lon": 23.7275, "pop": 3000000},
        {"name": "Patras", "lat": 38.2466, "lon": 21.7346, "pop": 150000},
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
        {"name": "Berlin", "lat": 52.5200, "lon": 13.4050, "pop": 3600000},
        {"name": "Amsterdam", "lat": 52.3676, "lon": 4.9041, "pop": 820000}
    ],   
    "russia_2010": [
        {"name": "Moscow", "lat": 55.7558, "lon": 37.6173, "pop": 11500000},
        {"name": "St. Petersburg (Station: 23.4°C)", "lat": 59.9311, "lon": 30.3609, "pop": 5400000}, 
        {"name": "Nizhny Novgorod", "lat": 56.3269, "lon": 44.0059, "pop": 1250000},
        {"name": "Voronezh", "lat": 51.6755, "lon": 39.2089, "pop": 1000000},
        {"name": "Helsinki", "lat": 60.1699, "lon": 24.9384, "pop": 650000} 
    ],
    "india_pak_2015": [     
        {"name": "Karachi", "lat": 24.8607, "lon": 67.0011, "pop": 16000000},
        {"name": "Hyderabad (Pak)", "lat": 25.3960, "lon": 68.3578, "pop": 1700000},
        {"name": "New Delhi", "lat": 28.6139, "lon": 77.2090, "pop": 26000000},
        {"name": "Nagpur", "lat": 21.1458, "lon": 79.0882, "pop": 2400000},
        {"name": "Hyderabad (India)", "lat": 17.3850, "lon": 78.4867, "pop": 10000000},
        {"name": "Vijayawada", "lat": 16.5062, "lon": 80.6480, "pop": 1500000},
        {"name": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "pop": 8000000},
        {"name": "Bhubaneswar (Station: 29.2°C)", "lat": 20.2961, "lon": 85.8245, "pop": 1100000},
        {"name": "Dhaka (Station: 28.0°C)", "lat": 23.8103, "lon": 90.4125, "pop": 22000000}, 
        {"name": "Muscat", "lat": 23.5859, "lon": 58.4059, "pop": 1500000}   
    ],
    "iran_2015": [
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
    "pnw_heat_dome": [      
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
    "delhi_heat_wave": [        
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
    "persian_gulf_2024": [      
        {"name": "Dubai (Station: 31.4°C)", "lat": 25.276987, "lon": 55.296249, "pop": 3300000},
        {"name": "Doha", "lat": 25.2854, "lon": 51.5310, "pop": 2300000},
        {"name": "Bandar Abbas", "lat": 27.1832, "lon": 56.2666, "pop": 526000},
        {"name": "Abu Dhabi", "lat": 24.4539, "lon": 54.3773, "pop": 1450000}
    ],
    "australia_heat_dome": [
        {"name": "Jakarta (Station: 27.2°C)", "lat": -6.2088, "lon": 106.8456, "pop": 10500000}, 
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
#          HELPER FUNCTIONS (NEW PIPELINE)
# ==========================================

def generate_plotly_teaser(scenario_id, title, lats, lons, values, output_dir,
                          briefing="", description=""):
    """Generates the fast-loading 2D Plotly Teaser for Web Gallery use."""
    print("Building Plotly Teaser...")
    fig = go.Figure(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=8,
            color=values,
            colorscale='YlOrRd',
            cmin=20, 
            cmax=38,
            opacity=0.75,
            showscale=True,
            colorbar=dict(title="Wet Bulb °C")
        ),
        text=[f"Wet Bulb: {v:.1f}°C" for v in values],
        hoverinfo='text'
    ))
    
    center_lat = sum(lats)/len(lats) if lats else 0
    center_lon = sum(lons)/len(lons) if lons else 0
    
    # Build briefing annotation for bottom-left of map
    annotations = []
    if briefing:
        # Clean up briefing for display: first paragraph only, truncate
        brief_lines = briefing.split('\n\n')
        brief_text = brief_lines[0] if brief_lines else briefing
        if len(brief_text) > 200:
            brief_text = brief_text[:197] + "..."
        # Add hint about 3D Earth button
        brief_text += "<br><br><i>Click 3D Earth for full visualization in Google Earth</i>"
        
        annotations.append(dict(
            text=brief_text,
            showarrow=False,
            xref="paper", yref="paper",
            x=0.02, y=0.02,
            xanchor="left", yanchor="bottom",
            font=dict(size=11, color="#1a1a2e"),
            bgcolor="rgba(255,255,255,0.85)",
            bordercolor="rgba(0,0,0,0.15)",
            borderwidth=1,
            borderpad=8,
            align="left"
        ))
    
    fig.update_layout(
        title=title,
        mapbox=dict(
            style="white-bg",
            center=dict(lat=center_lat, lon=center_lon),
            zoom=3,
            layers=[dict(
                below='traces',
                sourcetype='raster',
                sourceattribution='ESRI',
                source=['https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}']
            )]
        ),
        margin=dict(l=0, r=0, t=40, b=0),
        annotations=annotations
    )
    
    # NEW: Build HTML manually to guarantee Gallery Studio compatibility
    fig_json = fig.to_json()
    fig_dict = json.loads(fig_json)
    data_str = json.dumps(fig_dict.get('data', []))
    layout_str = json.dumps(fig_dict.get('layout', {}))

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
</head>
<body style="background:#f5f5f0; margin:0;">
    <div id="plotly-graph" style="width:100vw; height:100vh;"></div>
    <script>
        var data = {data_str};
        var layout = {layout_str};
        Plotly.newPlot('plotly-graph', data, layout);
    </script>
</body>
</html>"""
    
    teaser_path = os.path.join(output_dir, f"{scenario_id}_teaser.html")
    with open(teaser_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"✅ Plotly Teaser saved: {teaser_path}")


def package_and_cleanup(scenario_id, files_to_package, output_dir):
    """Zips the raw KML and PNG files into a single-document KMZ.
    
    Merges all KML layers into one doc.kml with <Folder> wrappers.
    Google Earth only reads the first KML in a KMZ archive, so separate
    KML files would result in only one layer loading. This approach
    puts everything in a single document with toggleable folders.
    
    Keeps original KML/PNG files on disk for the desktop Python orrery.
    """
    kmz_filename = f"{scenario_id}_blockbuster.kmz"
    kmz_path = os.path.join(output_dir, kmz_filename)
    print(f"Packaging {kmz_filename}...")
    
    # Separate KML files from asset files (PNG etc.)
    kml_files = [f for f in files_to_package if f.endswith('.kml') and os.path.exists(f)]
    asset_files = [f for f in files_to_package if not f.endswith('.kml') and os.path.exists(f)]
    
    # Merge all KML document bodies into folders within a single doc.kml
    folders = ""
    for kml_path in kml_files:
        basename = os.path.basename(kml_path)
        # Derive a readable layer name from the filename
        # e.g. "1948-08-26_spikes_nyc_1948.kml" -> "Spikes"
        parts = basename.replace('.kml', '').split('_')
        layer_name = basename
        for part in parts:
            if part.lower() in ('spikes', 'heatmap', 'impact'):
                layer_name = part.capitalize()
                break
        
        # Read the KML and extract the <Document> body
        with open(kml_path, 'r', encoding='utf-8') as f:
            kml_text = f.read()
        
        # Extract content between <Document ...> and </Document>
        m = re.search(r'<Document[^>]*>(.*)</Document>', kml_text, re.DOTALL)
        body = m.group(1).strip() if m else ''
        
        if body:
            folders += f"""
        <Folder>
            <name>{layer_name}</name>
            {body}
        </Folder>"""
    
    doc_kml = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
    <Document>
        <name>{scenario_id}</name>{folders}
    </Document>
</kml>
"""
    
    with zipfile.ZipFile(kmz_path, 'w', zipfile.ZIP_DEFLATED) as kmz:
        # Single merged doc.kml as the only KML entry
        kmz.writestr('doc.kml', doc_kml)
        # Add asset files (PNGs referenced by the KML layers)
        for f in asset_files:
            kmz.write(f, arcname=os.path.basename(f))
                
    # NOTE: Raw KML/PNG files are NOT deleted.
    # They remain in data/ for the desktop Python orrery.
    # The KMZ (for web gallery) and raw files (for desktop) coexist.
            
    print(f"Packaged: {kmz_filename} ({len(kml_files)} layers merged)")
    return kmz_path


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
        self.listbox.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

        for name in SCENARIOS.keys():
            self.listbox.insert(tk.END, name)

        btn = ttk.Button(self.root, text="Generate Assets (Teaser + KMZ)", command=self.run_pipeline)
        btn.pack(pady=20)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_lbl = tk.Label(self.root, textvariable=self.status_var, font=("Helvetica", 9), fg="gray")
        status_lbl.pack(pady=5)

    def create_legend_card(self):
        """Creates the biological limit scale image."""
        fig, ax = plt.subplots(figsize=(3, 4), dpi=100)
        ax.axis('off')
        y_pos = 0.9
        ax.text(0.5, y_pos, "BIOLOGICAL\nLIMIT SCALE", ha='center', va='center', fontsize=12, fontweight='bold', color='black')
        y_pos -= 0.15
        
        ax.text(0.5, y_pos, "(Wet Bulb Temperature)", ha='center', va='center', fontsize=9, style='italic', color='#444444')
        y_pos -= 0.15

        zones = [
            ("35°C+", "Theoretical Limit (Raymond)", "black"),
            ("31°C+", "Biological Breach (Vecellio)", "#8B0000"),
            ("26°C+", "High Risk (Carter/Foster)", "red"),
            ("20°C+", "Moderate Risk (ISO)", "orange")
        ]
        
        for label, desc, color in zones:
            rect = mpatches.Rectangle((0.1, y_pos-0.05), 0.15, 0.1, facecolor=color, edgecolor='black')
            ax.add_patch(rect)
            ax.text(0.3, y_pos, label, ha='left', va='center', fontsize=10, fontweight='bold')
            ax.text(0.3, y_pos-0.05, desc, ha='left', va='top', fontsize=8, color='#555555')
            y_pos -= 0.15

        legend_path = os.path.join(DATA_DIR, 'legend_risk_index_cited.png')
        plt.savefig(legend_path, bbox_inches='tight', transparent=True)
        plt.close()
        return legend_path

    def create_intel_card(self, title, description, briefing, date, mission_id):
        """Creates the dynamic briefing text card."""
        fig, ax = plt.subplots(figsize=(4.5, 5), dpi=120)
        ax.axis('off')
        
        rect = mpatches.Rectangle((0, 0), 1, 1, facecolor='#111111', edgecolor='#333333', linewidth=2, alpha=0.9, transform=ax.transAxes)
        ax.add_patch(rect)

        y_pos = 0.92
        ax.text(0.05, y_pos, "SCENARIO INTEL", ha='left', va='top', fontsize=10, fontweight='bold', color='#FFCC00', fontfamily='monospace')
        y_pos -= 0.08
        ax.text(0.05, y_pos, title.upper(), ha='left', va='top', fontsize=14, fontweight='bold', color='white', fontfamily='sans-serif')
        y_pos -= 0.08
        ax.text(0.05, y_pos, f"DATE: {date}", ha='left', va='top', fontsize=9, color='#AAAAAA', fontfamily='monospace')
        y_pos -= 0.08
        
        wrapped_desc = textwrap.fill(description, width=45)
        ax.text(0.05, y_pos, wrapped_desc, ha='left', va='top', fontsize=10, style='italic', color='#DDDDDD')
        
        y_pos -= (len(wrapped_desc.split('\n')) * 0.05) + 0.05
        ax.plot([0.05, 0.95], [y_pos, y_pos], color='#444444', linewidth=1, transform=ax.transAxes)
        y_pos -= 0.05
        
        wrapped_briefing = textwrap.fill(briefing, width=50)
        ax.text(0.05, y_pos, wrapped_briefing, ha='left', va='top', fontsize=9, color='white', fontfamily='serif', linespacing=1.4)
        
        intel_path = os.path.join(DATA_DIR, f'{date}_intel_{mission_id}.png')
        plt.savefig(intel_path, bbox_inches='tight', transparent=True)
        plt.close()
        return intel_path

    def create_pop_legend_card(self):
        """Creates the population circle key."""
        fig, ax = plt.subplots(figsize=(3, 2), dpi=100)
        ax.axis('off')
        
        ax.text(0.5, 0.8, "POPULATION HUB", ha='center', va='center', fontsize=10, fontweight='bold', color='black')
        
        circle = mpatches.Circle((0.5, 0.4), 0.15, facecolor='none', edgecolor='#00A5FF', linewidth=2)
        ax.add_patch(circle)
        
        ax.text(0.5, 0.1, "Radius scales with\nMillions of People", ha='center', va='center', fontsize=8, color='#555')
        
        legend_path = os.path.join(DATA_DIR, 'legend_impact_pop.png')
        plt.savefig(legend_path, bbox_inches='tight', transparent=True)
        plt.close()
        return legend_path

    def fetch_era5_data_openmeteo(self, lat_range, lon_range, date):
        """Fetches historic wet-bulb data."""
        cache_file = os.path.join(DATA_DIR, 'weather_cache.json')
        cache = {}
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                try:
                    cache = json.load(f)
                except:
                    pass
        
        lats, lons, values = [], [], []
        total_points = len(lat_range) * len(lon_range)
        processed = 0
        
        for lat in lat_range:
            for lon in lon_range:
                processed += 1
                if processed % 10 == 0:
                    self.status_var.set(f"Fetching ERA5 Grid: {processed}/{total_points}")
                    self.root.update()
                    
                cache_key = f"{lat}_{lon}_{date}"
                if cache_key in cache:
                    lats.append(lat)
                    lons.append(lon)
                    values.append(cache[cache_key])
                    continue
                
                url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={date}&end_date={date}&hourly=temperature_2m,relative_humidity_2m"
                try:
                    response = requests.get(url)
                    data = response.json()
                    if 'hourly' in data:
                        temps = data['hourly']['temperature_2m']
                        humids = data['hourly']['relative_humidity_2m']
                        
                        max_wb = -999
                        for t, h in zip(temps, humids):
                            if t is not None and h is not None:
                                wb = t * math.atan(0.151977 * math.sqrt(h + 8.313659)) + \
                                     math.atan(t + h) - math.atan(h - 1.676331) + \
                                     0.00391838 * math.pow(h, 1.5) * math.atan(0.023101 * h) - 4.686035
                                if wb > max_wb: max_wb = wb
                                
                        lats.append(lat)
                        lons.append(lon)
                        values.append(max_wb)
                        cache[cache_key] = max_wb
                        time.sleep(0.1) 
                except Exception as e:
                    print(f"Error fetching {lat},{lon}: {e}")
                    
        with open(cache_file, 'w') as f:
            json.dump(cache, f)
            
        return lats, lons, values

    def run_pipeline(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a scenario.")
            return
            
        mission_name = self.listbox.get(selection[0])
        config = SCENARIOS[mission_name]
        
        mission_id = config['id']
        date = config['date']
        focus_val_min = config['focus_val_min']
        
        self.status_var.set("Generating Intel Cards...")
        self.root.update()
        
        legend_risk_path = self.create_legend_card()
        legend_pop_path = self.create_pop_legend_card()
        intel_path = self.create_intel_card(mission_name, config['description'], config['briefing'], date, mission_id)

        self.status_var.set("Fetching ERA5 Weather Data...")
        self.root.update()
        
        lats, lons, values = self.fetch_era5_data_openmeteo(config['lat_range'], config['lon_range'], date)

        if not values:
            messagebox.showerror("Error", "No weather data retrieved.")
            self.status_var.set("Ready")
            return

        self.status_var.set("Building 3D Topology...")
        self.root.update()
        
        # ---------------------------
        # BUILD SPIKES
        # ---------------------------
        kml_spikes = simplekml.Kml()
        kml_spikes.document.name = f"{mission_id} Spikes ({date})"

        screen = kml_spikes.newscreenoverlay(name="Intel Card")
        screen.icon.href = os.path.basename(intel_path)
        screen.overlayxy = simplekml.OverlayXY(x=0, y=1, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
        screen.screenxy = simplekml.ScreenXY(x=0.02, y=0.98, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
        screen.size = simplekml.Size(x=0.25, y=0, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)

        screen_leg = kml_spikes.newscreenoverlay(name="Risk Scale")
        screen_leg.icon.href = os.path.basename(legend_risk_path)
        screen_leg.overlayxy = simplekml.OverlayXY(x=1, y=0, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
        screen_leg.screenxy = simplekml.ScreenXY(x=0.98, y=0.05, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
        screen_leg.size = simplekml.Size(x=0.15, y=0, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)

        for lat, lon, val in zip(lats, lons, values):
            if val >= focus_val_min:
                height = (val - focus_val_min) * 50000 
                pnt = kml_spikes.newpoint(name=f"{val:.1f}")
                pnt.coords = [(lon, lat, height)]
                pnt.extrude = 1
                pnt.altitudemode = simplekml.AltitudeMode.relativetoground
                
                if val >= 35.0: # Theoretical Limit
                    color = 'ff000000' 
                elif val >= 31.0: # Biological Breach
                    color = 'ff00008b' 
                elif val >= 26.0: # High Risk
                    color = 'ff0000ff' 
                else:             # Moderate Risk
                    color = 'ff00a5ff' 
                    
                pnt.style.polystyle.color = color
                pnt.style.polystyle.fill = 1
                pnt.style.linestyle.width = 0

        spikes_filename = os.path.join(DATA_DIR, f"{date}_spikes_{mission_id}.kml")
        kml_spikes.save(spikes_filename)

        # ---------------------------
        # BUILD HEATMAP
        # ---------------------------
        grid_x, grid_y = np.mgrid[min(lons):max(lons):100j, min(lats):max(lats):100j]
        grid_z = griddata((lons, lats), values, (grid_x, grid_y), method='linear')

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

        # ---------------------------
        # BUILD IMPACT POPULATION
        # ---------------------------
        kml_pop = simplekml.Kml()
        kml_pop.document.name = f"{mission_id} Impact Zones"
        
        screen_pop = kml_pop.newscreenoverlay(name="Pop Legend")
        screen_pop.icon.href = os.path.basename(legend_pop_path)
        screen_pop.overlayxy = simplekml.OverlayXY(x=0, y=0, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
        screen_pop.screenxy = simplekml.ScreenXY(x=0.02, y=0.05, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)
        screen_pop.size = simplekml.Size(x=0.15, y=0, xunits=simplekml.Units.fraction, yunits=simplekml.Units.fraction)

        impact_filename = os.path.join(DATA_DIR, f"{date}_impact_{mission_id}.kml")
        
        if mission_id in POPULATION_HUBS:
            for city in POPULATION_HUBS[mission_id]:
                radius_km = city['pop'] / 250000.0  
                R = 6371.0 
                lat_rad = math.radians(city['lat'])
                lon_rad = math.radians(city['lon'])
                
                points = []
                for i in range(32):
                    theta = math.radians(float(i) / 32 * 360.0)
                    dist_rad = radius_km / R
                    pt_lat = math.asin(math.sin(lat_rad) * math.cos(dist_rad) + math.cos(lat_rad) * math.sin(dist_rad) * math.cos(theta))
                    pt_lon = lon_rad + math.atan2(math.sin(theta) * math.sin(dist_rad) * math.cos(lat_rad), math.cos(dist_rad) - math.sin(lat_rad) * math.sin(pt_lat))
                    points.append((math.degrees(pt_lon), math.degrees(pt_lat)))
                points.append(points[0])
                
                pol = kml_pop.newpolygon(name=city['name'])
                pol.outerboundaryis = points
                pol.style.polystyle.color = '6600a5ff'
                pol.style.polystyle.fill = 1
                pol.style.linestyle.color = 'ff00a5ff'
                pol.style.linestyle.width = 2
                
            kml_pop.save(impact_filename)

        # ==========================================
        #     NEW PIPELINE BRIDGE (TEASER & KMZ)
        # ==========================================
        
        # 1. Generate the Web Gallery Plotly Teaser
        generate_plotly_teaser(mission_id, f"{mission_name} ({date})", lats, lons, values, DATA_DIR,
                              briefing=config.get('briefing', ''),
                              description=config.get('description', ''))

        # 2. Collect the exact 7 files we just created in this specific run
        generated_files = [
            spikes_filename,
            heat_filename,
            impact_filename if mission_id in POPULATION_HUBS else "",
            img_path,
            legend_risk_path,
            legend_pop_path,
            intel_path
        ]
        
        # 3. Zip them into a KMZ and immediately delete those loose files
        package_and_cleanup(mission_id, generated_files, DATA_DIR)

        self.status_var.set("Ready")
        messagebox.showinfo("Success", f"Generated Teaser and KMZ Blockbuster for:\n{mission_name}")


if __name__ == "__main__":
    app = MissionSelector()
    app.root.mainloop()