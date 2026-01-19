"""
Paleoclimate Visualization for Paloma's Orrery
Phanerozoic temperature reconstruction (540 Ma - present)

Shows the "big picture" of Earth's climate history with Plotly's zoom capability
to explore details from the Phanerozoic "double hump" down to ice ages and 
the remarkable stability of the Holocene.

Data Preservation is Climate Action
"""

import json
import os
import numpy as np
from save_utils import save_plot

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Data files
# PALEO_DATA_DIR = 'paleoclimate_data'
PALEO_DATA_DIR = 'data'
LR04_CACHE = os.path.join(PALEO_DATA_DIR, 'lr04_benthic_stack.json')
# SCOTESE_PHANEROZOIC = '8c__Phanerozoic_Pole_to_Equator_Temperatures.csv'
SCOTESE_PHANEROZOIC = os.path.join(PALEO_DATA_DIR, '8c__Phanerozoic_Pole_to_Equator_Temperatures.csv')

# Geologic time periods - expanded to full Earth history
GEOLOGIC_PERIODS = [
    # Precambrian (4.5 Ga - 541 Ma)
    {'name': 'Hadean', 'start': 4500, 'end': 4000, 'color': '#8B4789'},
    {'name': 'Archean', 'start': 4000, 'end': 2500, 'color': '#F0619D'},
    {'name': 'Proterozoic', 'start': 2500, 'end': 541, 'color': '#FE9D6F'},
    
    # Paleozoic (541 - 252 Ma)
    {'name': 'Cambrian', 'start': 541, 'end': 485.4, 'color': '#7FA056'},
    {'name': 'Ordovician', 'start': 485.4, 'end': 443.8, 'color': '#009270'},
    {'name': 'Silurian', 'start': 443.8, 'end': 419.2, 'color': '#B3E1B6'},
    {'name': 'Devonian', 'start': 419.2, 'end': 358.9, 'color': '#CB8C37'},
    {'name': 'Carboniferous', 'start': 358.9, 'end': 298.9, 'color': '#67A599'},
    {'name': 'Permian', 'start': 298.9, 'end': 252.2, 'color': '#F04028'},
    
    # Mesozoic (252 - 66 Ma)
    {'name': 'Triassic', 'start': 252.2, 'end': 201.3, 'color': '#812B92'},
    {'name': 'Jurassic', 'start': 201.3, 'end': 145.0, 'color': '#34B2C9'},
    {'name': 'Cretaceous', 'start': 145.0, 'end': 66.0, 'color': '#7FC64E'},
    
    # Cenozoic (66 Ma - present)
    {'name': 'Paleocene', 'start': 66.0, 'end': 56.0, 'color': '#FD9A52'},
    {'name': 'Eocene', 'start': 56.0, 'end': 33.9, 'color': '#FDB462'},
    {'name': 'Oligocene', 'start': 33.9, 'end': 23.03, 'color': '#FED7AA'},
    {'name': 'Miocene', 'start': 23.03, 'end': 5.333, 'color': '#FFFF99'},
    {'name': 'Pliocene', 'start': 5.333, 'end': 2.58, 'color': '#FFFFCC'},
    {'name': 'Pleistocene', 'start': 2.58, 'end': 0.0117, 'color': '#C6F7FF'},
    {'name': 'Holocene', 'start': 0.0117, 'end': 0.000001, 'color': '#59DEDE'}
]

# Hominin and hominoid species - earliest fossil evidence dates
# Sources: Smithsonian Human Origins, Nature, Science, peer-reviewed literature
# 
# UPDATED December 2025 to reflect:
#   - Yunxian 2 reanalysis (Feng et al., Science, Sept 2025)
#   - Five-Branch Model of Middle Pleistocene human evolution
#   - Cambridge two-population origin of H. sapiens (Cousins et al., Nature Genetics, March 2025)
#
# evidence='fossil' : Physical remains recovered, dated directly or via stratigraphy
# evidence='dna_only': "Ghost populations" identified through genetic signatures in 
#                      modern humans; no fossil remains recovered
#
# The Pleistocene wasn't a single-file march of species but a braided stream 
# of populations mixing, separating, and remixing across Africa and Eurasia.
#
# FIVE-BRANCH MODEL (post-Yunxian 2):
#   1. Asian H. erectus (ancient survivors)
#   2. H. heidelbergensis (now considered a specialized branch, not direct ancestor)
#   3. H. neanderthalensis (European branch, diverged ~1.38 Ma)
#   4. H. longi / Denisovans (East Asian branch, diverged ~1.32 Ma)
#   5. H. sapiens (African branch)

