# HANDOFF -- European Heat Dome June 2026 (L-065)

Tony Quintanilla, PE | Claude Opus 4.8 | 2026-06-25

Base SHA: 7734856060a5ec153152c7472b122deef52e1d7e (branch main)
  Round trip confirmed at session start and at clone (HEAD == base).
Design: wet-bulb spine (fetch_era5_heatwave + HEATWAVE_THRESHOLDS) + absolute
  air-temp pins (engine pin_stations path), C only. Current dome, date 2026-06-21.
Departs from the Western convention (anomaly + F pins); recenters on health.

--------------------------------------------------------------------------------
CHANGE 1 -- scenarios_heatwaves.py
Append this block inside SCENARIOS, immediately before the closing ']' (was line 639).
--------------------------------------------------------------------------------

    # Europe Heat Dome June 2026 (L-065). Added June 2026 with Anthropic's Claude Opus 4.8.
    {
        'scenario_id': 'europe_2026', 'name': 'Europe Heat Dome (June 2026)',
        'boundary_type': 'heatwave',
        'date': '2026-06-21',
        'lat_range': range(53, 36, -2), 'lon_range': range(-10, 16, 2),
        'focus_val_min': 20.0,
        'description': 'Saharan dry-heat dome; June air-temp records, low wet-bulb, no-AC mortality.',
        # Source (briefing attribution numerics): Climate Central Climate Shift Index
        #   (csi.climatecentral.org), 2026-06-22 [confirm live value at fetch].
        # Source: Copernicus C3S / WMO, Europe State of the Climate (Europe ~2x global warming rate).
        'briefing': (
            "THE DRY DOME. A blocking high pulled Saharan air over Western Europe. "
            "For Europe the danger is less about wet-bulb extremes than about duration, "
            "record overnight minima, and low AC adoption -- the 2003 pattern repeating. "
            "Air-temp records fell from Iberia to the UK.\n\n"
            "Station Records (Air Temp): UK 35.8C (Wiggonholt, June record); "
            "Spain 43.7C (Tama, Cantabria); Portugal 42.7C (Pinhao).\n"
            "Regional Map Peak: [TO-FETCH]C (Wet Bulb).\n\n"
            "SOURCE: Met Office; AEMET; IPMA. ATTRIBUTION: Climate Central Climate "
            "Shift Index rates this heat at least 5x more likely due to human-caused "
            "climate change; EU Copernicus C3S / WMO note Europe is warming about "
            "twice the global average."
        ),
        'populations': [
            {"name": "Madrid", "lat": 40.4168, "lon": -3.7038, "pop": 3300000},
            {"name": "Lisbon", "lat": 38.7223, "lon": -9.1393, "pop": 550000},
            {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "pop": 2100000},
            {"name": "London", "lat": 51.5074, "lon": -0.1278, "pop": 8900000},
            {"name": "Seville", "lat": 37.3891, "lon": -5.9845, "pop": 690000},
        ],
        'pin_stations': [
            {"name": "Wiggonholt UK", "lat": 50.95, "lon": -0.50, "air_temp_c": 35.8,
             "note": "UK June record, provisional"},   # Source: Met Office via CNN, 2026-06-24
            {"name": "Tama Cantabria", "lat": 43.16, "lon": -4.61, "air_temp_c": 43.7,
             "note": "Cantabria all-time record"},      # Source: AEMET via CNN, 2026-06-23
            {"name": "Pinhao PT", "lat": 41.19, "lon": -7.55, "air_temp_c": 42.7,
             "note": "Iberia peak 21 Jun"},             # Source: AEMET/IPMA via Mappr, 2026-06-21
        ],
        'thresholds': HEATWAVE_THRESHOLDS,
        'fetch': fetch_era5_heatwave,
        'lats': [], 'lons': [], 'values': [],
    },

--------------------------------------------------------------------------------
CHANGE 2 -- earth_system_generator.py  (~line 169, station-pin label)
Non-breaking / key-aware: the pin-label line is SHARED with
scenarios_western_heatwave_march_2026.py, which feeds 'air_temp_f'. A hard swap
to air_temp_c would KeyError Western's pins. Branch on the key instead.

  was:
            label = f"{station['air_temp_f']:.0f}F"

  now:
            if 'air_temp_c' in station:
                label = f"{station['air_temp_c']:.1f}C"
            else:
                label = f"{station['air_temp_f']:.0f}F"

--------------------------------------------------------------------------------
VERIFICATION (container gate -- DONE)
--------------------------------------------------------------------------------
  py_compile     : OK (both modules)
  schema parity  : europe_2026 == europe_2003 keys + pin_stations
  wet-bulb wiring : fetch_era5_heatwave + HEATWAVE_THRESHOLDS confirmed
  pins            : 3, C-only (air_temp_c; no air_temp_f)
  label branch    : new -> '43.7C'; Western -> '96F' (preserved)
  ASCII / LF      : clean
  NOT run here    : Open-Meteo fetch (offline), provenance_scanner
                    (needs exceptions file), Mode-5 render

--------------------------------------------------------------------------------
TONY-SIDE STEPS (in order)
--------------------------------------------------------------------------------
  1. Run the europe_2026 fetch (fetch_era5_heatwave) for 2026-06-21; it
     populates lats/lons/values from Open-Meteo's ERA5 archive.
  2. Read the regional wet-bulb peak off the fetched grid; replace
     'Regional Map Peak: [TO-FETCH]C' in the briefing with the real value.
     Let the data speak -- do not pre-write the number.
  3. Confirm the live Climate Central CSI multiplier (the '5x') at
     csi.climatecentral.org; update the briefing if it has moved.
  4. Confirm the 3 station records against the primary met service
     (Met Office / AEMET / IPMA). Values are provisional as transcribed.
  5. provenance_scanner.py with data/provenance_exceptions.json -> Tier-1 = 0.
  6. Generate the Plotly teaser + KMZ and eyeball both (Mode-5). This is the
     authoritative close gate. Green container tests are not a render.

--------------------------------------------------------------------------------
LEDGER UPDATE -- L-065 (apply in LEDGER_CONSOLIDATED.md)
--------------------------------------------------------------------------------
Section A row -> bump date:
  | ! | L-065 | European heat wave heat map (Earth System track) | OPEN | 4.8 | 2026-06-25 |

Section H, append to the [L-065] block:
  - BUILD 2026-06-25 (on 7734856): europe_2026 appended to scenarios_heatwaves.py
    (wet-bulb spine + C-only air-temp pins); earth_system_generator.py pin label
    made key-aware (C for europe_2026, F preserved for Western). Container gate
    green. OPEN pending: fetch + wet-bulb-peak fill + live CSI confirm + station
    confirm + provenance Tier-1=0 + Mode-5 render. Move to DONE after render.
  - Stage 1 (Sentinel-3 LST snapshot) NOT built -- separate artifact; wet-bulb
    needs humidity which LST does not carry. Spec on request.

WATCH: World Weather Attribution rapid study on the June 2026 event. If it
  publishes, it is the strongest citable attribution -- replace the CSI/C3S line.