HOMININ_SPECIES = [
    # =====================================================================
    # FOSSIL-CONFIRMED SPECIES (filled triangle markers)
    # y_offset: manual vertical offset from base position (-10.0)
    #           positive = up, negative = down
    #           Use minimal offsets to keep markers clustered near -10 line
    # =====================================================================
    
    # Early Hominoids (apes) - Miocene
    {'name': 'Proconsul', 'age_ma': 21, 'category': 'hominoid', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': 'Early Miocene ape from Kenya/Uganda.<br>Earliest well-documented hominoid.<br>Arboreal quadruped, ~20-22 Ma.<br><i>Source: Smithsonian Human Origins</i>'},
    {'name': 'Morotopithecus', 'age_ma': 20.6, 'category': 'hominoid', 'evidence': 'fossil',
     'y_offset': 0.7,  # Stagger up from Proconsul
     'note': 'Early Miocene ape from Uganda.<br>Shows early signs of upright posture.<br>>20.6 Ma.<br><i>Source: Smithsonian Human Origins</i>'},
    
    # Earliest possible hominins - Late Miocene
    {'name': 'Sahelanthropus tchadensis', 'age_ma': 7.0, 'category': 'early_hominin', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': 'Oldest possible hominin ("Toumai").<br>Chad, 7.2-6.8 Ma.<br>Debated bipedality.<br><i>Source: Brunet et al. 2002, Nature</i>'},
    {'name': 'Orrorin tugenensis', 'age_ma': 6.0, 'category': 'early_hominin', 'evidence': 'fossil',
     'y_offset': 0.7,  # Slight stagger
     'note': '"Millennium Man" from Kenya.<br>Femur suggests bipedality.<br>6.1-5.8 Ma.<br><i>Source: Senut et al. 2001</i>'},
    {'name': 'Ardipithecus kadabba', 'age_ma': 5.7, 'category': 'early_hominin', 'evidence': 'fossil',
     'y_offset': 1.4,  # Stagger down
     'note': 'Early hominin from Ethiopia.<br>Toe bone suggests bipedality.<br>5.8-5.2 Ma.<br><i>Source: Haile-Selassie 2001</i>'},
    {'name': 'Ardipithecus ramidus', 'age_ma': 4.4, 'category': 'early_hominin', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': '"Ardi" from Ethiopia.<br>Facultative biped, woodland habitat.<br>4.5-4.4 Ma.<br><i>Source: White et al. 2009, Science</i>'},
    
    # Australopithecines - Pliocene
    {'name': 'Australopithecus anamensis', 'age_ma': 4.2, 'category': 'australopith', 'evidence': 'fossil',
     'y_offset': 0.7,  # Stagger from ramidus
     'note': 'Earliest Australopithecus.<br>Kenya, near Lake Turkana.<br>4.2-3.9 Ma.<br><i>Source: Leakey et al. 1995</i>'},
    {'name': 'Australopithecus afarensis', 'age_ma': 3.85, 'category': 'australopith', 'evidence': 'fossil',
     'y_offset': 1.4,  # Stagger down
     'note': 'Includes "Lucy" (3.2 Ma).<br>Ethiopia, Kenya, Tanzania. Bipedal.<br>3.85-2.95 Ma.<br><i>Source: Johanson & White 1979</i>'},
    {'name': 'Australopithecus africanus', 'age_ma': 3.0, 'category': 'australopith', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': '"Taung Child" species. South Africa.<br>First australopith discovered (1924).<br>3.3-2.1 Ma.<br><i>Source: Dart 1925</i>'},
    
    # Homo genus - Pleistocene (fossil-confirmed)
    {'name': 'Homo (earliest)', 'age_ma': 2.8, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.7,  # Stagger from africanus
     'note': 'LD 350-1 jawbone, Ethiopia.<br>Earliest Homo specimen.<br>Genus emerges ~2.8 Ma.<br><i>Source: Villmoare et al. 2015, Science</i>'},
    {'name': 'Homo habilis', 'age_ma': 2.3, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': '"Handy man." First stone tool maker.<br>East/South Africa.<br>2.4-1.65 Ma.<br><i>Source: Leakey et al. 1964</i>'},
    {'name': 'Homo erectus', 'age_ma': 1.9, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': 'First to leave Africa, control fire.<br>Worldwide spread. 1.9 Ma - 110 ka.<br>One of five major Homo branches (2025 model).<br>Asian populations persisted alongside later species.<br><i>Source: Smithsonian Human Origins</i>'},
    {'name': 'Homo heidelbergensis', 'age_ma': 0.7, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': '[WARN] STATUS REVISED (2025): May be specialized<br>side-branch, not direct ancestor of sapiens.<br>Europe/Africa. 700-200 ka.<br>New divergence dates push common ancestors<br>back to >1 Ma, before heidelbergensis existed.<br><i>Source: Feng et al. 2025, Science; Stringer</i>'},
    {'name': 'Homo neanderthalensis', 'age_ma': 0.43, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,
     'note': 'European branch of Homo.<br>Earliest traits: Sima de los Huesos, Spain.<br>Classic Neanderthals 130-40 ka.<br>NEW: Diverged ~1.38 Ma (Yunxian 2 analysis).<br>Interbred with sapiens (~2% non-African DNA).<br><i>Source: Feng et al. 2025, Science</i>'},
    {'name': 'Homo longi', 'age_ma': 1.0, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,  # Slight stagger
     'note': '[SKULL] "Dragon Man" clade (named 2021).<br>Yunxian 2 skull (1 Ma) is earliest member.<br>Diverged from sapiens lineage ~1.32 Ma.<br>Includes Denisovans as late members.<br>Sister group to H. sapiens, not Neanderthals.<br><i>Source: Feng et al. 2025, Science</i>'},
    {'name': 'Homo sapiens', 'age_ma': 0.315, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,  # Stagger from neanderthalensis
     'note': 'Anatomically modern humans.<br>Jebel Irhoud, Morocco. ~315 ka.<br>NEW: Result of merger between two populations<br>that split ~1.5 Ma and reunited ~300 ka (80:20 ratio).<br><i>Source: Cousins et al. 2025, Nature Genetics</i>'},
    {'name': 'Denisovans', 'age_ma': 0.3, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.7,  # Stagger down from sapiens
     'note': 'Now placed within H. longi clade (2025).<br>Sediment DNA ~300 ka; fossils ~200 ka.<br>Denisova Cave, Siberia + Tibet, Laos.<br>Interbred with sapiens (up to 6% Oceanian DNA).<br><i>Source: Feng et al. 2025, Science</i>'},
    
    # Island Southeast Asia - remarkable parallel evolution
    {'name': 'Homo floresiensis', 'age_ma': 0.19, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,  # Stagger from sapiens/Denisovans cluster
     'note': '[ISLAND] "The Hobbit" of Flores, Indonesia.<br>~1m tall - island dwarfism or ancient lineage?<br>Survived until ~50 ka - COEXISTED with sapiens!<br>Sophisticated tools despite small brain.<br>190-50 ka (Liang Bua cave).<br><i>Source: Brown et al. 2004, Nature</i>'},
    {'name': 'Homo luzonensis', 'age_ma': 0.067, 'category': 'homo', 'evidence': 'fossil',
     'y_offset': 0.0,  # Isolated in time, no stagger needed
     'note': '[ISLAND] Philippines hominin (discovered 2019).<br>Callao Cave, Luzon. Small-bodied like floresiensis.<br>Mix of primitive and modern features.<br>Parallel island evolution - "Island Rule."<br>~67 ka - also coexisted with sapiens.<br><i>Source: Detroit et al. 2019, Nature</i>'},
    
    # =====================================================================
    # GHOST POPULATIONS (open triangle markers)
    # Identified through DNA signatures in modern humans; no fossils recovered
    # =====================================================================
    
    {'name': '"Superarchaic" Ghost', 'age_ma': 2.0, 'category': 'ghost', 'evidence': 'dna_only',
     'y_offset': 0.7,  # Stagger from erectus
     'note': '[GHOST] GHOST POPULATION (no fossils recovered)<br>Detected via DNA signatures in Denisovans.<br>Split from human lineage 2.2-1.8 Ma.<br>Possibly late H. erectus populations in Asia.<br>Contributed DNA to Neanderthal-Denisovan ancestor.<br><i>Source: Rogers et al. 2020, Science Advances</i>'},
    {'name': 'West African Ghost', 'age_ma': 0.7, 'category': 'ghost', 'evidence': 'dna_only',
     'y_offset': 0.7,  # Stagger from heidelbergensis
     'note': '[GHOST] GHOST POPULATION (no fossils recovered)<br>Detected in Yoruba, Mende, other West Africans.<br>2-19% of ancestry from unknown archaic hominin.<br>Split 360 ka - 1.02 Ma; introgressed 0-124 ka.<br>Genes enriched for tumor suppression, hormones.<br><i>Source: Durvasula & Sankararaman 2020,<br>Science Advances</i>'},
    {'name': 'Population A (80%)', 'age_ma': 1.5, 'category': 'ghost', 'evidence': 'dna_only',
     'y_offset': 0.0,
     'note': '[GHOST] GHOST POPULATION (no fossils recovered)<br>[SKULL] Major ancestor of H. sapiens (80% of genome).<br>Split from Population B ~1.5 Ma in Africa.<br>Severe bottleneck after split, then slow growth.<br>Also ancestral to Neanderthals and Denisovans.<br>Merged with Pop. B ~300 ka to form sapiens.<br><i>Source: Cousins et al. 2025, Nature Genetics</i>'},
    {'name': 'Population B (20%)', 'age_ma': 1.5, 'category': 'ghost', 'evidence': 'dna_only',
     'y_offset': 0.7,  # Stagger from Pop A (same age!)
     'note': '[GHOST] GHOST POPULATION (no fossils recovered)<br>[SKULL] Minor ancestor of H. sapiens (20% of genome).<br>Split from Population A ~1.5 Ma in Africa.<br>Genes concentrated in brain function and<br>neural processing-may have been crucial<br>for cognitive evolution.<br>Merged with Pop. A ~300 ka to form sapiens.<br><i>Source: Cousins et al. 2025, Nature Genetics</i>'},
    
    # Southeast Asian ghost populations
    {'name': '"Deep Denisovan" (D2)', 'age_ma': 0.28, 'category': 'ghost', 'evidence': 'dna_only',
     'y_offset': 1.4,  # Stagger from Denisovans/sapiens cluster
     'note': '[GHOST] GHOST POPULATION (no fossils recovered)<br>[DNA] Deeply divergent Denisovan lineage.<br>Split from Altai Denisovans ~280 ka.<br>Detected in Papuans, Filipinos (up to 4%).<br>Suggests multiple Denisovan populations across<br>SE Asia, not just Siberian group.<br><i>Source: Jacobs et al. 2019, Cell</i>'},
    {'name': 'SE Asian Archaic Ghost', 'age_ma': 0.15, 'category': 'ghost', 'evidence': 'dna_only',
     'y_offset': 0.0,  # Stagger from floresiensis
     'note': '[GHOST] GHOST POPULATION (no fossils recovered)<br>[DNA] Unknown archaic detected in SE Asians.<br>More divergent than Denisovans - possibly<br>from H. erectus descendants or floresiensis-<br>related populations. Controversial but intriguing.<br>May explain unique adaptations in region.<br><i>Source: Teixeira et al. 2021; Mondal et al. 2019</i>'},
]

# =========================================================================
# MARINE ISOTOPE STAGES (MIS)
# The "heartbeat" of Pleistocene climate - glacial/interglacial cycles
# that opened and closed migration corridors (Sahara, Levantine)
#
# Even numbers = cold/glacial (refugia, bottlenecks)
# Odd numbers = warm/interglacial (corridors open, expansions)
#
# These pulses directly drove the splits, mergers, and migrations
# visible in the hominin markers above.
# =========================================================================

MIS_STAGES = [
    # Recent (well-documented)
    {'name': 'MIS 1', 'start_ma': 0.014, 'end_ma': 0.0, 'type': 'warm',
     'note': 'Holocene (current interglacial)<br>Stable climate enables agriculture,<br>civilization, and global expansion.<br>Began ~11,700 years ago.'},
    {'name': 'MIS 2', 'start_ma': 0.029, 'end_ma': 0.014, 'type': 'cold',
     'note': 'Last Glacial Maximum (LGM)<br>Ice sheets at maximum extent.<br>Sea level 120m lower; land bridges open.<br>Humans confined to refugia.'},
    {'name': 'MIS 3', 'start_ma': 0.057, 'end_ma': 0.029, 'type': 'warm',
     'note': 'Interstadial (variable climate)<br>H. sapiens expands into Europe.<br>Coexistence with Neanderthals.<br>Cave art, symbolic behavior flourishes.'},
    {'name': 'MIS 4', 'start_ma': 0.071, 'end_ma': 0.057, 'type': 'cold',
     'note': 'Glacial period<br>[WARN] TOBA SUPERERUPTION (~74 ka)<br>Possible population bottleneck.<br>Volcanic winter, 6-10 year impact.'},
    
    # MIS 5 complex (substages)
    {'name': 'MIS 5a-d', 'start_ma': 0.130, 'end_ma': 0.071, 'type': 'warm',
     'note': 'Interglacial complex (variable)<br>Multiple warm/cool oscillations.<br>Sapiens and Neanderthals interbreed.<br>Out of Africa migrations begin.'},
    {'name': 'MIS 5e', 'start_ma': 0.130, 'end_ma': 0.115, 'type': 'warm',
     'note': '[EARTH] EEMIAN INTERGLACIAL<br>Last time as warm as today (naturally).<br>"Green Sahara" - corridor OPEN.<br>First major H. sapiens expansion.<br>Hippos in the Thames, lions in Alaska.'},
    
    # Deeper time
    {'name': 'MIS 6', 'start_ma': 0.191, 'end_ma': 0.130, 'type': 'cold',
     'note': '[SNOW] PENULTIMATE GLACIAL<br>Severe cold; Sahara impassable.<br>Populations isolated in refugia.<br>May have triggered 80/20 ghost split<br>that later formed H. sapiens.'},
    {'name': 'MIS 7', 'start_ma': 0.243, 'end_ma': 0.191, 'type': 'warm',
     'note': 'Interglacial<br>Corridor open; population mixing.<br>Early H. sapiens features emerging<br>in African fossil record.'},
    {'name': 'MIS 11', 'start_ma': 0.424, 'end_ma': 0.374, 'type': 'warm',
     'note': '[SUN] SUPER-INTERGLACIAL<br>Longest warm period of Pleistocene.<br>~50,000 years of warmth.<br>H. heidelbergensis flourishing.<br>Best analog for future climate?'},
    {'name': 'MIS 12', 'start_ma': 0.478, 'end_ma': 0.424, 'type': 'cold',
     'note': 'Severe glacial period<br>One of the coldest of Pleistocene.<br>Major evolutionary pressure.'},
]

# Special climate events (not MIS stages but significant)
CLIMATE_EVENTS = [
    {'name': 'Toba Supereruption', 'age_ma': 0.074, 'type': 'catastrophe',
     'note': '[VOLCANO] TOBA SUPERERUPTION (~74 ka)<br>Largest eruption in 2 million years.<br>Volcanic Explosivity Index 8.<br>6-10 year volcanic winter.<br>Proposed genetic bottleneck in humans<br>(debated but significant).<br><i>Source: Ambrose 1998; Rampino & Self 1992</i>'},
    {'name': 'Green Sahara (MIS 5e)', 'age_ma': 0.125, 'type': 'corridor',
     'note': '[TREE] GREEN SAHARA WINDOW<br>Sahara transforms to grassland/lakes.<br>Migration corridor OPEN.<br>H. sapiens expands into Levant.<br>First wave Out of Africa.<br><i>Source: Drake et al. 2011</i>'},
    {'name': 'Green Sahara (Holocene)', 'age_ma': 0.009, 'type': 'corridor',
     'note': '[TREE] AFRICAN HUMID PERIOD<br>Sahara green again (~11-5 ka).<br>Lakes, rivers, human settlements.<br>Cattle herding, rock art.<br>Ended ~5,500 ya [OK] desertification.<br><i>Source: deMenocal et al. 2000</i>'},
]

def d18o_to_temperature_approx(d18o_values):
    """
    Convert benthic delta18O to approximate temperature anomaly
    
    This is a simplified conversion. Benthic delta18O reflects both 
    ice volume and deep ocean temperature. The relationship varies
    over time, but rough approximation:
    - Higher delta18O = More ice + Colder temperatures
    - Lower delta18O = Less ice + Warmer temperatures
    
    Using simplified conversion: ~4-5 degC per 1 permil change
    Normalized to show relative changes from present
    """
    # Modern benthic delta18O is around 3.2 permil
    modern_d18o = 3.23  # From LR04 data at 0 ka
    
    # Convert to temperature anomaly (inverted because higher delta18O = colder)
    # Using ~4.5 degC per 1 permil as approximation
    temp_anomaly = -(np.array(d18o_values) - modern_d18o) * 4.5
    
    return temp_anomaly

def load_lr04_data():
    """Load LR04 benthic stack from cache"""
    try:
        with open(LR04_CACHE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def load_scotese_phanerozoic_data():
    """
    Load Scotese et al. (2021) Phanerozoic temperature data
    
    Returns global average temperatures from 540 Ma to 0 Ma
    Based on pole-to-equator temperature reconstructions
    """
    try:
        import csv
        
        ages_ma = []
        temps_global = []
        
        with open(SCOTESE_PHANEROZOIC, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            
            # Read header row (ages)
            header = next(reader)
            # Remove the 'latitude/age' label and convert to float
            age_values = [float(age) for age in header[1:]]
            
            # Read all latitude rows
            temp_grid = []
            for row in reader:
                if row and row[0]:  # Skip empty rows
                    try:
                        # Skip the latitude label, convert temps to float
                        temps = [float(t) for t in row[1:] if t]
                        if temps:  # Only add non-empty rows
                            temp_grid.append(temps)
                    except (ValueError, IndexError):
                        continue
            
            # Calculate global average by averaging across all latitudes for each age
            if temp_grid:
                # Convert to numpy for easier calculation
                import numpy as np
                temp_array = np.array(temp_grid)
                
                # Global average is mean across all latitudes (rows)
                global_avg_temps = np.mean(temp_array, axis=0)
                
                ages_ma = age_values
                temps_global = global_avg_temps.tolist()
        
        if ages_ma and temps_global:
            return {
                'ages_ma': ages_ma,
                'temp_global': temps_global
            }
        return None
        
    except (FileNotFoundError, Exception) as e:
        print(f"Warning: Could not load Scotese Phanerozoic data: {e}")
        return None


def load_holocene_data():
    """Load Kaufman et al. (2020) Holocene temperature reconstruction"""
    holocene_file = os.path.join(PALEO_DATA_DIR, 'temp12k_allmethods_percentiles.csv')
    
    try:

        import csv
        ages_years = []
        temps_median = []
        temps_5th = []
        temps_95th = []
        
        with open(holocene_file, 'r') as f:
            reader = csv.DictReader(f)
            # Strip whitespace from fieldnames
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            for row in reader:
                ages_years.append(float(row['ages']))
                temps_median.append(float(row['global_median']))
                temps_5th.append(float(row['global_5']))
                temps_95th.append(float(row['global_95']))
        
        # Convert years BP to Ma BP
        ages_ma = [age / 1_000_000 for age in ages_years]
        
        return {
            'ages_ma': ages_ma,
            'temp_median': temps_median,
            'temp_5th': temps_5th,
            'temp_95th': temps_95th
        }
    except (FileNotFoundError, KeyError) as e:
        print(f"Warning: Could not load Holocene data: {e}")
        return None

def calculate_preindustrial_offset(holocene_data):
    """
    Calculate offset to normalize to pre-industrial (1850-1900) baseline
    
    The Kaufman data is relative to 19th century. We need to find what
    the temperature was during 1850-1900 period (roughly 75-125 years BP)
    and use that as our zero point.
    """
    if not holocene_data:
        return 0.0
    
    ages_years = [age * 1_000_000 for age in holocene_data['ages_ma']]
    temps = holocene_data['temp_median']
    
    # Find temperatures for 1850-1900 period (75-175 years BP to be safe)
    preindustrial_temps = []
    for age, temp in zip(ages_years, temps):
        if 75 <= age <= 175:
            preindustrial_temps.append(temp)
    
    if preindustrial_temps:
        # Average of pre-industrial period
        return np.mean(preindustrial_temps)
    else:
        # If we don't have data for that exact period, use closest point
        # Find index closest to 100 years BP
        closest_idx = min(range(len(ages_years)), 
                         key=lambda i: abs(ages_years[i] - 100))
        return temps[closest_idx]

def load_modern_temperature_data():
    """Load modern instrumental temperature data to extend to present"""
    try:
        with open('data/temperature_giss_monthly.json', 'r') as f:
            data = json.load(f)
        
        records = data['data']
        
        # Convert to arrays and get annual averages
        years = []
        temps = []
        
        for record in records:
            year = record['year']
            
            if year not in years:
                years.append(year)
                # Get all months for this year that have valid data
                year_temps = [r['anomaly_c'] for r in records 
                             if r['year'] == year and r['anomaly_c'] is not None]
                if year_temps:
                    temps.append(np.mean(year_temps))
                else:
                    # Skip years with no valid data
                    years.pop()
        
        # Convert years to Ma BP (millions of years before present)
        # Present = 2025, so years before present = 2025 - year
        # Ma = (2025 - year) / 1,000,000
        current_year = 2025
        ages_ma = [(current_year - y) / 1_000_000 for y in years]
        
        return ages_ma, temps
        
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Warning: Could not load modern temperature data: {e}")
        return None, None

def create_paleoclimate_visualization():
    """
    Create Phanerozoic paleoclimate visualization
    
    Shows temperature over the past 540 million years with:
    - Geologic period shading
    - Multiple datasets: Scotese (540-5 Ma), LR04 (5-0.01 Ma), Holocene (12 ka), Modern (1880-present)
    - Zoomable to see detail from hundreds of millions of years down to millennia
    """
    
    if not PLOTLY_AVAILABLE:
        return None
    
    # Load all data sources
    scotese_data = load_scotese_phanerozoic_data()
    lr04_data = load_lr04_data()
    holocene_data = load_holocene_data()
    modern_ages_ma, modern_temps = load_modern_temperature_data()
    
    # Calculate pre-industrial baseline offset
    preindustrial_offset = calculate_preindustrial_offset(holocene_data) if holocene_data else 0.0
    
    # --- Process LR04 Data ---
    if not lr04_data:
        return None
    
    records = lr04_data['data']
    ages_ka = np.array([r['age_ka_bp'] for r in records])
    d18o_values = np.array([r['d18o_permil'] for r in records])
    ages_ma_lr04 = ages_ka / 1000.0
    temp_anomaly_lr04 = d18o_to_temperature_approx(d18o_values)
    temp_anomaly_lr04 = temp_anomaly_lr04 - preindustrial_offset
    
    # Filter to end at Holocene start (12 ka = 0.012 Ma)
    # LR04 optimized for ice age cycles; Kaufman better for Holocene
    holocene_start_ma = 0.012
    mask_lr04 = ages_ma_lr04 >= holocene_start_ma
    ages_ma_lr04 = ages_ma_lr04[mask_lr04]
    temp_anomaly_lr04 = temp_anomaly_lr04[mask_lr04]

    # --- Process Scotese Data ---
    scotese_ages_ma = None
    scotese_temps = None
    
    if scotese_data:
        scotese_ages_ma = np.array(scotese_data['ages_ma'])
        scotese_temps_raw = np.array(scotese_data['temp_global'])
        
        # Normalize Scotese data to match LR04 at the transition point (~5 Ma)
        # Find Scotese value at 5 Ma
        transition_age = 5.0
        scotese_at_transition = np.interp(transition_age, scotese_ages_ma, scotese_temps_raw)
        
        # Find LR04 value at 5 Ma
        lr04_at_transition = np.interp(transition_age, ages_ma_lr04, temp_anomaly_lr04)
        
        # Calculate offset to align them
        scotese_offset = lr04_at_transition - scotese_at_transition
        scotese_temps = scotese_temps_raw + scotese_offset
        
        # Filter to use Scotese data for deep time (>2 Ma)
        # Scotese method: Lithologic indicators + Koppen belts (~5 Myr resolution)
        # Optimized for deep time patterns, not high-resolution recent climate
        # Use LR04/Holocene/Modern for <2 Ma (higher temporal resolution)
        mask = scotese_ages_ma >= 2.0
        scotese_ages_ma = scotese_ages_ma[mask]
        scotese_temps = scotese_temps[mask]

    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=1, cols=1,
        specs=[[{"secondary_y": True}]]
    )
    
    # Add Scotese Phanerozoic temperature trace (540-5 Ma) - plotted first so it's behind
    if scotese_ages_ma is not None and scotese_temps is not None:
        fig.add_trace(
            go.Scatter(
                x=scotese_ages_ma,
                y=scotese_temps,
                mode='lines',
                name='Phanerozoic Global Temperature (Scotese et al. 2021)',
                line=dict(color='#003049', width=2),
        #        hovertemplate='Age: %{x:.1f} Ma<br>Temp Anomaly: %{y:.1f} degC<extra></extra>'
                hovertemplate='Age: %{x:.1f} Ma<br>Temp Anomaly: %{y:.1f} degC<br><i>~5 Myr resolution (deep time method)</i><extra></extra>'
            ),
            secondary_y=False
        )
    
    # Add LR04 temperature trace (5.3 Ma - 10 ka)
    fig.add_trace(
        go.Scatter(
            x=ages_ma_lr04,
            y=temp_anomaly_lr04,
            mode='lines',
            name='Paleoclimate Benthic Stack (Lisiecki & Raymo 2005)',
            line=dict(color='#C1121F', width=1.5),
            hovertemplate='Age: %{x:.3f} Ma<br>Temp Anomaly: %{y:.1f} degC<extra></extra>'
        ),
        secondary_y=False
    )
    
    # Add Holocene reconstruction trace
    if holocene_data:
        # Normalize Holocene data to pre-industrial
        holocene_temps_normalized = [t - preindustrial_offset for t in holocene_data['temp_median']]
        
        # Filter to end at 1880 CE (where instrumental record begins)
        # 1880 CE = 145 years before 2025 = 0.000145 Ma
        instrumental_start_ma = 0.000145
        holocene_ages_filtered = []
        holocene_temps_filtered = []
        for age, temp in zip(holocene_data['ages_ma'], holocene_temps_normalized):
            if age >= instrumental_start_ma:  # Older than 1880
                holocene_ages_filtered.append(age)
                holocene_temps_filtered.append(temp)

        fig.add_trace(
            go.Scatter(
        #        x=holocene_data['ages_ma'],
        #        y=holocene_temps_normalized,
                x=holocene_ages_filtered,
                y=holocene_temps_filtered,                
                mode='lines',
                name='Holocene Reconstruction (Kaufman 2020)',
                line=dict(color="#2CC174", width=2),
                hovertemplate='Age: %{x:.6f} Ma<br>Temp Anomaly: %{y:.2f} degC<extra></extra>'
            ),
            secondary_y=False
        )

    # ADD THIS: Add modern instrumental data
    if modern_ages_ma and modern_temps:

        # Normalize instrumental data to pre-industrial
        # NASA GISS is relative to 1951-1980, need to shift to 1850-1900
        # From literature: 1951-1980 was ~0.7 degC warmer than 1850-1900
        giss_to_preindustrial_offset = 0.7
        modern_temps_normalized = [t + giss_to_preindustrial_offset - preindustrial_offset 
                                   for t in modern_temps]
        
        fig.add_trace(
            go.Scatter(
                x=modern_ages_ma,
                y=modern_temps,
                mode='lines',
                name='Instrumental Record 1880-2025 (NASA GISS)',
                line=dict(color="#3586B5", width=3),  # Bright orange-red
                hovertemplate='Year: %{customdata}<br>Temp Anomaly: %{y:.2f} degC<extra></extra>',
                customdata=[2025 - int(age * 1_000_000) for age in modern_ages_ma]
            ),
            secondary_y=False
        )
        
        # Add Younger Dryas regional temperature bands
        # Shows spatial heterogeneity: different regions experienced different cooling
        # Based on paleoclimate reconstructions and ice core data
        
        yd_start = 0.0129  # 12,900 years ago
        yd_end = 0.0117    # 11,700 years ago
        
        # Band 1: Global average cooling (~0.5-1.5 degC)
        # Subtle signal when averaged over entire planet
        fig.add_trace(
            go.Scatter(
                x=[yd_start, yd_start, yd_end, yd_end, yd_start],
                y=[0, -1.5, -1.5, 0, 0],
                fill='toself',
                fillcolor='rgba(0,206,209,0.1)',  # Very light turquoise
                line=dict(width=0),
                mode='lines',
                name='YD Global (~1 degC)',
                showlegend=False,
                hovertemplate='Younger Dryas (Global)<br>Estimated: 0.5-1.5 degC cooling<br><i>Global average signal</i><extra></extra>'
            ),
            secondary_y=False
        )
        
        # Band 2: Northern Hemisphere mid-latitudes (Europe & North America, ~2-6 degC)
        # Regional cooling where most humans lived
        fig.add_trace(
            go.Scatter(
                x=[yd_start, yd_start, yd_end, yd_end, yd_start],
                y=[-2, -6, -6, -2, -2],
                fill='toself',
                fillcolor='rgba(0,206,209,0.4)',  # Medium turquoise
                line=dict(width=0),
                mode='lines',
                name='YD Regional (~4 degC)',
                showlegend=False,
                hovertemplate='Younger Dryas (Regional)<br>Europe & North America: 2-6 degC cooling<br><i>Mid-latitude Northern Hemisphere</i><extra></extra>'
            ),
            secondary_y=False
        )
        
        # Band 3: Greenland/North Atlantic extreme (~8-10 degC)
        # Maximum regional impact from ice core records
        fig.add_trace(
            go.Scatter(
                x=[yd_start, yd_start, yd_end, yd_end, yd_start],
                y=[-8, -10, -10, -8, -8],
                fill='toself',
                fillcolor='rgba(0,206,209,0.9)',  # Darker turquoise
                line=dict(width=0),
                mode='lines',
                name='YD Greenland (~9 degC)',
                showlegend=False,
                hovertemplate='Younger Dryas (Greenland)<br>GISP2 ice core: 8-10 degC cooling<br><i>Maximum regional impact</i><extra></extra>'
            ),
            secondary_y=False
        )

        # ============================================================
        # MARINE ISOTOPE STAGES (MIS) - Pleistocene Climate Pulses
        # Vertical bands showing glacial (cold/blue) and interglacial
        # (warm/red) periods that controlled migration corridors
        # ============================================================
        
        for mis in MIS_STAGES:
            # Different colors for warm (interglacial) vs cold (glacial)
            if mis['type'] == 'warm':
                color = "rgba(255, 99, 71, 0.12)"  # Tomato, subtle
            else:
                color = "rgba(100, 149, 237, 0.12)"  # Cornflower blue, subtle
            
            fig.add_vrect(
                x0=mis['start_ma'], x1=mis['end_ma'],
                fillcolor=color,
                layer="below",
                line_width=0,
            )
            
            # Add hoverable annotation at top of each MIS band
            mid_x = (mis['start_ma'] + mis['end_ma']) / 2
            fig.add_trace(
                go.Scatter(
                    x=[mid_x],
                    y=[8.5],  # Near top of chart
                    mode='markers',
                    marker=dict(
                        symbol='diamond' if mis['type'] == 'warm' else 'square',
                        size=8,
                        color='rgba(255, 99, 71, 0.7)' if mis['type'] == 'warm' else 'rgba(100, 149, 237, 0.7)',
                        line=dict(width=1, color='white')
                    ),
                    hovertemplate=(
                        f"<b>{mis['name']}</b><br>"
                        f"<b>{mis['start_ma']*1000:.0f} - {mis['end_ma']*1000:.0f} ka</b><br>"
                        f"{mis['note']}"
                        "<extra></extra>"
                    ),
                    showlegend=False
                ),
                secondary_y=False
            )
        
        # Add special climate events (Toba, Green Sahara windows)
        for event in CLIMATE_EVENTS:
            # Different markers for different event types
            if event['type'] == 'catastrophe':
                symbol = 'triangle-down'
                color = 'rgba(255, 0, 0, 0.8)'
                size = 12
            else:  # corridor
                symbol = 'star'
                color = 'rgba(34, 139, 34, 0.8)'
                size = 10
            
            fig.add_trace(
                go.Scatter(
                    x=[event['age_ma']],
                    y=[7.5],  # Slightly below MIS markers
                    mode='markers',
                    marker=dict(
                        symbol=symbol,
                        size=size,
                        color=color,
                        line=dict(width=1, color='white')
                    ),
                    hovertemplate=(
                        f"<b>{event['name']}</b><br>"
                        f"<b>{event['age_ma']*1000:.0f} ka</b><br>"
                        f"{event['note']}"
                        "<extra></extra>"
                    ),
                    showlegend=False
                ),
                secondary_y=False
            )

        # ============================================================
        # HOMININ EVOLUTION MARKERS
        # Small triangle markers at bottom of chart showing earliest
        # evidence for key hominoid/hominin species
        # 
        # Two marker types:
        #   - Filled triangles: fossil-confirmed species
        #   - Open triangles: ghost populations (DNA-only evidence)
        #
        # Markers use manual y_offset values defined in HOMININ_SPECIES
        # for precise control over vertical positioning.
        # ============================================================
        
        # Base y-position
        base_y_position = -10.0
        
        # Build y-positions from manual offsets
        species_y_positions = {
            sp['name']: base_y_position + sp.get('y_offset', 0.0)
            for sp in HOMININ_SPECIES
        }
        
        # Separate fossil-confirmed from ghost populations
        fossil_species = [sp for sp in HOMININ_SPECIES if sp.get('evidence', 'fossil') == 'fossil']
        ghost_species = [sp for sp in HOMININ_SPECIES if sp.get('evidence') == 'dna_only']
        
        # Add faint vertical lines from each marker down to x-axis (all species)
        for sp in HOMININ_SPECIES:
            # Use slightly different line style for ghost populations
            line_alpha = 0.2 if sp.get('evidence') == 'dna_only' else 0.3
            marker_y = species_y_positions[sp['name']]
            fig.add_shape(
                type="line",
                x0=sp['age_ma'],
                y0=marker_y,
                x1=sp['age_ma'],
                y1=9.5,  # Extend to top of chart area
                line=dict(
                    color=f"rgba(128, 128, 128, {line_alpha})",
                    width=1,
                    dash="dot"
                ),
                xref="x",
                yref="y"
            )
        
        # Add FOSSIL-CONFIRMED species (filled triangles)
        if fossil_species:
            fossil_ages = [sp['age_ma'] for sp in fossil_species]
            fossil_y = [species_y_positions[sp['name']] for sp in fossil_species]
            fossil_names = [sp['name'] for sp in fossil_species]
            fossil_notes = [sp['note'] for sp in fossil_species]
            
            fig.add_trace(
                go.Scatter(
                    x=fossil_ages,
                    y=fossil_y,
                    mode='markers',
                    marker=dict(
                        symbol='triangle-up',
                        size=10,
                        color='rgba(70, 70, 70, 0.7)',
                        line=dict(width=1, color='#333')
                    ),
                    hovertemplate=(
                        '<b>%{customdata[0]}</b><br>'
                        '<b>%{customdata[1]:.2f} Ma</b><br>'
                        '%{customdata[2]}'
                        '<extra></extra>'
                    ),
                    customdata=[[name, age, note] for name, age, note in 
                               zip(fossil_names, fossil_ages, fossil_notes)],
                    name='Hominin species earliest evidence (fossil)',
                    showlegend=True
                ),
                secondary_y=False
            )
        
        # Add GHOST POPULATIONS (open triangles)
        if ghost_species:
            ghost_ages = [sp['age_ma'] for sp in ghost_species]
            ghost_y = [species_y_positions[sp['name']] for sp in ghost_species]
            ghost_names = [sp['name'] for sp in ghost_species]
            ghost_notes = [sp['note'] for sp in ghost_species]
            
            fig.add_trace(
                go.Scatter(
                    x=ghost_ages,
                    y=ghost_y,
                    mode='markers',
                    marker=dict(
                        symbol='triangle-up-open',  # Open triangle
                        size=11,
                        color='rgba(100, 100, 100, 0.9)',
                        line=dict(width=2, color='#555')
                    ),
                    hovertemplate=(
                        '<b>%{customdata[0]}</b><br>'
                        '<b>Split time: ~%{customdata[1]:.1f} Ma</b><br>'
                        '%{customdata[2]}'
                        '<extra></extra>'
                    ),
                    customdata=[[name, age, note] for name, age, note in 
                               zip(ghost_names, ghost_ages, ghost_notes)],
                    name='"Ghost" populations earliest evidence (DNA only)',
                    showlegend=True
                ),
                secondary_y=False
            )
        
        # Add legend entries for MIS stages
        # Warm/Interglacial legend entry
        fig.add_trace(
            go.Scatter(
                x=[None], y=[None],
                mode='markers',
                marker=dict(symbol='diamond', size=10, color='rgba(255, 99, 71, 0.7)'),
                name='Marine Isotope Stages (MIS) - Warm',
                showlegend=True
            ),
            secondary_y=False
        )
        # Cold/Glacial legend entry
        fig.add_trace(
            go.Scatter(
                x=[None], y=[None],
                mode='markers',
                marker=dict(symbol='square', size=10, color='rgba(100, 149, 237, 0.7)'),
                name='Marine Isotope Stages (MIS) - Cold',
                showlegend=True
            ),
            secondary_y=False
        )
        # Climate events legend entry
        fig.add_trace(
            go.Scatter(
                x=[None], y=[None],
                mode='markers',
                marker=dict(symbol='star', size=10, color='rgba(34, 139, 34, 0.8)'),
                name='Climate Windows',
                showlegend=True
            ),
            secondary_y=False
        )

        # Mark "present day"
        fig.add_vline(
            x=0.000001,  # Very close to present (1 year ago)
            line_dash="solid",
            line_color="red",
            line_width=2
        )
        
        # Add annotation for present - positioned at far right
        fig.add_annotation(
            x=np.log10(0.000001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.0,  # Use relative positioning (top of plot)
            yref="paper",
            text="2025",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>Present Day (2025 CE)</b><br>'
                      'Global temp: +1.28 degC above pre-industrial<br>'
                      'Atmospheric CO2: ~425 ppm<br>'
                      'Warmest decade in recorded history<br>'
                      'Rate of change: ~0.2 degC per decade<br>'
                      'Unprecedented in Holocene stability',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # =====================================================================
        # RECENT HEAT EVENTS - Reference to Earth System Controller
        # Add this after the existing annotations (around line 1765)
        # =====================================================================

        # Recent Heat Events marker (clusters all modern events)
        fig.add_annotation(
            x=np.log10(0.000005),  # visible near right edge
            y=6.0,  # Slightly above current anomaly line
            text='VIEW HEAT WAVES',
            showarrow=False,
            font=dict(size=9, color='#FF4500'),  # Orange-red
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#FF4500',
            borderwidth=2,
            borderpad=4,
            hovertext='<b>View Recent Extreme Heat Events in Google Earth</b><br>'
                    '<br>'
                    '1995: Chicago Heat Wave (739 deaths)<br>'
                    '2003: Europe Heat Wave (70,000+ deaths)<br>'
                    '2021: Pacific NW Heat Dome (1,200+ deaths)<br>'
                    '2022: China Yangtze Basin (70-day event)<br>'
                    '2023: Amazon "Boiling River"<br>'
                    '2024: Mali/Sahel, Delhi Heat Belt, Persian Gulf<br>'
                    '2025: Pakistan Heat Wave<br>'
                    '<br>'
                    '<b>KML layers available in data/ folder</b><br>'
                    'Use KML Layer Controller in Earth System Visualization to open<br>'
                    'Note: Google Earth Pro preinstalled required to open KML files',
            hoverlabel=dict(bgcolor='rgba(255,69,0,0.9)', font_size=11, font_color='white')
        )

        # Add annotation for 10 years ago (2015) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.00001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.0,  # Use relative positioning (top of plot)
            yref="paper",
            text="2015",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>2015 CE</b><br>'
                      'Year of Paris Climate Agreement<br>'
                      'Global temp: +1.0 degC above pre-industrial<br>'
                      'Hottest year on record (at the time)<br>'
                      '196 nations commit to climate action<br>'
                      'Beginning of renewable energy surge',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 100 years ago (1925) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.0001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.0,  # Use relative positioning (top of plot)
            yref="paper",
            text="1925",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>1925 CE</b><br>'
                      'The Roaring Twenties<br>'
                      'Global temp: ~0.1 degC above pre-industrial<br>'
                      'World population: 2 billion<br>'
                      'Early automobile age begins<br>'
                      'CO2 starting to rise from coal use<br>'
                      'Beginning of modern warming signal',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 1000 years ago (1025) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.001),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="1025",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>1025 CE (Medieval Period)</b><br>'
                      'Height of Medieval Warm Period<br>'
                      'Vikings settled Greenland<br>'
                      'Stable Holocene climate continues<br>'
                      'Global temp within Holocene range<br>'
                      'Agriculture thriving across Europe/Asia<br>'
                      'Pre-industrial baseline conditions',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )  

        # Add annotation for 10,000 years ago (10,000 bce) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.01),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="10,000 BCE",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>10,000 BCE</b><br>'
                      'End of last Ice Age<br>'
                      'Beginning of Holocene interglacial<br>'
                      'Agricultural Revolution begins<br>'
                      'Humans start farming in Fertile Crescent<br>'
                      'Climate stability enables civilization<br>'
                      'World population: ~5 million',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )                       

        # Add annotation for 100,000 years ago (100,000 bce) - positioned at far right
        fig.add_annotation(
            x=np.log10(0.1),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="100,000 BCE",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>100,000 BCE</b><br>'
                      'Deep in Pleistocene Ice Age<br>'
                      'Modern humans in Africa<br>'
                      'Neanderthals in Europe<br>'
                      'Sea levels ~100m lower than today<br>'
                      'Massive ice sheets cover continents<br>'
                      'Temp ~5-10 degC colder than present',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )  

        # Add annotation for 1,000,000 years ago (1,000,000 bce) - positioned at far right
        fig.add_annotation(
            x=np.log10(1.0),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="1 million BCE (1 Ma)",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>1 Million Years Ago</b><br>'
                      'Early Pleistocene Ice Age<br>'
                      'Homo erectus using fire<br>'
                      '100,000-year glacial cycles begin<br>'
                      'Ice sheets grow and retreat<br>'
                      'Human ancestors adapting to change<br>'
                      'Stone tool technology advancing',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )  

        # Add annotation for 10 Ma years ago - positioned at far right
        fig.add_annotation(
            x=np.log10(10),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="10 Ma",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>10 Million Years Ago</b><br>'
                      'Late Miocene Epoch<br>'
                      'Grasslands expanding worldwide<br>'
                      'Great apes diversifying in Africa<br>'
                      'Antarctica fully ice-covered<br>'
                      'Global cooling trend underway<br>'
                      'Modern ocean circulation patterns form',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        )

        # Add annotation for 100 Ma years ago - positioned at far right
        fig.add_annotation(
            x=np.log10(100),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="100 Ma",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>100 Million Years Ago</b><br>'
                      'Mid-Cretaceous greenhouse world<br>'
                      'Dinosaurs at peak diversity<br>'
                      'No polar ice caps<br>'
                      'Sea levels 200m higher than today<br>'
                      'CO2 ~4x higher than pre-industrial<br>'
                      'Temp ~10 degC warmer than present',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        ) 

        # Add annotation for 540 Ma years ago - positioned at far right
        fig.add_annotation(
            x=np.log10(540),  # Use log10 for log-scale x-axis
            xref='x',            
            y=1.00,  # Use relative positioning (top of plot)
            yref="paper",
            text="<540 Ma",
            showarrow=False,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='red',
            ax=0,
            ay=-40,
            font=dict(size=10, color='red'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='red',
            borderwidth=1,
            hovertext='<b>Phanerozoic Eon (0.538 billion years)</b><br>'
                      'Beginning of Cambrian Period 538.8 million years ago. Cambrian Explosion of life.<br>'
                      'First animals with shells. Trilobites, early fish appear. Complex ecosystems emerge.<br><br>'
                      '<b>Proterozoic Eon (2.0 billion years)</b><br>'
                      '2.5 Billion Years Ago (Ga) to 538.8 Million Years Ago (Ma)<br>'
                      'Great Oxidation Event. Complex (eukaryotic) cells. Assembly and breakup of supercontinents.<br>' 
                      'First large, soft-bodied multicellular animals (Ediacaran biota).<br><br>'
                      '<b>Archean Eon (1.5 billion years)</b><br>'
                      '4.0 Ga to 2.5 Ga<br>'
                      'Formation of the first continental crust (cratons), the cooling of the planet, and the<br>' 
                      'origin of life (represented by microbial fossils like stromatolites).<br><br>'
                      '<b>Hadean Eon (0.5 billion years)</b><br>'
                      '4.54 Ga to 4.0 Ga<br>'
                      'Earth\'s formation (4.54 Ga). Intense meteorite bombardment.<br>' 
                      'Initial differentiation of the planet\'s core, mantle, and crust.',
            hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
        ) 

# Add geologic period shading - use actual Ma values, not log
    for period in GEOLOGIC_PERIODS:
        # Use the actual Ma values - the log axis will transform them
        fig.add_shape(
            type="rect",
            xref="x",
            yref="paper",
            x0=period['start'],  # Use actual value, not log!
            y0=0,
            x1=period['end'],     # Use actual value, not log!
            y1=1,
            fillcolor=period['color'],
            opacity=0.2,
            layer="below",
            line_width=0
        )
        
        # Calculate midpoint and width in log space for label positioning
        start_log = np.log10(period['start'])
        end_log = np.log10(period['end'])
        midpoint_log = (start_log + end_log) / 2
        period_width = abs(start_log - end_log)
        
        # Adjust font size based on period width
        if period_width > 0.3:
            font_size = 10
            opacity = 1.0
        elif period_width > 0.15:
            font_size = 8
            opacity = 0.9
        else:
            font_size = 7
            opacity = 0.8
        
        # But for annotations, we still need log space
        fig.add_annotation(
            x=midpoint_log,
            xref="x",
            y=1.02,
            yref="paper",
            text=period['name'],
            showarrow=False,
            font=dict(size=font_size, color='#333'),
            textangle=-45,
            xanchor='left',
            yanchor='bottom',
            opacity=opacity
        )


    # Add era labels (broader time divisions)
    eras = [
        {'name': 'Precambrian', 'start': 4500, 'end': 541, 'color': '#8B4789'},
        {'name': 'Paleozoic', 'start': 541, 'end': 252.2, 'color': '#7FA056'},
        {'name': 'Mesozoic', 'start': 252.2, 'end': 66.0, 'color': '#34B2C9'},
        {'name': 'Cenozoic', 'start': 66.0, 'end': 0.000001, 'color': '#FD9A52'}
    ]
    
    """
    # Add Phanerozoic Eon label (spans Paleozoic + Mesozoic + Cenozoic)
    # Calculate midpoint across all three Phanerozoic eras
    phanerozoic_start = 541  # Beginning of Cambrian
    phanerozoic_end = 0.000001  # Present
    phanerozoic_midpoint_log = (np.log10(phanerozoic_start) + np.log10(phanerozoic_end)) / 2
    
    fig.add_annotation(
        x=phanerozoic_midpoint_log,
        y=1.065,  # Position above era labels
        yref="paper",
        text="<b>PHANEROZOIC EON (540 Ma - Present)</b>",
        showarrow=False,
        font=dict(size=14, color='#2C5F2D'),  # Dark green
        xanchor='center',
        yanchor='bottom',
        bgcolor='rgba(255,255,255,0.7)',
        bordercolor='#2C5F2D',
        borderwidth=2,
        borderpad=4
    )
    """
    
    for era in eras:
        # Calculate midpoint in log space
        midpoint_log = (np.log10(era['start']) + np.log10(era['end'])) / 2
        
        fig.add_annotation(
            x=midpoint_log,
            y=1.00,  # Position above the period labels
            yref="paper",
            text=f"<b>{era['name']}</b>",
            showarrow=False,
            font=dict(size=12, color=era['color']),
            xanchor='center',
            yanchor='bottom'
        )

    # Mark the Holocene explicitly
    fig.add_trace(
        go.Scatter(
            x=[0.0117, 0.0117],
    #        y=[temp_anomaly_lr04.min(), temp_anomaly_lr04.max()],
            y=[-13.0, 0.0],            
            mode='lines',
            name='Holocene Begins (11.7 ka)',
            line=dict(color='green', width=2, dash='dash'),
            showlegend=False,
            hoverinfo='skip'
        ),
        secondary_y=False
    )
    
    # ax=0, ay=-40 [OK] Straight down [DOWN]
    # ax=40, ay=0 [OK] Straight right [RIGHT]
    # ax=40, ay=-60 [OK] Diagonal up-right [UP-RIGHT]
    # ax=-40, ay=40 [OK] Diagonal down-left [DOWN-LEFT]

    # Anthropocene (recent, so use arrow like others)
    fig.add_annotation(
        x=np.log10(0.000075),  # 1950 CE is 75 years ago
        y=0.0,
        text='Proposed Anthropocene<br>(after 1950 CE)',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='red',
        ax=28,
        ay=-70,
        font=dict(size=9, color='red'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='red',
        borderwidth=1,
        hovertext='<b>Proposed Anthropocene Epoch</b><br>'
                  'Proposed start: 1950 CE (Great Acceleration)<br>'
                  'Human activity dominates Earth system<br>'
                  'Nuclear testing, plastic, concrete markers<br>'
                  'CO2 rising faster than any natural event<br>'
                  'Sixth mass extinction underway<br>'
                  'Geologists debate: new epoch or event?',
        hoverlabel=dict(bgcolor='rgba(220,20,60,0.9)', font_size=11)
    )

    # Origin of Humanity - about 350 to 160,000 years ago
    # Add visual period marker (blue shaded region showing event duration)
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.350,  # 350,000 ya
        x1=0.160,  # 160,000 ya
        y0=0,
        y1=1,
    #    fillcolor='#00D188,0.3', 
        fillcolor='rgba(0, 209, 136,0.1)',
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
        x=np.log10(0.25),  
        y=4.5,
        text='Origin of Humanity',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor="#00D188",  
        ax=0,
        ay=0, 
        font=dict(size=9, color='#00D188'),
        bgcolor='rgba(0, 209, 136,0)',
        bordercolor='#00D188',
        borderwidth=1,          
        hovertext='<b>Origin of Humanity (350,000-160,000 years ago)</b><br>'
        'The generally accepted range for the origin of Homo sapiens is between 300,000 and 200,000 years ago,<br>' 
        'although recent discoveries continually push the minimum date back. This range is based on the oldest<br>' 
        'widely recognized fossil evidence, all found in Africa.<br>' 
        '<b>Earliest Evidence (c. 300,000 years ago):</b> Fossils from the Jebel Irhoud site in Morocco, dated<br>' 
        'to approximately 300,000 years ago (with a range of 350,000 - 280,000 years ago), are currently the<br>' 
        'oldest known remains classified as early Homo sapiens. These specimens possess a mix of archaic and<br>' 
        'modern facial features.<br>' 
        '<b>Early Modern Humans (c. 233,000 - 160,000 years ago):</b><br>' 
        '- Omo I remains from Ethiopia, recently re-dated to at least 230,000 years ago.<br>' 
        '- Fossils from Herto, Ethiopia, dated to about 160,000 years ago.<br>' 
        '- The Florisbad Skull from South Africa, dated to about 260,000 years ago.<br>' 
        'The current scientific consensus suggests that Homo sapiens did not originate in a single "cradle"<br>' 
        'but rather emerged across the entire African continent from a widespread population of ancestral humans.<br>',                  
        hoverlabel=dict(bgcolor='rgba(0, 209, 136,0.7)', font_size=11)
    )

    # Younger Dryas - the "Big Freeze" that interrupted deglaciation
    # Add visual period marker (blue shaded region showing event duration)
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.0129,  # 12,900 years ago (start)
        x1=0.0117,  # 11,700 years ago (end)
        y0=0,
        y1=1,
        fillcolor='rgba(0,206,209,0)',  # Light turquoise
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
        x=np.log10(0.0123),  # ~12,300 years ago (middle of YD)
        y=-3.1,
        text='Younger Dryas<br>("Big Freeze")',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#00CED1',  # Dark turquoise
        ax=-95,
        ay=-95, 
        font=dict(size=9, color='#00CED1'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#00CED1',
        borderwidth=1,          
        hovertext='<b>Younger Dryas (12,900-11,700 years ago)</b><br>'
                  'Abrupt cooling event with regional variations:<br>'
                  '  * <b>Global</b>: ~1 degC cooling (averaged)<br>'
                  '  * <b>Europe/N. America</b>: 2-6 degC cooling<br>'
                  '  * <b>Greenland</b>: 8-10 degC cooling (ice cores)<br>'
                  '<i>Brief event smoothed in 100-year resolution data</i><br>'
                  'Meltwater disrupted Gulf Stream circulation<br>'
                  'Led to megafauna extinctions & agricultural origins<br>'
                  '<b>Three turquoise bands show regional cooling ranges</b>',                  
        hoverlabel=dict(bgcolor='rgba(0,206,209,0.9)', font_size=11)
    )
    
    # Add annotation for Holocene - positioned directly over the line
    fig.add_annotation(
#        x=0.0117,
        x=np.log10(0.0117),  # Use log10 for log-scale x-axis
        xref='x',        
        y=1.5,  # Adjust this value to position vertically where you want
        text="<b>Start of Holocene</b>",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='green',
        ax=0,
        ay=-42,
        font=dict(size=9, color='green'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='green',
        borderwidth=1,
        hovertext='<b>Holocene Begins (11,700 years ago)</b><br>'
                  'End of last glacial period<br>'
                  'Rapid warming of ~5 degC in centuries<br>'
                  'Ice sheets retreat, sea level rises 120m<br>'
                  'Stable, warm climate enables agriculture<br>'
                  'Human civilization flourishes<br>'
                  'Most stable climate in 800,000 years',
        hoverlabel=dict(bgcolor='rgba(34,139,34,0.9)', font_size=11)
    )

    # Medieval Warm Period
    # Add visual period marker (orange shaded region)
    # MWP: 950-1250 CE = 1075-775 years ago
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.001075,  # 950 CE (1075 years ago)
        x1=0.000775,  # 1250 CE (775 years ago)
        y0=0,
        y1=1,
        fillcolor='rgba(255,140,0,0.12)',  # Light orange
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
            x=np.log10(0.000925),  # ~1100 CE (middle of MWP) is 925 years ago
            y=0.10,
            text='Medieval Warm Period',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor='#FF8C00',  # Dark orange
            ax=-45,
            ay=-55,
            font=dict(size=9, color='#FF8C00'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#FF8C00',
            borderwidth=1,
            hovertext='<b>Medieval Warm Period (950-1250 CE)</b><br>'
                    'Regional warming in North Atlantic/Europe<br>'
                    'Vikings settled Greenland, agricultural boom<br>'
                    '<br>'
                    '<b>Temperature Ranges (see horizontal bands):</b><br>'
                    '* Regional (light orange): +0.3 to +0.5 degC<br>'
                    '* Global average (dark orange): +0.1 to +0.2 degC<br>'
                    '<br>'
                    '<i>Note: Century-scale event smoothed in 100-yr data</i><br>'
                    'Shows: Small global changes = large regional impacts<br>'
                    '<b>[ZOOM] Zoom to 500-1500 CE to see temperature bands clearly!</b><br>'
                    '<b>Orange vertical region shows event duration</b>',
            hoverlabel=dict(bgcolor='rgba(255,140,0,0.9)', font_size=11)
        )

# Medieval Warm Period - Temperature Range Bands
    # Showing BOTH regional and global ranges with nested opacity
    
    # Regional range (North Atlantic/Europe): ~+0.3 to +0.5 degC
    # Lighter, wider band showing local impact
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.001075,  # 950 CE
        x1=0.000775,  # 1250 CE
        y0=0.3,  # Regional range (wider)
        y1=0.5,
        fillcolor='rgba(255,140,0,0.15)',  # Light orange
        line=dict(width=0),  # No border (cleaner)
        layer="below"
    )
    
    # Global range: ~+0.1 to +0.2 degC
    # Darker, narrower band showing planetary average
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.001075,  # 950 CE
        x1=0.000775,  # 1250 CE
        y0=0.1,  # Global range (narrower)
        y1=0.2,
        fillcolor='rgba(255,140,0,0.35)',  # Darker orange
        line=dict(width=0),
        layer="below"
    )

    # Little Ice Age
    # Add visual period marker (blue shaded region)
    # LIA: 1300-1850 CE = 725-175 years ago
    fig.add_shape(
        type="rect",
        xref="x",
        yref="paper",
        x0=0.000725,  # 1300 CE (725 years ago)
        x1=0.000175,  # 1850 CE (175 years ago)
        y0=0,
        y1=1,
        fillcolor='rgba(65,105,225,0.12)',  # Light royal blue
        line=dict(width=0),
        layer="below"
    )
    
    fig.add_annotation(
        x=np.log10(0.000450),  # ~1575 CE (middle of LIA) is 450 years ago
        y=-0.2,
        text='Little Ice Age',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#4169E1',  # Royal blue
        ax=20,
        ay=-55, 
        font=dict(size=9, color='#4169E1'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#4169E1',
        borderwidth=1,
        hovertext='<b>Little Ice Age (1300-1850 CE)</b><br>'
                  'Regional cooling in North Atlantic/Europe<br>'
                  'Viking Greenland abandoned, Thames froze, famines<br>'
                  '<br>'
                  '<b>Temperature Ranges (see horizontal bands):</b><br>'
                  '* Regional (light blue): -0.5 to -1.0 degC<br>'
                  '* Global average (dark blue): -0.2 to -0.3 degC<br>'
                  '<br>'
                  '<i>Note: Best visible in regional high-res proxies</i><br>'
                  'Even small global changes affect civilizations<br>'
                  '<b>[ZOOM] Zoom to 1200-1900 CE to see temperature bands clearly!</b><br>'
                  '<b>Blue vertical region shows event duration</b>',
        hoverlabel=dict(bgcolor='rgba(65,105,225,0.9)', font_size=11)
    )

# Little Ice Age - Temperature Range Bands
    # Showing BOTH regional and global ranges with nested opacity
    
    # Regional range (North Atlantic/Europe): ~-0.5 to -1.0 degC
    # Lighter, wider band showing local impact
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.000725,  # 1300 CE
        x1=0.000175,  # 1850 CE
        y0=-1.0,  # Regional range (wider)
        y1=-0.5,
        fillcolor='rgba(65,105,225,0.15)',  # Light blue
        line=dict(width=0),
        layer="below"
    )
    
    # Global range: ~-0.2 to -0.3 degC
    # Darker, narrower band showing planetary average
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=0.000725,  # 1300 CE
        x1=0.000175,  # 1850 CE
        y0=-0.3,  # Global range (narrower)
        y1=-0.2,
        fillcolor='rgba(65,105,225,0.35)',  # Darker blue
        line=dict(width=0),
        layer="below"
    )    

# K-Pg Extinction
    fig.add_annotation(
#        x=66.0, 
        x=np.log10(66.0),
        y=-8,
        text='K-Pg Extinction<br>(Dinosaurs)',
        showarrow=False, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor='#333',
        ax=0, ay=-40,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,
        hovertext='<b>K-Pg Extinction (66 Million Years Ago)</b><br>'
                  'Asteroid impact in Yucatan Peninsula<br>'
                  'Chicxulub crater: 180 km diameter<br>'
                  '~75% of species extinct (including dinosaurs)<br>'
                  'Impact winter: years of darkness and cold<br>'
                  'Ended Mesozoic Era, began Age of Mammals<br>'
                  'Birds (avian dinosaurs) survived',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # PETM
    fig.add_annotation(
        x=np.log10(56.0),
        y=15.78,
        text='PETM<br>(Thermal Maximum)',
        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor='#333',
        ax=0, 
        ay=-90,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,
        hovertext='<b>PETM - Paleocene-Eocene Thermal Maximum</b><br>'
                  '~56 million years ago<br>'
                  'Rapid warming of ~5-8 degC in <10,000 years<br>'
                  'Massive carbon release (volcanic/methane)<br>'
                  'Ocean acidification, deep-sea extinctions<br>'
                  'Mammals diversified and spread globally<br>'
                  'Closest ancient analog to modern warming',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # Grande Coupure
    fig.add_annotation(
        x=np.log10(34.0),
        y=8.44,
        text='Grande Coupure<br>(Cooling begins)',
        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor='#333',
        ax=40, 
        ay=-40,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,
        hovertext='<b>Grande Coupure - The "Great Cut"</b><br>'
                  '~34 million years ago (Eocene-Oligocene)<br>'
                  'Abrupt cooling, ice sheets form on Antarctica<br>'
                  'Drop of ~4 degC in less than 400,000 years<br>'
                  'Opening of Drake Passage (Antarctica-S.America)<br>'
                  'Circumpolar current isolates Antarctica<br>'
                  'Major faunal turnover in Europe',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # Ice Ages Begin - positioned to align with data
    fig.add_annotation(
        x=np.log10(2.58),  # Use log10 for log-scale x-axis
        y=0.5,  # Adjusted y position to be closer to where data is
        text='Ice Ages Begin',
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor='#333',
        ax=0,
        ay=-40,
        font=dict(size=9, color='#333'),
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='#333',
        borderwidth=1,
        hovertext='<b>Quaternary Ice Age Begins</b><br>'
                  '~2.6 million years ago (Pleistocene)<br>'
                  'Regular glacial-interglacial cycles begin<br>'
                  '41,000-year cycles, then 100,000-year cycles<br>'
                  'Ice sheets cover Northern Hemisphere<br>'
                  'Human ancestors adapt to climate swings<br>'
                  'Still in this ice age today (Holocene = warm phase)',
        hoverlabel=dict(bgcolor='rgba(50,50,50,0.9)', font_size=11)
    )
    
    # ===== DEEP TIME EVENTS (with ? hover for minimal clutter) =====
    
    # Cretaceous Thermal Maximum
    fig.add_annotation(
        x=np.log10(90),
        y=20,
        text='CTM',
        showarrow=False,
        font=dict(size=9, color='#333'),
    #    font=dict(size=16, color='#7FC64E'),  # Cretaceous green
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,    
    #    bgcolor='rgba(255,255,255,0.9)',
    #    bordercolor='#7FC64E',
    #    borderwidth=2,
        borderpad=4,
        hovertext='<b>Cretaceous Thermal Maximum (~90 Ma)</b><br>'
                  'Peak Mesozoic greenhouse conditions<br>'
                  'Global temp ~20 degC above pre-industrial<br>'
                  'High CO2, no polar ice, warm oceans<br>'
                  'Dinosaurs thrived in hot world',
        hoverlabel=dict(bgcolor='rgba(127,198,78,0.9)', font_size=11)
    )
    
    # Permian-Triassic Extinction
    fig.add_annotation(
        x=np.log10(252),
        y=25.5,
        text='P-T Ext.',
        showarrow=False,
        font=dict(size=9, color='#333'),        
    #    font=dict(size=16, color='#F04028'),  # Permian red
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,    
    #    bgcolor='rgba(255,255,255,0.9)',
    #    bordercolor='#F04028',
    #    borderwidth=2,
        borderpad=4,
        hovertext='<b>Permian-Triassic Extinction (~252 Ma)</b><br>'
                  'The "Great Dying" - worst mass extinction<br>'
                  '~96% of marine species extinct<br>'
                  '~70% of terrestrial vertebrates extinct<br>'
                  'Caused by Siberian Traps volcanism<br>'
                  'Massive CO2 release, ocean anoxia<br>'
                  'Global temp ~28 degC (peak hothouse)',
        hoverlabel=dict(bgcolor='rgba(240,64,40,0.9)', font_size=11)
    )
    
    # Carboniferous Icehouse
    fig.add_annotation(
        x=np.log10(300),
        y=-3.5,
        text='Icenhouse',
        showarrow=False,
        font=dict(size=9, color='#333'),        
    #    font=dict(size=16, color='#67A599'),  # Carboniferous teal
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,    
    #    bgcolor='rgba(255,255,255,0.9)',
    #    bordercolor='#67A599',
    #    borderwidth=2,
        borderpad=4,
        hovertext='<b>Carboniferous Icehouse (~300 Ma)</b><br>'
                  'The "Coal Age" - vast tropical forests<br>'
                  'Trees evolved lignin (hard to decompose)<br>'
                  'Massive carbon burial [OK] coal deposits<br>'
                  'Drew down atmospheric CO2<br>'
                  'Triggered glaciation (~12 degC drop)<br>'
                  'First forests changed the planet!',
        hoverlabel=dict(bgcolor='rgba(103,165,153,0.9)', font_size=11)
    )
    
    # Late Ordovician Glaciation
    fig.add_annotation(
        x=np.log10(445),
        y=-8,
        text='Glaciation',
        showarrow=False,
        font=dict(size=9, color='#333'),        
    #    font=dict(size=16, color='#009270'),  # Ordovician green
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,    
    #    bgcolor='rgba(255,255,255,0.9)',
    #    bordercolor='#009270',
    #    borderwidth=2,
        borderpad=4,
        hovertext='<b>Late Ordovician Glaciation (~445 Ma)</b><br>'
                  'First major Phanerozoic icehouse<br>'
                  'Rapid cooling to ~5 degC<br>'
                  'Massive ice sheets on Gondwana<br>'
                  'Sea level drop of ~100m<br>'
                  'End-Ordovician mass extinction<br>'
                  '~85% of marine species extinct',
        hoverlabel=dict(bgcolor='rgba(0,146,112,0.9)', font_size=11)
    )
    
    # End-Triassic Extinction (optional but you said "all"!)
    fig.add_annotation(
        x=np.log10(201),
        y=18,
        text='E-T Ext.',
        showarrow=False,
        font=dict(size=9, color='#333'),        
    #    font=dict(size=16, color='#812B92'),  # Triassic purple
        bgcolor='rgba(255,255,255,0.8)', bordercolor='#333', borderwidth=1,    
    #    bgcolor='rgba(255,255,255,0.9)',
    #    bordercolor='#812B92',
    #    borderwidth=2,
        borderpad=4,
        hovertext='<b>End-Triassic Extinction (~201 Ma)</b><br>'
                  'One of the "Big Five" mass extinctions<br>'
                  '~75% of species extinct<br>'
                  'Caused by CAMP volcanism<br>'
                  '(Central Atlantic Magmatic Province)<br>'
                  'CO2 spike, ocean acidification<br>'
                  'Opened ecological space for dinosaurs',
        hoverlabel=dict(bgcolor='rgba(129,43,146,0.9)', font_size=11)
    )
        

    # Add 3.3 degC
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=3.3,
        x1=0.94,
        y1=3.3,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
    # Add 2.8 degC 
#    fig.add_shape(
#        type="line",
#        xref="paper",
#        yref="y",
#        x0=0.0,
#        y0=2.8,
#        x1=0.94,
#        y1=2.8,
#        line=dict(
#            color="red",
#            width=1,
#            dash="dot"
#        )
#    )

    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.77,
        y=3.40,
        text="Current Policies (UNEP): 2.6 degC - 3.3 degC",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='red'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 2.6 degC 
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=2.6,
        x1=0.94,
        y1=2.6,
        line=dict(
            color="red",
            width=1,
            dash="dot"
        )
    )
    
#    fig.add_annotation(
#        xref="paper",
#        yref="y",
#        x=0.82,
#        y=3.10,
#        text="2.5 degC to 2.9 degC Trajectory",
#        showarrow=False,
#        bgcolor="rgba(255,255,255,0.8)",
#        font=dict(size=9, color='black'),
#        xanchor='left',
#        yanchor='bottom'
#    )

    # Add 1.28 degC current anomaly line - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=1.28,
        x1=0.94,
        y1=1.28,
        line=dict(
            color="green",
            width=1,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=1.40,
        text="1.28 degC -- Current Anomaly",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='green'),
        xanchor='left',
        yanchor='bottom'
    )

    # Add 0 degC baseline - spans both plots
    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=0.0,
        y0=0,
        x1=0.94,
        y1=0,
        line=dict(
            color="black",
            width=1,
            dash="dot"
        )
    )
    
    fig.add_annotation(
        xref="paper",
        yref="y",
        x=0.80,
        y=-1.0,
        text="0 degC -- 1850 - 1900 Baseline",
        showarrow=False,
        bgcolor="rgba(255,255,255,0)",
        font=dict(size=9, color='black'),
        xanchor='left',
        yanchor='bottom'
    )

    info_text = (
        "<b>Earth's Climate History and Human Origins</b><br>"
        "<br>"
        "[EARTH] <b>Phanerozoic:</b> Scotese et al. 2021 (540 Ma); "
        "   <i>Method: Lithologic indicators + delta^18O + models</i><br>"
        "[CLOCK] <b>Paleoclimate:</b> LR04 Benthic Stack (5.3 Ma); "
        "   <i>Method: Benthic foraminifera delta^18O</i><br>"
        "[SNOW] <b>Younger Dryas:</b> Alley (GISP2 ice core, 2000); "
        "   <i>Method: Greenland ice core delta^18O</i><br>"
        "[TEMP] <b>Holocene:</b> Kaufman et al. 2020 (12 ka); "
        "   <i>Method: Multi-proxy (pollen, sediments, biomarkers)</i><br>"
        "[SUN] <b>Modern:</b> NASA GISS (1880-2025); "
        "   <i>Method: Instrumental (thermometers, satellites)</i><br>"
        "* Time Span: 540 Ma to 2100 CE<br>"
        "[CHART] Baseline: Pre-industrial (1850-1900)<br>"
        "<br>"
#        "[INFO] <b>Overlapping curves show method differences</b> "
#        "   Scientific uncertainty is normal and expected!<br>"
#        "<br>"
        "[*] <b>Proxy Handoffs:</b> Each dataset ends where higher-resolution methods begin<br>"
#        "<br>"

#        "* Phanerozoic 'double hump' (540 Ma)<br>"
#        "* Mesozoic greenhouse (252-66 Ma)<br>"
#        "* Ice age cycles (last 2.6 Ma)<br>"
#        "* Holocene stability (last 12,000 years)<br>"
#        "<br>"
        "[*] <b>Key Insight:</b> The Holocene's stable climate "
        "enabled human civilization to flourish.<br>"
        "[ZOOM] <b>Use zoom to explore details!</b>"
    )    

    fig.add_annotation(
        text=info_text,
        xref="paper", yref="paper",
        x=0.50, y=0.95,
        xanchor="left", yanchor="top",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="#2E86AB",
        borderwidth=2,
        borderpad=10,
        showarrow=False,
        font=dict(size=10),
        align="left"
    )
    
    fig.update_xaxes(
        title_text="Millions of Years Before Present (Ma, logarithmic scale)",
        autorange=False,
        range=[np.log10(540), np.log10(0.000001)],  # 540 Ma to ~present
        type="log",
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )   

    fig.update_yaxes(
        title_text="Temperature Anomaly ( degC, relative to present)",
        secondary_y=False,
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )
    
    # Layout
    fig.update_layout(
        title={
            'text': "Earth's Climate History: 540 Million Years to 2100 CE (Phanerozoic Eon)<br><sub>From Cambrian Explosion to Present</sub>",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18}
        },
        hovermode='closest',
        showlegend=True,
        legend=dict(
            x=0.94,
            y=0.00,
            xanchor='right',
            yanchor='bottom',
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#2E86AB',
            borderwidth=2,
            font=dict(size=10)
        ),
        plot_bgcolor='white',
        height=700,
        margin=dict(t=80, b=80, l=80, r=80)
    )
    
    # Add source citation
    fig.add_annotation(
        text="Data: Scotese et al. (2021) Phanerozoic | Lisiecki & Raymo (2005) LR04 | Kaufman et al. (2020) Holocene | Alley (2000) GISP2 Ice Core (YD) | NASA GISS | Paloma's Orrery",
        xref="paper", yref="paper",
        x=0.5, y=-0.10,
        xanchor="center", yanchor="top",
        showarrow=False,
        font=dict(size=9, color='#666')
    )
    
    return fig

def main():
    """Test the visualization"""
    if not PLOTLY_AVAILABLE:
        print("Error: Plotly not available")
        return
    
    print("Creating paleoclimate visualization...")
    fig = create_paleoclimate_visualization()
    
    if fig:
        print("[OK] Visualization created successfully")
        # Offer to save
        save_plot(fig, "paleoclimate_540Ma_to_present")        
        print("Opening in browser...")
        fig.show()
    else:
        print("[FAIL] Could not create visualization - check if data is cached")
        print(f"Expected data file: {LR04_CACHE}")

if __name__ == '__main__':
    main()
