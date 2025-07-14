# Constants Module

# Import necessary libraries

import numpy as np
from datetime import datetime, timedelta

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit
KM_PER_AU = 149597870.7   # Approximate kilometers per Astronomical Unit

# Orbital parameters for planets and dwarf planets
# https://ssd.jpl.nasa.gov/sats/elem/

# Add to constants.py

# International Astronomical Union (IAU) has defined nominal values for planetary radii, 2015.
CENTER_BODY_RADII = {       # km
    'Sun': 696340,      # Solar radius
    'Mercury': 2440,
    'Venus': 6052,
    'Earth': 6371,
    'Moon': 1737,
    'Mars': 3396.2,    # JPL uses an equipotential virtual surface with a mean radius at the equator as the Mars datum. 
    'Jupiter': 71492,   # was 69911
    'Saturn': 58232,
    'Uranus': 25362,
    'Neptune': 24622,
    'Pluto': 1188,
    'Bennu': 0.262,     # Bennu's mean radius
    'Eris/Dysnomia': 1163,
    'Arrokoth': 0.0088,  # Approximate mean radius
    'Planet 9': 24000   # comes from models that assume Planet Nine has a mass around 5-10 Earth masses and an internal composition similar to Uranus and Neptune.
}

"""
parent_planets = {
    'Earth': ['Moon'],
    'Mars': ['Phobos', 'Deimos'],
    'Jupiter': ['Io', 'Europa', 'Ganymede', 'Callisto', 'Metis', 'Adrastea', 'Amalthea', 'Thebe'],
    'Saturn': ['Titan', 'Enceladus', 'Rhea', 'Dione', 'Tethys', 'Mimas', 'Iapetus', 'Phoebe', 'Pan', 'Daphnis', 'Prometheus',
               'Pandora', 'Hyperion'],
    'Uranus': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon', 'Portia', 'Mab'],
    'Neptune': ['Triton', 'Despina', 'Galatea'],
    'Pluto': ['Charon', 'Styx', 'Nix', 'Kerberos', 'Hydra'],
    'Eris/Dysnomia': ['Dysnomia']
}

planet_tilts = {        # degrees
    'Earth': 0,         # 23.44 tilt not needed,  the moon is already defined in the ecliptic frame; using tilt does not align
    'Mars': 25.19,     # 25.19 tilt; neither the positive nor the negative tilt align
    'Jupiter': 3.13,    # tilt aligns well
    'Saturn': -26.73,   # 26.73 tilt; the positive tilt does not align; the negative is much better
    'Uranus': 97.77,   # 97.77 tilt; does not align either positive or negative
    'Neptune': 28.32,   # 28.32; does not align well, but the negative tilt is worse
    'Pluto': -122.53    # 122.53; does not align well, the negative is better
}
"""

# Dictionary of known orbital periods for validation
KNOWN_ORBITAL_PERIODS = {
    # Planets (in Earth years)
    'Mercury': 0.24,    # 87.6 days
    'Venus': 0.62,      # 226.3 days
    'Earth': 1.0,       # 365.25 days
    'Mars': 1.88,       # 686.67 days
    'Jupiter': 11.86,   # 4,330.6 days (11.86 years)
    'Saturn': 29.46,    # 10,755.7 days (29.46 years)
    'Uranus': 84.01,    # 30,684.7 days (84.01 years)
    'Neptune': 164.8,   # 60,193.0 days (164.8 years)
    'Pluto': 248.0,     # 90,582.0 days (248.0 years)
    
    # Major satellites (already in Earth days); https://ssd.jpl.nasa.gov/sats/elem/
    'Moon': 27.32,      # 27.32 days
    'Phobos': 0.32,     # 0.32 days (7.68 hours)
    'Deimos': 1.26,     # 1.26 days (30.24 hours)
    'Io': 1.77,         # 1.77 days (42.48 hours)
    'Europa': 3.55,     # 3.55 days (85.2 hours)
    'Ganymede': 7.15,   # 7.15 days
    'Callisto': 16.69,  # 16.69 days
    'Metis': 0.295,     # 0.295 days (7.08 hours)
    'Adrastea': 0.298,  # 0.298 days (7.15 hours)
    'Amalthea': 0.498,  # 0.498 days (11.95 hours)
    'Thebe': 0.675,      # 0.675 days (16.20 hours)
    'Titan': 15.95,     # 15.95 days
    'Enceladus': 1.37,  # 1.37 days (32.88 hours)
    'Rhea': 4.52,       # 4.52 days
    'Dione': 2.74,      # 2.74 days (65.76 hours)
    'Tethys': 1.89,     # 1.89 days (45.36 hours)
    'Pan': 0.575051,        # https://ssd.jpl.nasa.gov/sats/elem/ and following
    'Daphnis': 0.594080,
    'Prometheus': 0.615878,
    'Pandora': 0.631369,
    'Hyperion': 21.276658,
    'Iapetus': 79.331002,
    'Mimas': 0.94,      # 0.94 days (22.56 hours)
    'Phoebe': 550.56,   # 550.56 days (1.51 years)
    'Miranda': 1.41,    # 1.41 days (33.84 hours)
    'Ariel': 2.52,      # 2.52 days (60.48 hours)
    'Umbriel': 4.14,    # 4.14 days (99.36 hours)
    'Titania': 8.71,    # 8.71 days
    'Oberon': 13.46,    # 13.46 days
    'Portia': 0.513196,
    'Mab': 0.923293,

    'Triton': 5.88,     # 5.88 days (141.12 hours); https://ssd.jpl.nasa.gov/sats/elem/
    'Despina': 0.334656,
    'Galatea': 0.428744,

    'Charon': 6.39,     # 6.39 days; https://ssd.jpl.nasa.gov/sats/elem/
    'Styx': 20.16,     
    'Nix': 24.86,       # 24.86 days
    'Hydra': 38.20,     # 38.20 days
    'Kerberos': 32.17,     
    'Dysnomia': 15.79,  # 15.79 days
    
    # Dwarf planets and KBOs (in Earth years)
    'Ceres': 4.6,       # 1,680.15 days (4.6 years)
    'Eris': 558.0,      # 203,809.50 days (558.0 years)
    'Haumea': 284.0,    # 103,731.00 days (284.0 years)
    'Makemake': 306.0,  # 111,766.50 days (306.0 years)
    'Quaoar': 288.0,    # 105,192.00 days (288.0 years)
    'Sedna': 11400.0,   # 4,163,850.00 days (11,400.0 years)
    'Orcus': 247.0,      # 90,216.75 days (247.0 years)

    # Comets
    'Halley': 76        # Halley's orbital period varies. This is an average
}

# Mapping of SIMBAD object types to full descriptions
object_type_mapping = {
    'Ae*': 'A-type Star with emission lines',
    'AGB*': 'Asymptotic Giant Branch Star',
    'alf2CVnV': 'Variable Star',
    'alf2CVnV*': 'Variable Star',
    'AM*': 'AM Herculis-type Variable Star',
    'BD*': 'Brown Dwarf',

    'Be*': 'Be Star. Spectral type of B. Emission lines in its spectrum<br> ' 
    'indicate the presence of hot, glowing gas around the star.',

    'BlueSG': 'Blue Supergiant Star',
    'BlueSG*': 'Blue Supergiant Star',
    'BlueStraggler': 'Blue Straggler Star',
    'BlueStraggler*': 'Blue Straggler Star',
    'BrownD*': 'Brown Dwarf',
    'BY*': 'BY Draconis-type Variable Star',

    'C*': 'Carbon Star. While they don\'t fit into the main sequence OBAFGKM classification, carbon stars have their own<br>' 
    'distinct spectral characteristics and evolutionary path.<br>' 
    '* Strong carbon absorption lines: Carbon stars are characterized by strong absorption bands of carbon molecules<br>' 
    '  (like C2 and CN) in their spectra. This gives them a distinctly reddish appearance, often described as ruby red or deep orange.<br>' 
    '* More carbon than oxygen: Unlike most stars (like our Sun), where oxygen is more abundant than carbon, carbon stars<br>' 
    '  have an excess of carbon in their atmospheres. This excess carbon forms those characteristic carbon molecules.<br>' 
    '* Asymptotic giant branch (AGB) stars: Most carbon stars are evolved stars on the asymptotic giant branch (AGB). These<br>' 
    '  are stars that have exhausted the hydrogen fuel in their core and have gone through a phase of helium fusion.<br>' 
    '* Dredge-ups: During the AGB phase, these stars experience "dredge-ups" where carbon from the interior is brought to the<br>' 
    '  surface by convection currents. This is what leads to the excess carbon in their atmospheres.<br>' 
    '* Classical carbon stars: These are the most common type, typically red giants on the AGB.<br>' 
    '* Non-classical carbon stars: These are less common and can be found in different evolutionary stages. They may have<br>' 
    '  formed their excess carbon through mass transfer from a binary companion.<br>' 
    '* Stellar evolution: Carbon stars provide valuable insights into the late stages of stellar evolution and the processes<br>' 
    '  that occur in aging stars.<br>' 
    '* Nucleosynthesis: They play a role in the production of heavier elements in the universe, as some of the carbon they produce<br>' 
    '  is eventually ejected into space through stellar winds.<br>' 
    '* Unique appearance: Their deep red color makes them stand out in the night sky.',
          
    'Ce*': 'Classical Cepheid Variable Star',
    'Cepheid': 'Cepheid Variable Star',
    'Cepheid*': 'Cepheid Variable Star',
    'ChemPec*': 'Chemically Peculiar Star',
    'ClassicalCep': 'Classical Cepheid Variable Star',
    'ClassicalCep*': 'Classical Cepheid Variable Star',
    'dS*': 'Delta Scuti-type Variable Star',
    'DQ*': 'Degenerate Star of type DQ',
    'EclBin': 'Eclipsing Binary Star System',
    'EllipVar': 'Ellipsoidal Variable Star',
    'EllipVar*': 'Ellipsoidal Variable Star',
    'EmLine*': 'Emission Lines Star',
    'Eruptive*': 'Eruptive Variable Star',
    'Fl*': 'Flare Star',
    'HB*': 'Horizontal Branch Star',
    'HighMassXBin': 'High-Mass X-ray Binary system',
    'HighPM': 'High Proper-Motion Star',
    'HighPM*': 'High Proper-Motion Star',
    'HorBranch*': 'Horizontal Branch star',
    'Inexistent': 'Inexistent/Non-standard Classification',
    'Infrared': 'Infrared Object',
    'LongPeriodV': 'Variable Star',
    'LongPeriodV*': 'Variable Star',
    'Low-Mass*': 'Low-Mass Star',
    'LowMassXBin': 'Low-Mass X-ray Binary',
    'LP*': 'Long-period Variable Star',

    'MainSequence*': 'A main sequence star is like the "adult" phase in the life of a star.<br> ' 
    'It\'s the stage where a star spends most of its existence, shining steadily and fusing hydrogen<br> ' 
    'into helium in its core.  Our Sun is a perfect example of a main-sequence star. It generates<br> ' 
    'energy through nuclear fusion of hydrogen into helium in its core. This process releases enormous<br> ' 
    'amounts of energy, which powers the star\'s luminosity. The outward pressure from this energy<br> ' 
    'production balances the inward force of gravity, keeping the star stable and in equilibrium. Main<br> ' 
    'sequence stars can have a wide range of masses, from about 0.08 times the mass of the Sun to<br> ' 
    'around 200 times the Sun\'s mass. More massive stars are hotter and bluer, while less massive<br> ' 
    'stars are cooler and redder. More massive stars are much more luminous than less massive stars. <br> ' 
    'Massive stars burn through their fuel quickly and have short lifespans, while low-mass stars<br> ' 
    'can shine for billions or even trillions of years. Main sequence stars make up about 90% of all<br> ' 
    'A main sequence star is a star in its prime, steadily fusing hydrogen and shining brightly.',

    'Mira': 'Mira Variable Star',
    'Mira*': 'Mira Variable Star',
    'N*': 'Nova',
    'No*': 'Nova-like Star',
    'OH/IR*': 'OH/IR star', 
    'PM*': 'High Proper-Motion Star',
    'post-AGB*': 'Post-asymptotic Giant Branch Star',
    'Pulsar': 'Pulsar',
    'RedSG': 'Red Supergiant Star',
    'RedSG*': 'Red Supergiant Star',

    'RGB*': 'Red Giant Branch Star. Low- to intermediate-mass stars, like our Sun.<br> ' 
    'RGB stars have already finished fusing hydrogen into helium in their cores.<br> ' 
    'This marks the end of their main-sequence lifetime. They have a non-fusing)<br> ' 
    'helium core surrounded by a shell where hydrogen fusion continues. When the<br> ' 
    'core hydrogen is depleted, the core contracts and heats up, and the star\'s<br> ' 
    'outer layers expand dramatically. This expansion causes the star\'s surface<br> ' 
    'temperature to cool, radiating a reddish color. The star becomes much more<br> ' 
    'luminous overall due to its increased size. This process moves the star off<br> ' 
    'the main sequence and onto the subgiant branch and then into the red giant<br> ' 
    'Eventually, the core becomes hot and dense enough to ignite helium fusion.<br> ' 
    'This leads to horizontal or the asymptotic giant branch. Ultimately, the<br> ' 
    'star\'s core will become a white dwarf, a small, dense remnant.',

    'RR*': 'RR Lyrae-type Variable Star',
    'RRLyrae_Candidate': 'RR Lyrae-type Variable Star Candidate',
    'RRLyrae_Candidate*': 'RR Lyrae-type Variable Star Candidate',
    'S*': 'Symbiotic Star',
    'SB*': 'Spectroscopic Binary Star. A type of binary star system<br> ' 
    'that can only be identified by analyzing its light spectrum.',
    'SN*': 'Supernova',
    's*r': 'Supergiant Star',
    'Star': 'Star',
    'Supergiant': 'Supergiant Star',
    'Supergiant*': 'Supergiant Star',
    'Symbiotic*': 'Symbiotic Star',
    'TTauri*': 'T Tauri Star',
    'Type2Cep': 'Type II Cepheid variable star',
    'Type2Cep*': 'Type II Cepheid variable star',
    'V*': 'Variable Star',
    'Variable*': 'Variable Star',
    'WD*': 'White Dwarf',
    'WhiteDwarf': 'White Dwarf',
    'WhiteDwarf*': 'White Dwarf',
    'WolfRayet*': 'Wolf-Rayet Star', 
    'WV*': 'Wolf-Rayet Star',
    'XrayBin': 'X-ray Binary System',
    'YellowSG': 'Yellow Supergiant Star',
    'Y*O': 'Young Stellar Object',
    'YSO': 'Young Stellar Object',
    'YSO_Candidate': 'Young Stellar Object Candidate',
    '**': 'Unknown/Unclassified',
    # Add other specific codes observed in data as needed
}

class_mapping = {
            'I': 'Supergiant. The largest and most luminous stars, often nearing the end of their lives.',
            'II': 'Bright giant. Luminous stars that are smaller and less massive than supergiants.',
            'III': 'Giant. Stars that have evolved off the main sequence and expanded significantly.',
            'IV': 'Subgiant. Stars that are transitioning between the main sequence and the giant phase.',
            'V': 'Main-sequence. Stars in the prime of their lives, fusing hydrogen into helium in their cores.',
            'VI': 'Subdwarf. Stars that are smaller and less luminous than main-sequence stars of the same temperature.',
            'VII': 'White dwarf. The small, dense remnants of low- to medium-mass stars after they have exhausted their nuclear fuel.',
        }

# Note in note_frame
note_text = (
    "What's an orrery? \n\n"

    "An orrery is a model of the solar system! This model attempts to display celestial and human objects in both stationary " 
    "and animated 3D plots over different periods of time. It uses real-time data from NASA's Jet Propulsion Laboratory's Horizon System " 
    "to plot actual positions of objects. In addition, complete idealized orbits of the planets, asteroids, dwarf planets, and Kuiper " 
    "belt objects are calculated from their orbital parameters using Kepler's equations. Explore! \n\n" 

    "In addition to the solar system, you can also create 2D and 3D plots of our stellar neighborhood. There are four ways to do this: "
    "by distance in light-years or by brightness as apparent magnitude, and in both modes in a 2D or a 3D plot.\n\n"

    "You can plot our stellar neighborhood up to 100 light-years away in 2D and 3D, with a user defined entry in light-years.\n\n" 

    "The other way of selecting stars is by apparent magnitude. This method also plots 2D or 3D, but the star selection is quite " 
    "different. Instead of seeing all stars within a certain distance from the Sun, you see all stars visible to the unaided eye up " 
    "to a certain apparent, or visual magnitude, meaning how bright they appear, which is a function of how luminous they are and " 
    "their distance from us.\n\n" 
    
    "If you click the \"Move Camera to the Center\" button, the view will move to the position of the Sun.\n\n" 

    "The 3D plot is just that, you will "
    "see stars plotted relative to the Sun in their actual positions, up to the selected distance in light-years, or up to the selected "
    "apparent magnitude, regardless of the distance. In fact, you will begin to see the shape and tilt of the galaxy! You can also " 
    "use a drop down menu of bright stars and Messier Objects that are plotted, which will allow you to point to that object!\n\n"
    
    "You can also see in all plots the hovertext with the stars' information, in some cases in detail as I add it. You can toggle " 
    "between full hovertext information and just the star's name using the buttons, \"Full Star Info\" and \"Star Names Only\".\n\n"  
    
    "The 2D star plot is the classic Hertzprung-Russell diagram of stars plotted by "
    "luminosity, or absolute magnitude, meaning how intrinsically bright the star is, and temperature, which is related to the star's "
    "spectral class and color. This is a more scientific plot that reveals a lot about the "
    "kind of stars they are, and their place in stellar evolution. The 2D plots can be done both by distance and apparent magnitude.\n\n" 

    "More on the magnitude mode: You can select the magnitude "
    "you wish to plot up to apparent magnitude 9, extremely faint stars, which is what you might be able to see from space, down to -1.44, which is the "
    "apparent magnitude of the brightest star in the sky, Sirius, and everything in between as explained in the hovertext.\n\n" 

    "One nice feature of the 3D apparent magnitude plot, is that you can also plot Messier non-stellar objects, such as nebula and " 
    "open clusters! You can also see the stars in their "
    "familiar constellations IF viewed from the Sun's position at the center of the plot. For example, if you use the \"Move Camera to " 
    "Center\" button to move your view to the position of the Sun, and keep the default magnitude of 4 and select the manual scale default setting of "
    "1400 light-years distance, you will see the familiar Orion constellation with M42 the Orion Nebula! You can see other constellations " 
    "as well if you use the menu to select bright stars in a constellation. Hint: try the alpha stars! Experiment!\n\n"
    
    "A crucial difference between the magnitude plot and the distance plot is that some stars that are visible are extremely far away, " 
    "thousands of light-years, yet will still be "
    "visible because of how luminous they are, such as the Blue Supergiants! "
    "On the other hand, nearer, fainter stars, may not be plotted at all, for example White Dwarfs. In fact, the greater the apparent magnitude " 
    "that you select, you will fetch more faint stars, which are farther aways, and you will begin to see the shape and tilt of the " 
    "galaxy! Warning: the higher the apparent magnitude you select, the more stars you will fetch and the longer your plot will take " 
    "to create, up to a minute and a half at apparent magnitude 9, the limit of visibity in space, say from the Space Station.\n\n"

    "If the star 3D or 2D star field gets too crowded and you wish to see more detail, reduce the light-year distance, the apparent "
    "magnitude, or reduce the scale in light-years in the case of 3D apparent magnitude plots.\n\n" 
    
    "In the case of 3D plots, you can also toggle the hovertext from detailed descriptions " 
    "to star name only using the \"Star Names Only\" toggle button.\n\n" 

    "In 3D plots, to see the star field from the view point of the Sun (us!) use the \"Move Camera to Center\" button.\n\n"
    
    "The color scales follow the color of the black body radiation associated with star temperature, in other words, the star\'s " 
    "actual color. The Sun is colored chlorophyll green, to set it apart in the plot and because it represents the Sun\'s life-giving light! " 
    "Plants have evolved to use the most abundant parts of the Sun's visible light spectrum for photosynthesis (red and blue) " 
    "while reflecting the green light.\n\n"

    "Solar System Objects:\nThe Solar sytem object selection menu is scrollable. Select the objects to plot.\n\n"  

    "Data availability is limited for space missions and comets. "
    "Objects will only be plotted on dates the data is available. "
    "For space missions and comets, be careful to enter a start date and number of days, weeks, months or years to plot that are " 
    "within the timeframes of all the objects to plot to avoid plotting errors. "
    "For dates beyond 2199-12-29, the Horizons system does not provide data for most objects. " 
    "Objects like Dwarf Planet Sedna have orbital periods that are thousands of years long so the orbit will only plot partially " 
    "with actual positions. Full ideal orbits estimated from their orbital parameters using Kepler\'s equations are also plotted. " 
    "This is also the case for Dwarf Planet Pluto!\n\n"

    "The Sun is visualized in detail with all its structural sections, core, radiative zone, convective zone and photosphere, "
    "chromosphere, inner corona, outer corona, and solar wind (inner limit, termination shock and heliopause). See the hovertext.\n\n" 
    
    "We also visualize the inner and outer Oort clouds, the inferred source of comets. Manually select the scale "
    "at 100000 AU to see this."

    "This orrery is created using data from the JPL Horizons system (https://ssd.jpl.nasa.gov/horizons/app.html#/) "
    "See the hyperlink on the orrery display. "
    "Ensure you have an active internet connection, as data is fetched in real-time. Be patient when fetching a lot of object positions, " 
    "especially non-animated plots that show actual positions. \n\n"

    "J2000 Ecliptic Coordinate System:\n" 
    "Object positions are fetched from the JPL Horizons system, which by default provides data in the J2000 ecliptic coordinate system. "
    "This is a celestial coordinate system that aligns with the plane of Earth's orbit around the Sun (the ecliptic) and is fixed " 
    "relative to the stars as of the epoch J2000.0 (January 1, 2000).\n\n"

    "Astronomical Units (AU):\n" 
    "The x, y, and z coordinates are measured in Astronomical Units (AU). "
    "One AU is approximately the average distance from the Earth to the Sun, about 149.6 million kilometers or 93 million miles.\n\n" 

    "Explore and enjoy!\n\n"

    "Python programming by Tony Quintanilla with assistance from Claude, ChatGPT and Gemini AI LLMs, January 2025. "
    "Contact info: \"tonyquintanilla@gmail.com\"."
)


# Function to map celestial objects to colors
def color_map(planet):
    colors = {
        'Sun': 'rgb(102, 187, 106)',      # chlorophyll green
    #    'Sun': 'rgb(255, 249, 240)',  # Slightly warm white to represent 6000K at the Sun's surface. The inner corona is 2M K.
        'Mercury': 'rgb(128, 128, 128)',   # Description: Dark Gray reflecting Mercury's rocky and heavily cratered surface.
        'Venus': 'rgb(255, 255, 224)',
        'Earth': 'rgb(0, 102, 204)',
        'Moon': 'rgb(211, 211, 211)',
        'Mars': 'rgb(188, 39, 50)',
        'Phobos': 'rgb(139, 0, 0)',
        'Deimos': 'rgb(105, 105, 105)',
        'Ceres': 'rgb(105, 105, 105)',

        'Jupiter': 'rgb(255, 165, 0)',
        'Io': 'rgb(255, 140, 0)',
        'Europa': 'rgb(173, 216, 230)',
        'Ganymede': 'rgb(150, 75, 0)',
        'Callisto': 'rgb(169, 169, 169)',
        'Metis': 'rgb(180, 120, 100)',    # Reddish-brown
        'Adrastea': 'rgb(190, 150, 130)',  # Light reddish-brown
        'Amalthea': 'rgb(200, 60, 50)',    # Red
        'Thebe': 'rgb(170, 110, 90)',       # Dark reddish-brown

        'Saturn': 'rgb(210, 180, 140)',
        'Titan': 'rgb(255, 215, 0)',
        'Enceladus': 'rgb(192, 192, 192)',
        'Rhea': 'rgb(211, 211, 211)',
        'Dione': 'rgb(255, 182, 193)',
        'Tethys': 'rgb(173, 216, 230)',
        'Mimas': 'rgb(105, 105, 105)',
        'Pan': 'rgb(180, 180, 180)',            # (Light Gray)
        'Daphnis': 'rgb(190, 190, 190)',        # (Slightly lighter gray)
        'Prometheus': 'rgb(170, 170, 170)',     # (Medium Gray)
        'Pandora': 'rgb(185, 185, 185)',        # (Light-Medium Gray)
        'Hyperion': 'rgb(160, 100, 80)',        # (Dark reddish-brown)
        'Iapetus': 'rgb(220, 220, 220)',        # Trailing Hemisphere: (220, 220, 220) (Light Gray/Whitish); 
                                                # Leading Hemisphere (Cassini Regio): (50, 50, 50) (Very dark gray/almost black) 
        'Phoebe': 'cyan',

        'Uranus': 'rgb(173, 216, 230)',
        'Titania': 'rgb(221, 160, 221)',         
        'Oberon': 'rgb(128, 0, 128)',
        'Umbriel': 'rgb(148, 0, 211)',    
        'Ariel': 'rgb(144, 238, 144)',
        'Miranda': 'rgb(0, 128, 0)',
        'Portia': 'rgb(150, 150, 150)',
        'Mab': 'rgb(100, 100, 120)',

        'Neptune': 'rgb(0, 0, 255)',
        'Triton': 'rgb(0, 255, 255)',
        'Despina': 'rgb(175, 175, 175)',
        'Galatea': 'rgb(175, 175, 175)',

        'Pluto': 'rgb(205, 92, 92)',
        'Charon': 'rgb(169, 169, 169)',
        'Styx': 'rgb(180, 180, 180)',
        'Nix': 'rgb(200, 200, 200)',  
        'Kerberos': 'rgb(170, 170, 170)',      
        'Hydra': 'rgb(190, 190, 190)', 

        'Planet 9': 'grey',  # grey

        'Haumea': 'rgb(128, 0, 128)',
        'Makemake': 'rgb(255, 192, 203)',
        'Eris': 'rgb(240, 240, 240)',
        'Voyager 1': 'white',
        'Voyager 2': 'gold',
        'Cassini': 'green',
        'New Horizons': 'cyan',
        'Arrokoth': 'red',
        'Juno': 'cyan',
        'Galileo': 'white',
        'Apollo 11 S-IVB': 'cyan',        
        'Pioneer10': 'red',
        'Pioneer11': 'green',
        'Europa': 'red',
        'OSIRIS': 'cyan',
        'Parker': 'white',
        'JWST': 'gold',
        'Rosetta': 'white',
        'Bepi': 'red',
        'SolO': 'red',
        'Akatsuki': 'cyan',

        'EM-L1': 'cyan',        
        'EM-L2': 'white',
        'EM-L3': 'green',
        'EM-L4': 'gold',
        'EM-L5': 'red',
        'L1': 'cyan',        
        'L2': 'white',
        'L3': 'green',
        'L4': 'gold',
        'L5': 'red',

        'Kamo oalewa': 'cyan',
        '2024 PT5': 'red',
        '2023 JF': 'white',
        '2024 DW': 'gold',        
        '2024 YR4': 'green',

        'Apophis': 'red',
        'Vesta': 'cyan',
        'Bennu': 'white',
        'Lutetia': 'green',
        'Šteins': 'red',  

        'Oumuamua': 'gold',
        '3I/ATLAS': 'gold',
        'Ikeya-Seki': 'green',
        'West': 'red',
        'Halley': 'cyan',
        'Hyakutake': 'white',
        'Hale-Bopp': 'gold',
        'McNaught': 'green',
        'NEOWISE': 'red',
        'C/2025_K1': 'cyan',
        'Tsuchinshan': 'cyan',
        'ATLAS': 'white',
        'Churyumov': 'gold',
        'Borisov': 'red',

        'SOHO': 'white',
        'JamesWebb': 'gold',
        'Ryugu': 'gold',
        'Eros': 'green',
        'Dinkinesh': 'white',
        'Donaldjohanson': 'red',
        'Eurybates': 'green',
        'Patroclus': 'white',
        'Leucus': 'gold',
        'Polymele': 'cyan',
        'Orus': 'pink',
        'Itokawa': 'red',
        'Chang\'e': 'cyan',
        'MarsRover': 'white',
        'DART': 'gold',
        'Lucy': 'green',
        'Gaia': 'red',
        'Hayabusa2': 'cyan',  
        'Quaoar': 'rgb(244, 164, 96)',
        'Dysnomia': 'white',
        'Sedna': 'rgb(135, 206, 235)',
        '2017 OF201': 'rgb(150, 90, 60)',
        'Orcus': 'rgb(0, 100, 0)',
        'Varuna': 'rgb(218, 165, 32)',
        'Ixion': 'rgb(218, 165, 32)',
        'GV9': 'rgb(128, 0, 128)',
        'MS4': 'rgb(255, 0, 0)',  
        'Gonggong': 'red',           
    }
    return colors.get(planet, 'goldenrod')

# Dictionary mapping celestial object names to their descriptions
INFO = {
# Celestial objects
        'Sun': 'The star at the center of our solar system. To display structure and atmosphere select "Solar Shells".\n\n'
        '* Missions:\n' 
        '  * Pioneer 5 (NASA/DOD, 1960): Measured magnetic field phenomena, solar flare particles, and ionization.\n' 
        '  * Helios 1 & 2 (DFVLR/NASA, 1974 & 1976): Studied solar wind, magnetic and electric fields, cosmic rays, and dust.\n' 
        '  * ISEE-3 (NASA, 1978): Observed solar phenomena in conjunction with Earth-orbiting satellites, comets.\n' 
        '  * Ulysses (ESA/NASA, 1990-2009): Observed the Sun\'s polar regions and the solar wind at high solar latitudes.\n' 
        '  * WIND (NASA, 1994-Present): Still active, it provides continuous measurements of the solar wind.\n' 
        '  * SOHO (Solar and Heliospheric Observatory) (ESA/NASA, 1995-Present): A continuous view from its core to the solar wind.\n' 
        '  * ACE (Advanced Composition Explorer) (NASA, 1997-Present): Measures particles from the solar wind and galactic cosmic rays.\n' 
        '  * Hinode (JAXA/NASA/ESA/STFC, 2006-Present): Explores the Sun\'s magnetic fields.\n' 
        '  * STEREO (Solar TErrestrial RElations Observatory) (NASA, 2006-Present): Imaging the 3D structure of coronal mass ejections.\n' 
        '  * Solar Dynamics Observatory (SDO) (NASA, 2010-Present): High-resolution images of solar flares and eruptions.\n' 
        '  * IRIS (Interface Region Imaging Spectrograph) (NASA, 2013-Present): Sun\'s lower atmosphere (chromosphere and transition).\n' 
        '  * Parker Solar Probe (NASA, 2018-Present): Flew through the corona to study coronal heating and solar wind acceleration.\n' 
        '  * Solar Orbiter (ESA/NASA, 2020-Present): Provides unprecedented insight into how our local star "works" with 10 science instruments.\n' 
        '  * PUNCH (Polarimeter to Unify the Corona and Heliosphere) (NASA, Launched March 2025): Will study the Sun\'s outer atmosphere.\n' 
        '  * Solar Polar Orbit Observatory (Planned 2029): Will study views of its polar regions.',

        'Solar Shells': 'Solar structure and atmosphere, Oort cloud, and gravitational reach.',

        'Mercury': 'The smallest planet and closest to the Sun.\n' 
        '* Mercury-centered: do not select Mercury; visualize shells at manual scale 0.002 AU.\n' 
        '* Heliocentric: select Mercury with or without shells.\n' 
        '* Missions: Mariner 10, Messenger, BepiColombo',

        'Venus': 'Second planet from the Sun, known for its thick atmosphere.\n' 
        '* Venus-centered: do not select Venus; visualize shells at 0.01 AU.\n'
        '* Heliocentric: select Venus with or without shells.\n'  
        '* Missions: Venera (USSR); Mariner 2, 5, 10; Pioneer Venus Project, Vega (USSR), Magellan, Galileo, Cassini-Huygens,\n' 
        '  Venus Express, MESSENGER, Akatsuki, Parker Solar Probe, BepiColombo, DAVINCI, VERITAS, EnVision, Shukrayaan-1, Solar Orbiter.',

        'Earth': 'Our home planet, the third from the Sun.\n' 
        '* Earth-centered: do not select Earth; visualize shells at 0.02 AU.\n'
        '* Heliocentric: select Earth with or without shells.\n'
        '* Missions: Galileo, Cassini-Huygens, Rosetta, New Horizons, JUNO, Parker Solar Probe, Deep Impact, NEAR Shoemaker, Solar Orbiter.',

        'Moon': 'Earth\'s only natural satellite. The Moon\'s orbit is actually inclined by about 5.145° to the ecliptic plane, ' 
        'but approximately 28.545° to Earth\'s equatorial plane (this variation comes from Earth\'s own axial tilt of 23.4°). '
        'The Moon\'s orbital parameters are not fixed but vary significantly over time due to precession of the nodes, ' 
        'perturbations from the Sun\'s gravity, Earth\'s non-spherical shape, and other gravitational influences.\n\n' 
        'Missions: Early Pioneers (1950s-1960s):\n' 
        '* Luna Programme (USSR): This Soviet program launched many "Luna" probes, achieving significant firsts (1959 - 1966).\n' 
        '* Pioneer Program (USA): Early American attempts at lunar exploration. Pioneer 4 (1959) successfully performed a lunar flyby.\n' 
        '* Ranger Program (USA): A series of American impactor missions designed to take close-up images of the Moon before crashing into its surface (1961 - 1965).\n' 
        '* Surveyor Program (USA): American robotic landers that demonstrated the technology for soft landings, crucial for the Apollo program (1966 - 1968).\n' 
        '* Lunar Orbiter Program (USA): American orbiters that mapped the lunar surface in preparation for Apollo landings (1966 - 1967).\n' 
        '* The Apollo Era (1960s-1970s): NASA\'s iconic human spaceflight program that successfully landed humans on the Moon.n' 
        '  * Apollo 8 (1968): First crewed mission to orbit the Moon.\n' 
        '  * Apollo 11 (1969): Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon.\n' 
        '  * Five subsequent Apollo missions (Apollo 12, 14, 15, 16, 17) also landed astronauts on the Moon; Apollo 17, departing in December 1972.\n' 
        '* Renewed Robotic Exploration (1990s-Present): International Efforts.\n' 
        '  * Hiten (Japan, 1990): Japan\'s first lunar mission.\n' 
        '  * Clementine (USA, 1994): Orbiter that produced a detailed map of the lunar surface.\n' 
        '  * Lunar Prospector (USA, 1998): Orbiter that found evidence of water ice at the lunar poles.\n' 
        '  * SMART-1 (ESA, 2003): European Space Agency\'s first lunar mission, testing new propulsion technology.\n' 
        '  * Kaguya (SELENE) (Japan, 2007): Comprehensive lunar orbiter for scientific studies.\n' 
        '  * Chang\'e Program (China): China\'s ambitious lunar exploration program (2007 - 2024).\n' 
        '  * Chandrayaan Program (India): India\'s lunar program (2008 - 2023).\n' 
        '  * Lunar Reconnaissance Orbiter (LRO) (USA, 2009): NASA orbiter continuously mapping the Moon in high detail.\n' 
        '  * LCROSS (USA, 2009): Impact mission to search for water ice at the lunar poles.\n' 
        '  * GRAIL (USA, 2011): Twin spacecraft that precisely measured the Moon\'s gravity field.\n' 
        '  * LADEE (USA, 2013): Studied the lunar exosphere and dust.\n' 
        '  * CAPSTONE (USA, 2022): Tested a unique elliptical lunar orbit for future missions like the Gateway.\n' 
        '  * Commercial Lunar Payload Services (CLPS) (USA): NASA program funding private companies for lunar deliveries.\n' 
        '  * Luna 25 (Russia, 2023): Russia\'s first lunar landing attempt since 1976.\n' 
        '  * SLIM (Japan, 2024): Japan\'s successful, though sideways, lunar lander.\n' 
        '  * Queqiao-2 (China, 2024): A lunar communications relay satellite for far side missions.\n'
        '* Future Missions (Ongoing and Planned):\n' 
        '  * Artemis Program (USA): NASA\'s program to return humans to the Moon, aiming for a sustained human presence.\n' 
        '  * Luna 26, 27, 28 (Russia): Planned future Russian lunar missions.\n' 
        '  * Beresheet2 (Israel): Planned private lunar mission.\n' 
        '  * Lunar Gateway: A planned international space station in lunar orbit, supporting future human missions.',

        'Kamo oalewa': 'Asteroid Kamo\'oalewa (469219 / 2016 HO3) is a near-Earth asteroid that has garnered significant scientific interest.\n' 
        '* Classification and Orbit: Kamo\'oalewa is a very small, elongated asteroid belonging to the Apollo group of near-Earth objects. \n' 
        '  What makes it particularly unique is its status as Earth\'s best and most stable "quasi-satellite." This means it orbits the \n' 
        '  Sun with parameters very similar to Earth\'s, appearing to "dance" around our planet in a looping, oscillating path. While it\'s \n' 
        '  too distant to be gravitationally bound like a true moon, it remains relatively close to Earth, between 38 and 100 times the \n' 
        '  distance of the Moon. Its orbit is relatively stable and is expected to remain in this configuration for hundreds of thousands of years.\n' 
        '* Physical Characteristics: Kamo\'oalewa is estimated to be between 40-100 meters in diameter, making it one of the smallest \n' 
        '  asteroids ever targeted for a mission. It\'s also a fast rotator, completing a rotation in approximately 28 minutes.\n' 
        '* Mysterious Origin: One of the most intriguing aspects of Kamo\'oalewa is its potential origin. Research suggests that its \n' 
        '  reflected light spectrum matches lunar rocks from NASA\'s Apollo missions. This has led to the hypothesis that Kamo\'oalewa \n' 
        '  might be a fragment of our own Moon, ejected by an ancient impact. Confirmation of this theory through sample analysis would be \n' 
        '  groundbreaking, as no other known asteroid has been definitively linked to lunar origins.\n' 
        '* Tianwen-2 Mission: Tianwen-2 is China\'s ambitious deep space mission designed to explore asteroid Kamo\'oalewa and a main-belt \n' 
        '  comet. The Tianwen-2 mission launched on May 28, 2025. The mission\'s initial target is Kamo\'oalewa. Tianwen-2 will rendezvous \n' 
        '  with the asteroid in mid-2026 and spend about nine months in its vicinity. It aims to collect approximately 100 grams of \n' 
        '  regolith (surface material) using both "touch-and-go" and "anchor-and-attach" methods. The "anchor-and-attach" method would be \n' 
        '  a first for asteroid sampling. The collected samples are planned to be returned to Earth in November 2027. Analyzing these \n' 
        '  samples will be crucial in determining Kamo\'oalewa\'s true origin (e.g., lunar fragment or main-belt asteroid) and providing \n' 
        '  insights into the early solar system',

        '2024 PT5': 'In late September 2024, Earth temporarily captured a small asteroid into its orbit, leading to it being ' 
        'dubbed Earth\'s "second moon". The object\'s official designation is 2024 PT5, but it was also referred to as a ' 
        '"mini-moon" due to its small size. \n* Size: It\'s estimated to be only about 11 meters wide, making it incredibly ' 
        'small compared to our permanent Moon.\n* Origin: It belongs to the Arjuna asteroid belt, a group of asteroids that ' 
        'share similar orbits with Earth.\n* Closest approach August 9, 2024. \n* Temporary Capture: 2024 PT5 was only temporarily ' 
        'captured by Earth\'s gravity. ' 
        'It entered our orbit on September 29, 2024, and is expected to depart on November 25, 2024.\n* Visibility: Due to its ' 
        'small size, it\'s not visible to the naked eye and requires powerful telescopes to be observed.\n* While 2024 PT5 is ' 
        'not a permanent addition to our celestial neighborhood, its temporary presence provided scientists with a valuable ' 
        'opportunity to study near-Earth objects and learn more about the dynamics of our solar system.\n* Plot 2024 PT5 with' 
        'Earth as the center to see its close approach and also with the Sun as the center to see its orbit near Earth\'s.',

        '2023 JF': 'Asteroid 2023 JF is a small near-Earth asteroid that made a close approach to Earth in May 2023. Here\'s a \n' 
        'breakdown:\n' 
        '* Size: It\'s estimated to be about 34 feet (10 meters) wide, roughly the size of a bus.\n' 
        '* Classification: It\'s classified as a "Near Earth Asteroid" due to its orbit\'s proximity to Earth.\n' 
        '* Close Approach to Earth and Moon:\n' 
        '* Date of Close Approach: Asteroid 2023 JF flew past Earth on May 9, 2023 23:41.\n' 
        '* Distance: At its closest, it was approximately 320,322 km away from Earth. This distance is closer than \n' 
        '  the Moon\'s average orbit around Earth, which is about 384,400 km).\n' 
        '  * Its closest approach to the Moon occurred on May 10, 2023 05:10 at a distance of 192,092 km.\n' 
        '* Significance: While it came closer than the Moon, it passed at a safe distance and posed no risk of impact. These close \n' 
        '  approaches by small asteroids are not uncommon. Astronomers use such events to study asteroids and practice planetary \n' 
        '  defense measures. Even if an asteroid of this size were to enter Earth\'s atmosphere, it would largely disintegrate, with \n' 
        '  some smaller fragments potentially falling as meteorites.\n\n' 
        'It\'s important to distinguish 2023 JF from other similarly named asteroids that also made close approaches in 2023 or 2024, \n' 
        'such as 2023 DZ2 (which passed at about half the Earth-Moon distance) or 2024 JF (which was expected to pass in May 2024). NASA \n' 
        'and other space agencies continuously monitor Near-Earth Objects (NEOs) to track their movements and assess any potential impact \n' 
        'risks.',

        '2024 YR4': '2024 YR4 is an asteroid that poses a potential risk to Earth, with a probability of nearly zero.\n' 
        '* It was discovered on December 27, 2024, with a close approach on December 25, 4:46 UTC at a distance of about 822,000 km.\n' 
        '* It is estimated to be between 40 and 100 meters wide.\n' 
        '* It\'s next close approach is on December 17, 2028, 12:16 UTC at a distance from Earth\'s surface of about 8,007,000 km, ' 
        'according to JPL Horizons.\n'
        '* As of June 3, 2025, YR4 is predicted to make its closest approach to Earth on December 22, 2032, 8:36 UTC. ' 
        'JPL Horizons estimates a closest approach of about 260,487 km from Earth\'s surface. ' 
        'And its closest approach to the Moon on December 22, 2032 at 15:10 UTC of about 8,945 km from the surface.\n'
        '* NASA 2-24-25: "NASA has significantly lowered the risk of near-Earth asteroid 2024 YR4 as an impact threat to Earth for ' 
        'the foreseeable future. When first discovered, asteroid 2024 YR4 had a very small, but notable chance of impacting our ' 
        'planet in 2032. As observations of the asteroid continued to be submitted to the Minor Planet Center, experts at NASA ' 
        'Jet Propulsion Laboratory\’s (JPL\’s) Center for Near-Earth Object Studies were able to calculate more precise models ' 
        'of the asteroid\’s trajectory and now have updated its impact probability on Dec. 22, 2032 to only 0.004% and found there ' 
        'is no significant potential for this asteroid to impact our planet for the next century. The latest observations have ' 
        'further reduced the uncertainty of its future trajectory, and the range of possible locations the asteroid could be on ' 
        'Dec. 22, 2032, has moved farther away from the Earth. There still remains a very small chance for asteroid 2024 YR4 to ' 
        'impact the Moon on Dec. 22, 2032. That probability is currently 1.7%."',

        '2024 DW': 'Close Flyby: Asteroid 2024 DW made a close approach to Earth on February 22, 2024. It passed within approximately ' 
        '225,000 kilometers of Earth, which is closer than the Moon\'s average distance.\n' 
        '* Size: It\'s estimated to be about the size of a bus, roughly 13 meters in diameter.\n' 
        '* Safety: Despite its close proximity, it was determined that 2024 DW did not pose a threat to Earth.\n' 
        '* Discovery: The asteroid was discovered by astronomers working with the Mt. Lemmon Survey.\n' 
        '* Orbit: It is an Apollo type asteroid. Meaning its orbit crosses earth\'s orbit.\n' 
        '* Tracking: NASA\'s Center for Near-Earth Object Studies (CNEOS) played a crucial role in tracking and calculating its orbit. ' 
        'In essence, 2024 DW was a relatively small asteroid that had a close encounter with Earth, providing astronomers with an ' 
        'opportunity to study near-Earth objects.',

        'EM-L1': 'From JPL Horizons ephemeris:  Revised: Jul 11, 2019; EM-L1; 3011; Earth-Moon Lagrange 1\n' 
        '#1) The Earth-Moon Lagrange-1 point (EM-L1) is an equilibirium location where the Moon\'s gravitational field partially \n' 
        '    counters that of the Earth.\n' 
        '#2) This point is between the Earth and Moon, about 84.907% of the distance from the Earth\'s center in the direction of \n' 
        '    the Moon\'s center (303000 to 345000 km from Earth, averaging ~327000 km), or 15.093% from the Moon in the direction \n' 
        '    of the Earth (53800 to 61400 km from Moon, averaging ~58100 km).\n' 
        '#3) EM-L1 is an unstable equilibrium point. This means an object at that location will remain there unless disturbed, \n' 
        '    whereupon it will move away.  In practice, there will always be some disturbance.',

        'EM-L2': 'From JPL Horizons ephemeris:  Revised: Jul 11, 2019; EM-L2; 3012; Earth-Moon Lagrange 2\n' 
        '#1) The Earth-Moon Lagrange-2 point (EM-L2) is an equilibirium location where the Moon\'s gravitational field partially \n' 
        '    counters that of the Earth.\n' 
        '#2) This point is past the Moon on the Earth-Moon line, about 116.783% of the EM distance (416300 to 475000 km from Earth \n' 
        '    center, averaging ~449600 km), or 16.783% of the EM distance from the Moon, in the direction away from the Earth \n' 
        '    (59800 to 68300 km from Moon center, averaging ~64600 km).\n' 
        '#3) EM-L2 is an unstable equilibrium point. This means an object at that location will remain there unless disturbed, \n' 
        '    whereupon it will move away.  In practice, there will always be some disturbance.', 

        'EM-L3': 'From JPL Horizons ephemeris:  Revised: Jul 11, 2019; EM-L3; 3013; Earth-Moon Lagrange 3\n' 
        '#1) The Earth-Moon Lagrange-3 point (EM-L3) is an equilibirium location where the Moon\'s gravitational field partially \n' 
        '    counters that of the Earth.\n'  
        '#3) EM-L3 is an unstable equilibrium point. This means an object at that location will remain there unless disturbed, \n' 
        '    whereupon it will move away.  In practice, there will always be some disturbance.', 

        'EM-L4': 'From JPL Horizons ephemeris:  Revised: Jul 11, 2019; EM-L4; 3014; Earth-Moon Lagrange 4\n' 
        '#1) The Earth-Moon Lagrange-4 point (EM-L4) is a location where the Moon\'s gravitational field partially counters that of \n' 
        '    the Earth. EM-L4 is one of the stable "Trojan" points (along with EM-L5). Small perturbations can displace an object \n' 
        '    from EM-L4, but it can return to the stable point.\n' 
        '#2) EM-L4 lies 60 degrees ahead of the Earth-Moon system along the Moon\'s orbit in plane of the orbit. It is about 1 lunar \n' 
        '    distance from the Earth and from the Moon (straight-lines), so 356000 to 407000 km, averaging 385000 km from Earth and \n' 
        '    Moon centers, forming the apex of an equilateral triangle, with the Earth and Moon defining the base-line.',

        'EM-L5': 'From JPL Horizons ephemeris:  Revised: Jul 11, 2019; EM-L5; 3014; Earth-Moon Lagrange 5\n' 
        '#1) The Earth-Moon Lagrange-5 point (EM-L5) is a location where the Moon\'s gravitational field partially counters that of \n' 
        '    the Earth. EM-L5 is one of the stable "Trojan" points (along with EM-L4). Small perturbations can displace an object \n' 
        '    from EM-L4, but it can return to the stable point.\n' 
        '#2) EM-L5 lies 60 degrees behind the Earth-Moon system along the Moon\'s orbit in plane of the orbit. It is about 1 lunar \n' 
        '    distance from the Earth and from the Moon (straight-lines), so 356000 to 407000 km, averaging 385000 km from Earth and \n' 
        '    Moon centers, forming the apex of an equilateral triangle, with the Earth and Moon defining the base-line.',

        'L1': 'From JPL Horizons ephemeris: Revised: Aug 29, 2013; SEMB-L1; 31; Sun & Earth-Moon Barycenter Lagrange 1\n' 
        '#1) The Sun & Earth-Moon Barycenter Lagrange-1 point (SEMB-L1) is a location where the Earth\'s gravitational field partially \n' 
        '    counters that of the Sun.\n' 
        '#2) This L1 point is about 1.5 million km (~900,000 miles) away from the Earth in the direction of the Sun, or slightly less than \n' 
        '    one percent of the way to the Sun (four times the distance from Earth to the Moon)\n' 
        '#3) The solar wind reaches L1 about an hour before it reaches Earth, making it a good place to observe changes in solar activity \n' 
        '    before the change propagates to the Earth. L1 provides an uninterrupted view of the Sun, being between the Earth and Sun.\n' 
        '#4) L1 is an unstable equilibrium point. This means an object at that location will remain there unless disturbed, whereupon it \n' 
        '    will move away. In practice, there will always be some disturbance. Further, since the Sun is a radio source, communications \n' 
        '    with spacecraft at L1 are difficult to pick out against the background noise. Thus, spacecraft such as Genesis, WIND, SOHO, \n' 
        '    and ACE are placed in "halo" orbits around the L1 point. SMART-1 flew through L1 prior to lunar impact.\n' 
        '* SEMB-L1 and SEMB-L2 will generally track along the Earth-Moon Barycenter\'s orbit, staying on the line between the Sun and the EMB.\n' 
        '* For the unstable L1, L2, L3 points, they are more like moving "targets" that a spacecraft must constantly adjust to stay near.', 

        'L2': 'Sun-Earth-Moon Barycenter Lagrange point 2. From JPL Horizons:\n' 
        '#1) The Sun & Earth-Moon Barycenter Lagrange-2 (L2) point is a location where the Earth\'s gravitational field partially \n' 
        '    counters that of the Sun.\n' 
        '#2) This L2 point is about 1.5 million km (~900,000 miles) away from the Earth, opposite the direction of the Sun, or slightly \n' 
        '    less than one percent of the Earth-Sun distance (four times the distance from Earth to the Moon)\n' 
        '#3) L2 has been selected as the location of the next generation James Webb Space Telescope, was used by the Genesis spacecraft \n' 
        '    on the return to Earth, and is (or will be) used for WMAP, Herschel, and Planck spacecraft.\n' 
        '* SEMB-L1 and SEMB-L2 will generally track along the Earth-Moon Barycenter\'s orbit, staying on the line between the Sun and the EMB.\n' 
        '* For the unstable L1, L2, L3 points, they are more like moving "targets" that a spacecraft must constantly adjust to stay near.', 

        'L3': 'Sun-Earth-Moon Barycenter Lagrange point 3. From JPL Horizons: The Sun & Earth-Moon Barycenter Lagrange-2 (L3) point is \n' 
        'a location where the Earth\'s gravitational field partially counters that of the Sun.\n' 
        '* Here\'s why you\'re observing that irregular motion for SEMB-L3, while the others (especially L4 and L5) appear to trace a \n' 
        '  more circular path:\n' 
        '  * L3\'s Unstable and Collinear Nature: L3, like L1 and L2, lies along the line connecting the two primary bodies (Sun and Earth-Moon Barycenter in \n' 
        '      this case). These collinear points are inherently unstable equilibrium points. Any slight perturbation (and there are \n' 
        '      many in the real solar system, from other planets, the Moon\'s wobble, solar wind pressure, etc.) will cause a body at \n' 
        '      L3 to drift away from the exact point.\n' 
        '  * "Hidden" from View: SEMB-L3 is on the opposite side of the Sun from the Earth. It\'s essentially orbiting the Sun at approximately the same \n' 
        '      distance as Earth, but 180 degrees out of phase.\n' 
        '  * The Dominant Influence of the Sun: The Sun\'s gravity is overwhelming. L3 is essentially a point that "tries" to stay at the same solar orbital distance as \n' 
        '      Earth, but because it\'s behind the Sun, the gravitational pull from the Earth (and Moon) is very subtle and often \n' 
        '      insufficient to perfectly hold it in a perfectly symmetric orbit around the Sun.\n' 
        '  * Perturbations from Other Planets: While L1, L2, L4, and L5 also experience perturbations, L3 is particularly sensitive. The gravitational tugs from Venus, \n' 
        '      Jupiter, and other planets, even though small, can have a noticeable effect on the precise location of the unstable L3 \n' 
        '      point. These perturbations will cause L3\'s ideal position to constantly shift slightly, resulting in an "irregular" or \n' 
        '      "wobbly" path when observed over time.\n' 
        '  * Influence of the Moon\'s Orbit: Even though we use the Earth-Moon Barycenter (EMB) as the secondary body for SEMB-L* calculations, the Moon\'s actual \n' 
        '      orbit around the Earth means that the "effective" secondary mass is constantly shifting slightly relative to the ideal \n' 
        '      EMB point. This introduces a small, but continuous, perturbation on all the SEMB-L* points, which is more noticeable for \n' 
        '      the unstable ones like L3.\n' 
        '  *Reference Frame and "Ideal" Orbit: When you plot the L-points, you\'re usually plotting their positions in an inertial frame (like the Solar System Barycenter \n' 
        '      frame). In this frame: SEMB-L1 and SEMB-L2 will generally track along the Earth-Moon Barycenter\'s orbit, staying on the \n' 
        '      line between the Sun and the EMB. SEMB-L4 and SEMB-L5 are the stable points. In an idealized circular restricted three-body \n' 
        '      problem, they would form equilateral triangles with the two primaries and trace the same perfect circular orbit as the \n' 
        '      secondary. In reality, they also exhibit small, stable librations (oscillations) around the ideal points, but their overall \n' 
        '      path will closely follow the EMB\'s orbit. SEMB-L3\'s instability means it doesn\'t settle into such a neat pattern of \n' 
        '      librations. Its position is constantly being nudged away from the ideal, resulting in a more complex, non-circular trajectory \n' 
        '      that reflects these ongoing instabilities and perturbations. In essence, L3 is highly sensitive to the "messiness" of the real \n' 
        '      solar system. While the mathematical definition of L3 exists, its physical location is constantly being pulled and pushed by \n' 
        '      various gravitational forces, leading to the irregular path you observed. It\'s a fantastic demonstration of the difference \n' 
        '      between idealized mathematical models and the complex reality of celestial mechanics!',

        'L4': 'From JPL Horizons: Revised: Aug 29, 2013; SEMB-L4; 34; Sun & Earth-Moon Barycenter Lagrange 4\n' 
        '#1) The Sun & Earth-Moon Barycenter Lagrange-4 (SEMB-L4) point is a location where the Earth\'s gravitational field partially \n' 
        '    counters that of the Sun.  L4 is one of the stable "Trojan" points (along with L5). Small perturbations can displace an \n' 
        '    object from L4, but it can return to the stable point.\n' 
        '#2) L4 lies 60 degrees ahead of the Earth-Moon system along the heliocentric orbit in plane of the orbit. It is about 1 au \n' 
        '    distant from the Earth (straight-line), forming the apex of an equilateral triangle, with the Sun and Earth-Moon barycenter \n' 
        '    defining the base-line.\n' 
        '#3) The STEREO-A spacecraft passes through L4.\n' 
        '* SEMB-L4 and SEMB-L5 are the stable points. In an idealized circular restricted three-body problem, they would form \n' 
        '  equilateral triangles with the two primaries and trace the same perfect circular orbit as the secondary. In reality, they \n' 
        '  also exhibit small, stable librations (oscillations) around the ideal points, but their overall path will closely follow \n' 
        '  the EMB\'s orbit.',  

        'L5': 'From JPL Horizons:  Revised: Aug 29, 2013; SEMB-L5; 35; Sun & Earth-Moon Barycenter Lagrange 5\n' 
        '#1) The Sun & Earth-Moon Barycenter Lagrange-5 (SEMB-L5) point is a location where the Earth\'s gravitational field partially \n' 
        '    counters that of the Sun. L5 is one of the stable "Trojan" points (along with L4). Small perturbations will displace an \n' 
        '    object from L5, but the object can return to the stable point.\n' 
        '#2) L5 lies 60 degrees behind the Earth-Moon system along the heliocentric orbit and in the plane of the orbit. It is about \n' 
        '    1 AU distant from the Earth (straight-line), forming the apex of an equilateral triangle, with the Sun and Earth-Moon \n' 
        '    barycenter defining the base-line.\n' 
        '#3) The STEREO-B spacecraft passes through L5.\n' 
        '* SEMB-L4 and SEMB-L5 are the stable points. In an idealized circular restricted three-body problem, they would form \n' 
        '  equilateral triangles with the two primaries and trace the same perfect circular orbit as the secondary. In reality, they \n' 
        '  also exhibit small, stable librations (oscillations) around the ideal points, but their overall path will closely follow \n' 
        '  the EMB\'s orbit.',        

        'Mars': 'Known as the Red Planet, fourth planet from the Sun.\n' 
        '* Mars-centered: do not select Mars; visualize shells at 0.01 AU.\n' 
        '* Heliocentric: select Mars with or without shells.\n'
        '* Missions: Mariner 4, 6, 7, 9; Mars 2, 3, 4, 6 and 7 (USSR); Viking 1 and 2; Mars Global Surveyor; 2001 Mars Odyssey;\n' 
        '  Mars Express; Mars Reconnaissance Orbiter; Mars Orbiter Mission; MAVEN; ExoMars Trace Gas Orbiter; Hope Mars Mission (UAE);\n' 
        '  Tianwen-1 Orbiter (China); Mars Pathfinder & Sojourner Rover; Spirit & Opportunity Rovers; Phoenix Lander; Curiosity Rover;\n' 
        '  InSight Lander; Perseverance Rover & Ingenuity Helicopter; Tianwen-1 Lander & Zhurong Rover (China).',

        'Phobos': 'The larger and closer of Mars\'s two moons, spiraling inward towards Mars.',
        'Deimos': 'The smaller and more distant moon of Mars, with a stable orbit. Retrogade orbit.',
        'Ceres': 'The largest object in the asteroid belt, considered a dwarf planet.',

        'Apophis': 'Near-Earth asteroid with a close approach in 2029.\n\n' 
        '* Missions:\n' 
        '  * OSIRIS-APEX (Origins, Spectral Interpretation, Resource Identification, and Security – Apophis EXplorer) - NASA:\n' 
        '    Scheduled to rendezvous with Apophis shortly after its 2029 Earth close-approach.\n' 
        '  * RAMSES (Rapid Apophis Mission for Space Safety) - ESA (European Space Agency): RAMSES to launch in April 2028 and arrive \n' 
        '    at Apophis in February 2029, giving it two months to study the asteroid before its close encounter with Earth.',

        'Vesta': 'Asteroid visited by NASA\'s Dawn mission.',

        'Bennu': 'A near-Earth asteroid studied by the OSIRIS-REx mission.\n' 
        '* Type: Bennu is a near-Earth asteroid classified as a carbonaceous (C-type) asteroid. These types of asteroids are rich in ' 
        'carbon and other organic molecules, as well as hydrated minerals. They are considered to be some of the most primitive ' 
        'objects in the solar system, essentially time capsules from the early days of our planetary system\'s formation.\n' 
        '* Size: Bennu is relatively small, with an equatorial diameter of about 510 meters. It\'s shaped somewhat like a spinning ' 
        'top or a lumpy potato.\n' 
        '* Rotation: Bennu rotates fairly quickly, completing a rotation every 4.3 hours.\n' 
        '* Orbit: Bennu\'s orbit brings it relatively close to Earth, making it accessible for a spacecraft mission. However, its orbit also crosses Earth\'s.\n' 
        '* Scientific Value: Carbonaceous asteroids like Bennu are believed to contain the building blocks of life - organic molecules, ' 
        'amino acids, and potentially even more complex compounds. Studying these materials can give us insights into the early solar ' 
        'system and the origins of life itself. Bennu is a pristine sample of this material.\n' 
        '* Accessibility: Bennu\'s near-Earth orbit made it a logistically feasible target for the OSIRIS-REx mission. The round trip was ' 
        'possible within a reasonable timeframe.\n' 
        '* Sample Return: The primary goal of OSIRIS-REx was to collect a sample of material from Bennu and return it to Earth. Bennu\'s ' 
        'size, composition, and relatively slow rotation made it a good candidate for a touch-and-go sample collection maneuver.\n' 
        'Planetary Defense: Studying Bennu also provides valuable information for planetary defense. Because it\'s a near-Earth asteroid, ' 
        'understanding its composition, structure, and orbit helps us better assess the potential threat of asteroid impacts and develop' 
        'mitigation strategies if necessary.\n' 
        '* Understanding Asteroids: Bennu is representative of a large population of C-type asteroids. Studying it in detail helps us ' 
        'understand the properties of these types of asteroids in general, which is important for understanding the history of the solar ' 
        'system.', 

        'Šteins': 'A main-belt asteroid visited by the Rosetta spacecraft.', 

        'Lutetia': 'A main-belt asteroid visited by the Rosetta spacecraft.', 

        'Ryugu': 'Asteroid visited by the Japanese Hayabusa2 mission.',
        'Eros': 'Asteroid explored by NASA\'s NEAR Shoemaker spacecraft.',

        'Dinkinesh': 'Asteroid Dinkinesh (Horizons ID 152830) is a small asteroid located in the inner main asteroid belt between \n' 
        'Mars and Jupiter. Its name means "you are wonderful" in Amharic, an Ethiopian language, and was given in honor of the Lucy \n' 
        'fossil, for which the Lucy mission is also named.\n' 
        '* The Lucy spacecraft launched on October 16, 2021, and is on a 12-year journey to explore a record-breaking number of \n' 
        '  asteroids. While its primary targets are the Jupiter Trojans, Lucy also makes flybys of main belt asteroids, like Dinkinesh, \n' 
        '  to test its instruments and trajectory.\n' 
        '* The flyby of Dinkinesh on November 1, 2023, was an engineering test of Lucy\'s autonomous tracking system, which is crucial \n' 
        '  for precisely targeting its main scientific objectives. This successful encounter demonstrated Lucy\'s capabilities and \n' 
        '  delivered the unexpected discovery of Selam, adding to our understanding of asteroid systems.\n'
        '* Dinkinesh is approximately 790 meters (0.5 miles) at its widest. A surprising discovery made by the Lucy spacecraft during \n' 
        '  its flyby was that Dinkinesh is not alone; it has a natural satellite named Selam. Even more remarkably, Selam itself is a \n' 
        '  contact binary, meaning it is composed of two smaller objects (each about 220 meters, or 0.15 miles, in diameter) touching \n' 
        '  each other. This was the first time a contact binary had been observed orbiting another asteroid.\n' 
        '* Observations of Dinkinesh and Selam have revealed a complex history. Dinkinesh has a prominent equatorial ridge and a \n' 
        '  linear trough, suggesting it has some internal strength and may have undergone a sudden "break-up" event where a chunk \n' 
        '  shifted, forming debris that later coalesced to create Selam. The system is tidally locked, with Selam orbiting Dinkinesh \n' 
        '  every 52.7 hours.\n' 
        '* Dinkinesh is also notable for being the smallest main belt asteroid ever visited by a spacecraft, providing valuable \n' 
        '  insights into how asteroids evolve, especially those that might eventually leave the main belt and become near-Earth asteroids.',

        'Donaldjohanson': 'A main-belt asteroid visited by the Lucy spacecraft.',

        'Eurybates': 'A trojan asteroid that will be visited by the Lucy spacecraft.',

        'Patroclus': 'A trojan asteroid that will be visited by the Lucy spacecraft.',

        'Polymele': 'A trojan asteroid that will be visited by the Lucy spacecraft.',

        'Orus': 'A trojan asteroid that will be visited by the Lucy spacecraft.',

        'Leucus': 'A trojan asteroid that will be visited by the Lucy spacecraft.',

        'Itokawa': 'Asteroid visited by the original Hayabusa mission.',

        'Jupiter': 'The largest planet in our solar system, famous for its Great Red Spot.\n'
        '* Jupiter-centered: do not select Jupiter; visualize shells at 0.5 AU.\n'
        '* Heliocentric: select Jupiter with or without shells.\n'
        '* Missions: Pioneer 10 and 11; Voyager 1 and 2; Ulysses; Cassini-Huygens; New Horizons; Galileo;\n' 
        '  Juno; JUpiter ICy moons Explorer (JUICE);Europa Clipper.\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.',

        'Metis': 'Jupiter moon. Innermost known moon, orbits within Jupiter\'s main ring, contributing dust to it.',
        'Adrastea': 'Jupiter moon. Tiny moon orbiting near the outer edge of Jupiter\'s main ring, source of ring material.',
        'Amalthea': 'Jupiter moon. Oddly shaped red moon associated with the Amalthea Gossamer Ring.',
        'Thebe': 'Jupiter moon. Small irregular moon that supplies dust to the outermost Thebe Gossamer Ring.',        
        'Io': 'Jupiter moon. The most volcanically active body in the Solar System.',
        'Europa': 'Jupiter moon. Covered with a smooth ice layer, potential subsurface ocean.',
        'Ganymede': 'Jupiter moon. The largest moon in the Solar System, bigger than Mercury.',
        'Callisto': 'Jupiter moon. Heavily cratered and geologically inactive.',

        'Saturn': 'Known for its beautiful ring system, the sixth planet from the Sun.'
        '* Saturn-centered: do not select Saturn; visualize shells at 0.5 AU.\n'
        '* Heliocentric: select Saturn with or without shells.\n'
        '* Missions: Pioneer 11; Voyager 1 and 2; Cassini-Huygens; Dragonfly (2028).\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.',

        'Titan': 'Saturn moon. The second-largest moon in the Solar System, with a thick atmosphere.',
        'Enceladus': 'Saturn moon. Known for its geysers ejecting water ice and vapor.',
        'Rhea': 'Saturn moon. Saturn\'s second-largest moon, with extensive cratered surfaces.',
        'Dione': 'Saturn moon. Features wispy terrains and numerous craters.',
        'Tethys': 'Saturn moon. Notable for its large Ithaca Chasma canyon.',
        'Mimas': 'Saturn moon. Known for the large Herschel Crater, resembling the Death Star.',

        'Pan': 'The innermost known moon of Saturn. It orbits within the Encke Gap of the A Ring and is responsible for keeping \n' 
        'that gap relatively clear. It has a distinctive equatorial ridge, giving it a flattened, ravioli-like appearance.',

        'Daphnis': 'A small moon that orbits within the Keeler Gap, a narrow gap in the outer part of Saturn\'s A Ring. Its \n' 
        'gravitational influence creates waves in the edges of the gap.', 

        'Prometheus': 'An irregularly shaped inner moon that acts as a shepherd moon for the inner edge of Saturn\'s F Ring. \n' 
        'Its slightly eccentric orbit leads to complex interactions with the ring material, creating kinks and streamers.',

        'Pandora': 'Another irregularly shaped inner moon and the outer shepherd moon of Saturn\'s F Ring. Along with Prometheus, \n' 
        'it helps to confine the F Ring into a narrow band.',

        'Hyperion': 'A mid-sized moon with a highly irregular shape and a chaotic rotation. Its surface is dark and reddish, \n' 
        'possibly due to hydrocarbon deposits, and it has a very porous, sponge-like appearance with many deep craters.',

        'Iapetus': 'A unique moon with a striking two-toned surface. Its leading hemisphere (Cassini Regio) is very dark, while \n' 
        'its trailing hemisphere is bright white, likely due to the deposition of icy material. It also has a mysterious equatorial \n' 
        'ridge that spans a significant portion of its circumference.',
    
        'Phoebe': 'Saturn moon. An irregular moon with a retrograde orbit around Saturn.',

        'Uranus': 'The ice giant with a unique tilt, orbits the Sun on its side.'
        '* Uranus-centered: do not select Uranus; visualize shells at 0.5 AU.\n'
        '* Heliocentric: select Uranus with or without shells.\n'
        '* Missions: Voyager 2; Uranus Orbiter and Probe (planned).\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.',

        'Titania': 'Uranus moon. The largest moon of Uranus, with a mix of heavily cratered and relatively younger regions.',    
        'Oberon': 'Uranus moon. The second-largest moon of Uranus, heavily cratered.',
        'Umbriel': 'Uranus moon. Features a dark surface with numerous impact craters.',  
        'Ariel': 'Uranus moon. Exhibits a mix of heavily cratered regions and younger surfaces.',
        'Miranda': 'Uranus moon. Known for its extreme geological features like canyons and terraced layers.',
        'Portia': 'Uranus moon, associated with outer ring Nu.',
        'Mab': 'Uranus moon, associated with outer ring Mu.',

        'Neptune': 'The eighth and farthest known planet in the solar system.\n'
        '* Neptune-centered: do not select Neptune; visualize shells at 1 AU.\n'
        '* Heliocentric: select Neptune with or without shells.\n'
        '* Missions: Voyager 2; Neptune Orbiter and Probe (possible).\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.',

        'Triton': 'Neptune\'s largest moon, has a retrograde orbit and geysers suggesting geological activity.',
        'Despina': 'Irregularly shaped, likely icy and grayish, orbiting close to the planet and possibly contributing to its ring system',
        'Galatea': 'Irregularly shaped, with an expected icy and grayish appearance, thought to shepherd the Adams ring arc.',

        'Pluto': 'Once considered the ninth planet, now classified as a dwarf planet.\n'
        '* Pluto-centered: do not select Pluto; visualize shells at 0.1 AU.\n'
        '* Heliocentric: select Pluto with or without shells.\n'
        '* Missions: New Horizons; Pluto Orbiter and Probe (possible).\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.',

        'Charon': 'Pluto\'s largest moon is tidally locked with it, forming a binary dwarf planet system.',
        'Styx': 'The smallest and innermost of Pluto\'s known moons is irregularly shaped and orbits between Charon and Nix.',        
        'Nix': 'A small, elongated moon of Pluto with a chaotic rotation.',
        'Kerberos': 'Pluto\'s second-smallest moon is thought to have a double-lobed shape.',
        'Hydra': 'The outermost known moon of Pluto is elongated and has a highly reflective, icy surface.',
        'Haumea': 'A dwarf planet known for its elongated shape and fast rotation.',
        'Makemake': 'A dwarf planet located in the Kuiper Belt, discovered in 2005.',

        'Eris': 'A distant dwarf planet, more massive than Pluto.\n'
        '* Eris/Dysnomia-centered: do not select Eris; visualize shells at 0.1 AU.\n'
        '* Heliocentric: select Eris with or without shells.\n'
        '* Missions: Proposed.\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.',

        'Dysnomia': 'Eris\'s moon. Orbital period: 15.79 Earth days', 

        'Quaoar': 'A large Kuiper Belt object with a ring system.',

        'Sedna': 'A distant trans-Neptunian dwarf planet with a long orbit. \n* Sedna is a fascinating object with an incredibly ' 
        'elongated orbit, meaning its distance from the Sun varies dramatically! \n* Mean distance to Sedna: 526 AU (approximately 79 ' 
        'billion kilometers) - This places it far beyond Pluto and the Kuiper Belt. \n* Perihelion (closest to the Sun): 76 AU ' 
        '\n* Aphelion (farthest from the Sun): A whopping 936 AU! \n* This makes it one of the most distant known objects in our solar system. ' 
        'To put this in perspective, at its farthest point, Sedna is over 20 times farther from the Sun than Pluto is! This extreme ' 
        'orbit is one of the reasons Sedna is so intriguing to astronomers. \n* It\'s thought that its unusual path might be due to ' 
        'gravitational influences from a yet-undiscovered planet in the outer reaches of our solar system, sometimes referred to ' 
        'as \"Planet Nine.\" \n* Sedna\'s long orbital period is another mind-boggling fact. It takes approximately 11,400 years for ' 
        'it to complete one trip around the Sun. \n* Sedna is definitely not a Kuiper Belt object. Its orbit takes it far beyond the ' 
        'Kuiper Belt\'s outer edge. It\'s considered a detached object, meaning its orbit is not significantly influenced by the ' 
        'gravitational pull of Neptune, unlike Kuiper Belt objects. Some astronomers even categorize it as an inner Oort Cloud ' 
        'object due to its immense distance. \n* As for its current distance, Sedna is currently at about 83.3 AU from the Sun. This ' 
        'means it\'s relatively close to its perihelion (closest point) and is currently moving closer to the Sun.',

        'Orcus': 'A large Kuiper Belt object with a moon named Vanth. Estimated to be about 910 km in diameter. ' 
        'Discovered on February 17, 2004.',

        '2017 OF201': 'an extreme trans-Neptunian object and dwarf planet candidate, estimated to be at least 500 kilometres in diameter.\n\n' 
        '* Visualize with a manual scale of at least 1500 AU.',

        'Varuna': 'A significant Kuiper Belt Object with a rapid rotation period.',
        'Ixion': 'A significant Kuiper Belt Object without a known moon.',
        '2004 GV9': 'A binary Kuiper Belt Object providing precise mass measurements through its moon.',
        '2002 MS4': 'A large unnumbered Kuiper Belt Object with no known moons.',  
        'Gonggong': 'One of the largest known Kuiper Belt Objects with a highly inclined orbit.',

        'Planet 9': 'Hypothetical planet with a potential candidate identified in 2025 IRAS/AKARI infrared data. ' 
        'Estimated to be 7-17 Earth masses (possibly Neptune-sized) at 500-700 AU from the Sun. ' 
        'Last detected in the Eridanus constellation with two observations 23 years apart (1983 IRAS and 2006 AKARI). ' 
        'If confirmed, its orbit would be much more distant than previously predicted, swinging between 280-1120 AU.\n\n' 
        'This visualization shows a scientifically plausible position based on the 2025 study, but has significant uncertainty. ' 
        'The exact position, orbit, and even existence of Planet 9 remain subject to confirmation. ' 
        'The position shown is calculated to be consistent with the orbit derived from observed data points, ' 
        'though only two observations (separated by 23 years) have been made so far.\n\n' 
        '* Planet 9-centered: do not select Planet 9; visualize shells at 8 AU.\n'
        '* Heliocentric: select Planet 9 with or without shells at 800 AU.\n'
        '* Missions: None.\n\n'
        'HTML VISUALIZATION 21.9 MB PER FRAME FOR ALL SHELLS AND MOONS.'
        'NOTE: The ideal orbit and estimated position will display in static plots. In animated plots, only the ideal orbit will display.\n\n' 
        'NOTE: This visualization is our estimate and neither the ideal orbit nor position are fetched from JPL Horizons.\n\n' 
        'Select manual scaling of 800 AU to fully display the estimated orbit.', 
# Missions
        'Voyager 1': 'The farthest human-made object from Earth, exploring interstellar space. Voyager 1 is a ' 
        'space probe that was launched by NASA on September 5, 1977, to study the outer Solar System and interstellar space. It is the ' 
        'farthest human-made object from Earth, at a distance of 165.2 AU (24.7 billion km; 15.4 billion mi) as of October 2024.\n ' 
        'Here are some key dates in the Voyager 1 mission:\n * September 5, 1977, launched from Cape Canaveral, Florida.\n ' 
        '* March 5, 1979, reaches Jupiter.\n * November 12, 1980, reaches Saturn.\n * February 14, 1990, takes the \'Pale Blue Dot\' ' 
        'photograph of Earth from a distance of 6 billion kilometers (3.7 billion miles).\n * February 17, 1998, overtakes Pioneer 10 ' 
        'to become the most distant human-made object from Earth.\n * August 25, 2012, crosses the heliopause and enters interstellar ' 
        'space, becoming the first spacecraft to do so.\n Voyager 1 is still operational and continues to send data back to Earth. ' 
        'It is expected to continue operating until at least 2025, when its radioisotope thermoelectric generators will no longer be ' 
        'able to provide enough power to operate its scientific instruments.\n Voyager 1 mission was the first spacecraft to visit ' 
        'Jupiter and Saturn. It discovered active volcanoes on Jupiter\'s moon Io. It revealed the complexity of Saturn\'s rings. ' 
        'It was the first spacecraft to cross the heliopause and enter interstellar space. It is the farthest human-made object from ' 
        'Earth. It is a testament to the ingenuity and perseverance of the scientists and engineers who designed, built, and operate ' 
        'it.',

        'Voyager 2': 'The only spacecraft to visit all four gas giants: Jupiter, Saturn, Uranus, and Neptune.',

        'Cassini': 'NASA: "A joint endeavor of NASA, ESA, and the Italian space agency (ASI), Cassini was a sophisticated robotic ' 
        'spacecraft sent to study Saturn and its complex system of rings and moons in unprecedented detail. Cassini carried a probe ' 
        'called Huygens to the Saturn system. The probe, which was built by ESA, parachuted to the surface of Saturn’s largest moon, ' 
        'Titan, in January 2005 — the most distant landing to date in our solar system. Huygens returned spectacular images and other ' 
        'science results during a two-and-a-half-hour descent through Titan’s hazy atmosphere, before coming to rest amid rounded ' 
        'cobbles of ice on a floodplain damp with liquid methane. Cassini completed its initial four-year mission in June 2008 and ' 
        'earned two mission extensions. Key discoveries during its 13 years at Saturn included a global ocean with strong indications ' 
        'of hydrothermal activity within Enceladus and liquid methane seas on Titan. The mission ended on Sept. 15, 2017."\n' 
        '* Launch: October 15, 1997\n'
        '* Venus flyby: April 26, 1998\n'
        '* Earth flyby: August 17, 1999\n'
        '* Jupiter flyby: December 26, 2000\n'
        '* Saturn orbit insertion: June 30, 2004\n'
        '* Final transmission: September 15, 2017',

        'New Horizons': 'New Horizons flew past Pluto in 2015, now exploring the Kuiper Belt.\n' 
        '* The New Horizons space probe is an interplanetary space probe built by the Applied Physics Laboratory of Johns Hopkins\n' 
        'University for NASA.\n' 
        '* It was launched on January 19, 2006 with the primary mission to conduct a flyby study of Pluto and its moons in the Kuiper Belt. ' 
        'It is the first spacecraft to explore Pluto and the Kuiper Belt up close.\n' 
        '* Approaches 2002 JF56 on June 13, 2006 to within 102,000 km at 10:06 UTC\n' 
        '* Jupiter gravity assist on February 28, 2007, 05:43 UTC, 2.3045(10)^6 km\n'
        '* Pluto Flyby: On July 14, 2015, Pluto-Charon encounter at 11:49:57 UTC. New Horizons made its historic closest approach to ' 
        'Pluto, capturing stunning images and valuable scientific data about the dwarf planet and its moons.\n' 
        '* Kuiper Belt Exploration: After its Pluto encounter, New Horizons continued its journey into the Kuiper Belt.\n' 
        '* Arrokoth (2014 MU69) flyby on January 1, 2019, at 05:35 UTC, as close as 3561 km, or 0.0000238015 AU if you plot it. '
        'NASA reports the closest approach at 3537.7 km, reconstructed, at 5:34:31 UTC.\n' 
        '* Scientific Instruments: New Horizons carries a suite of scientific instruments, including cameras, spectrometers, and ' 
        'plasma analyzers, to study the composition, atmosphere, and environment of Pluto and other Kuiper Belt objects.\n' 
        '* Continuing Mission: New Horizons is still traveling through the Kuiper Belt, and NASA may extend its mission to explore ' 
        'other distant objects in the future.',

        'Arrokoth': 'Arrokoth is the most distant object ever visited by a spacecraft, New Horizons, on January 1, 2019.\n' 
        '  * Official Name: Arrokoth (formerly known as Ultima Thule)\n' 
        '  * JPL Horizons Designation: (486958) 2014 MU69\n' 
        '  * Location: Kuiper Belt, a region beyond Neptune populated by icy bodies\n' 
        '  * Discovered: 2014 by the New Horizons team using the Hubble Space Telescope\n' 
        '  * Shape: A contact binary, meaning it\'s made of two lobes joined together. It resembles a flattened snowman.\n' 
        '  * Size: About 36 km (22 miles) long at its longest axis.\n' 
        '  * Color: Very red, even redder than Pluto. This is due to the presence of complex organic molecules called tholins, formed ' 
        'by radiation interacting with ices.\n' 
        '  * Surface: Smooth with few craters, suggesting it\'s ancient and hasn\'t experienced many impacts.\n' 
        '  * Composition: Likely a mix of ices (water, methane, etc.) and organic materials.\n' 
        '  * Significance:\n' 
        '    * Most Distant Object Explored: Arrokoth is the most distant and most primitive object ever visited by a spacecraft.\n' 
        '    * Clues to Solar System Formation: Because it\'s so far from the Sun, Arrokoth has likely remained relatively unchanged ' 
        'since the early days of the solar system. Studying it helps us understand the conditions and processes that led to the ' 
        'formation of planets and other celestial bodies.\n' 
        '    * Building Blocks of Life: Recent research suggests that Arrokoth may contain sugars like ribose and glucose, which are ' 
        'essential for life as we know it. This raises exciting questions about the potential for life to exist elsewhere in the universe.\n' 
        '    * New Horizons Flyby on January 1, 2019 (See "New Horizons" for more information):\n'
        '      * Plot Arrokoth/New_Horizons as the center body, and New Horizons, to visualize.\n'
        '      * Closest approach by New Horizons at 5:35 UTC, as close as 3561 km, or 0.0000238015 AU if you plot it. ID 2486958.\n' 
        '      * Detailed Images: Stunning images revealed Arrokoth\'s unique shape and surface features.\n' 
        '      * Compositional Data: Instruments on New Horizons analyzed the light reflected from Arrokoth, giving us information ' 
        'about its composition.\n' 
        '      * Insights into Formation: Scientists are using the data to create models of how Arrokoth formed, which has implications ' 
        'for our understanding of planet formation in general.', 

        'Juno': 'NASA\'s Juno mission is a spacecraft orbiting Jupiter to study the planet\'s origins, structure, atmosphere, and ' 
        'magnetosphere.\n'
        '* Key dates:\n' 
        '  * Juno launched on August 5, 2011.\n' 
        '  * Earth Flyby (Gravity Assist) on October 9, 2013\n' 
        '  * Jupiter Arrival and Orbit Insertion on July 5, 2016\n'
        '  * First Ganymede Flyby on June 7, 2021\n'
        '  * Extended Mission Start on August 1, 2021\n' 
        '  * First Europa Flyby on September 29, 2022\n' 
        '  * First Io Flyby on December 30, 2023\n'
        '  * Second Io Flyby on February 3, 2024\n'
        '  * End of recorded orbit on February 15, 2025\n'
        '  * End of Mission on September 2025 by Jupiter impact\n'
        '* Juno is the first spacecraft to orbit Jupiter from pole to pole, giving it a unique perspective on the planet\'s polar regions.\n' 
        '* Juno is also the first spacecraft to operate on solar power at such a great distance from the Sun.\n' 
        '* Juno has made several significant discoveries, including:\n' 
        '  * Jupiter has a complex and dynamic atmosphere, with powerful storms and cyclones that can last for centuries.\n' 
        '  * Jupiter\'s magnetic field is the strongest in the solar system, and it is generated by a layer of metallic hydrogen deep within the planet.\n' 
        '  * Jupiter has a core that is larger and more diffuse than previously thought.\n' 
        '  * Jupiter\'s moons are diverse and fascinating worlds in their own right, with potential for harboring life.\n' 
        '  * Juno is currently in an extended mission, which will last until 2025. During this time, it will continue to study Jupiter\n' 
        '    and its moons, providing valuable insights into the formation and evolution of our solar system.',

        'Galileo': 'Studied Jupiter and its major moons, including Europa and Ganymede.',

        'Apollo 11 S-IVB': 
        'MANUALLY SCALE TO 0.01 AU.\n'
        '* SPACECRAFT TRAJECTORY: The trajectory here is a reconstruction of the Apollo 11 S-IVB stage Earth departure trajectory ' 
        'developed by Daniel R. Adamo. The trajectory spans the time interval from 1969-Jul-16 16:40 to July 28 00:06 GMT/UTC.\n' 
        '* The Apollo 11 S-IVB spacecraft, as defined in this JPL Horizons ephemeris, refers to the third stage of the Saturn V rocket ' 
        'used for the Apollo 11 mission. This is the last and most powerful stage of the Saturn V rocket that propelled the Apollo 11 ' 
        'mission towards the Moon.\n' 
        '* Translunar Injection (TLI): It fired its engine a second time (after the initial Earth orbit insertion burn) to accelerate ' 
        'the Apollo 11 command/service module (CSM) and lunar module (LM) out of Earth orbit and onto a trajectory towards the Moon.\n' 
        '* Departure from Earth-Moon space: After TLI and the separation of the CSM/LM, the S-IVB stage performed "residual propellant ' 
        'dumps." This maneuver caused it to approach the Moon and then depart Earth-Moon space on a heliocentric trajectory, while ' 
        'the manned Apollo 11 mission continued to the Moon.\n' 
        '* Not the manned part of Apollo 11: It\'s crucial to distinguish the S-IVB stage from the Apollo 11 Command Module, Lunar ' 
        'Module, and the astronauts themselves, who continued on to the Moon and returned to Earth. The S-IVB stage was a discarded ' 
        'part of the rocket that went on its own separate path.\n' 
        '  * Launch, July 16, 13:32:00: This is the moment the Saturn V rocket, carrying the Apollo 11 spacecraft, lifted ' 
        'off from Launch Complex 39A at Kennedy Space Center, Florida. This marked the official start of the mission.\n' 
        '  * Earth orbit insertion, July 16, 13:43:49: After the first two stages of the Saturn V had expended their fuel ' 
        'and separated, the third stage (the S-IVB) ignited to place the Apollo spacecraft (Command/Service Module and Lunar Module) ' 
        'into a parking orbit around Earth. This allowed for final checks and preparation before the journey to the Moon.\n' 
        '  * Translunar injection (TLI), July 16, 16:22:13: This was a critical burn of the S-IVB engine. After orbiting Earth ' 
        'for about 2.5 hours, the S-IVB reignited to provide the immense thrust needed to accelerate the Apollo spacecraft out of ' 
        'Earth orbit and onto a trajectory that would take it to the Moon. This "injection" set the spacecraft on its path across ' 
        'the cislunar space.\n' 
        '  * CSM-LM docking, July 16, 16:56:03:\n' 
        '    * CSM: Command/Service Module. This was the main spacecraft component that housed the three astronauts for most of the mission.\n' 
        '    * The Command Module (CM) was the crew\'s living quarters, control center, and the only part that returned to Earth.\n' 
        '    * The Service Module (SM) contained the main propulsion system, fuel, oxygen, and other consumables. It was jettisoned before re-entry.\n' 
        '    * LM: Lunar Module. This was the two-stage spacecraft designed to land two astronauts on the Moon\'s surface.\n' 
        '    * Explanation: After TLI, the CSM separated from the S-IVB stage. The CSM then turned around, faced the LM (which was still ' 
        'attached to the S-IVB), and carefully docked nose-to-nose with it. This maneuver was crucial for extracting the LM from ' 
        'the S-IVB and preparing for the lunar landing phase. After docking, the combined CSM-LM pulled away from the S-IVB.\n' 
        '  * Lunar orbit insertion, July 19, 17:21:50: After a three-day journey from Earth, the Apollo 11 spacecraft ' 
        '(CSM and LM still docked together) fired its main engine (on the Service Module) to slow down sufficiently and enter ' 
        'orbit around the Moon. This placed them in a stable elliptical orbit from which the landing attempt could be made.\n' 
        '  * CSM-LM separation, July 20, 06:11:53: With the combined spacecraft in lunar orbit, the two active modules ' 
        'separated. Neil Armstrong and Buzz Aldrin were inside the Lunar Module ("Eagle"), while Michael Collins remained in the ' 
        'Command Module ("Columbia") orbiting the Moon. This was the final step before the lunar landing attempt.\n' 
        '  * Lunar landing, July 20, 08:17:40: The Lunar Module, piloted by Armstrong and Aldrin, began its descent from ' 
        'lunar orbit. After a tense, manually piloted final approach, the LM "Eagle" successfully touched down on the Moon\'s '
        'surface in the Sea of Tranquility. This marked the first time humans landed on an extraterrestrial body.\n' 
        '  * Begin EVA, July 20, 14:39:33: Extravehicular Activity. This refers to any activity performed by an astronaut ' 
        'outside a spacecraft. In this context, it specifically means stepping out of the Lunar Module onto the Moon\'s surface.\n '
        'After landing, Armstrong and Aldrin spent several hours preparing the LM for their spacewalk. This event marks the beginning ' 
        'of their preparations to exit the LM and begin their surface exploration.\n' 
        '  * First step on surface, July 20, 14:56:15: Neil Armstrong emerged from the Lunar Module and became the first ' 
        'human to step onto the Moon\'s surface, uttering the famous words, "That\'s one small step for man, one giant leap for mankind." ' 
        'Buzz Aldrin joined him shortly after.\n' 
        '  * Lunar liftoff, July 21, 17:54:01: After about 21.5 hours on the lunar surface, the ascent stage of the Lunar ' 
        'Module (carrying Armstrong and Aldrin) fired its engine, leaving the descent stage behind on the Moon. This propelled them ' 
        'back into lunar orbit to rendezvous with the Command Module.\n' 
        '  * LM-CSM docking, July 21, 09:34:00: The Lunar Module ascent stage successfully rendezvoused with the Command ' 
        'Module, still piloted by Michael Collins in lunar orbit. The two spacecraft then docked, allowing Armstrong and Aldrin ' 
        'to transfer back into the Command Module with their lunar samples. The LM ascent stage was then jettisoned into lunar orbit.\n' 
        '  * Transearth injection, July 21, 16:54:42: With all three astronauts safely aboard the Command Module, its main ' 
        'engine was fired one last time. This "injection" burn accelerated the Command Module out of lunar orbit and set it on a ' 
        'course back to Earth.\n' 
        '  * Splashdown, July 24, 16:50:35: After a journey of about 2.5 days from the Moon, the Command Module (the only ' 
        'part of the spacecraft designed to return to Earth) entered Earth\'s atmosphere, deployed its parachutes, and successfully ' 
        'landed in the Pacific Ocean. The Apollo 11 astronauts splashed down in the Pacific Ocean 2660 km east of Wake Island, 280 ' 
        'south of Johnston Atoll and 24 km from recovery ship USS Hornet. This marked the triumphant end of the Apollo 11 mission.',
        
        'Pioneer 10': 'The first spacecraft to travel through the asteroid belt and make direct observations',
        
        'Pioneer 11': 'The first spacecraft to encounter Saturn and study its rings.',
        
        'Europa-Clipper': 'Europa-Clipper is NASA\'s mission to explore Jupiter\'s moon Europa, launched October 14, 2024. No ephemeris available.',
        
        'OSIRIS REx': 'OSIRIS-REx is a NASA mission that collected samples from asteroid Bennu and returned to Earth.\n' 
        '* NASA information: "OSIRIS-REx ("Origins, Spectral Interpretation, Resource Identification, and Security-Regolith Explorer") explored 101955 ' 
        'Bennu (1999 RQ36), a carbonaceous B-type asteroid whose regolith may provide insights on the early history of the solar ' 
        'system. After the sample was returned to Earth, in 2023, the mission was retargeted to encounter asteroid Apophis in 2029 ' 
        'and renamed OSIRIS-APEX ("APophis EXplorer").\n' 
        '* MISSION EVENT SUMMARY (UTC):\n' 
        '  * 2016  Sep 08 23:05 Launch from Cape Canaveral\n' 
        '  * 2017  Sep 22 16:52 Earth flyby and gravity assist 23,592 km from geocenter\n' 
        '  * 2018  August, Bennu approach phase\n' 
        '  *       October, Rendevous with asteroid\n' 
        '  *       November, Estimate mass, shape, and spin state models\n' 
        '  *       December 3, Proximity operations began. Closest approach from December 4, 13:00 to 21:00. This marked the start ' 
        'of its detailed study of the asteroid.\n' 
        '  * 2019  January, Begin detailed mapping; identify candidate sample sites\n' 
        '  *       May, Sorties to examine 4 candidate sample sites\n' 
        '  *       October, Fly over candidate sample sites\n' 
        '  * 2020  April, First sample-collection rehearsal\n' 
        '  *       August, Second sample-collection rehearsal\n' 
        '  *       October 20, Collect sample > 60 grams. Touchdown from 21:00 to 22:13: OSIRIS-REx successfully collected a sample from Bennu\'s ' 
        'surface on October 20, 2020, at 22:13 UTC. This involved a brief "touch-and-go" maneuver where the spacecraft\'s sampling ' 
        'arm made contact with the asteroid\'s surface to collect dust and rocks. The plot will show the closest approach at about ' 
        '0.0000000024 to 0.0000000026 AU, third of a meter from the surface -- the length of the sampling arm.\n' 
        '  * 2021  May 10, Start return cruise and transport sample back to Earth\n' 
        '  * 2023  September 24, Sample Return Capsule (SRC) recovery on Earth\n' 
        '  * 2023  October 24, Retargeting maneuver for Apophis (OSIRIS-APEX)\n' 
        '* MISSION OBJECTIVES:\n'  
        '  * Map the asteroid\n' 
        '  * Return and analyze a sample of Bennu\'s surface\n' 
        '  * Document the sample site\n' 
        '  * Measure the orbit deviation caused by small non-gravitational forces\n' 
        '  * Compare observations made at the asteroid to ground-based observations\n' 
        'NOTE: To generate ephemerides OF destination asteroid Bennu as a target look-up "2101955". To use asteroid Bennu as an ' 
        'observing point, set the coordinate center to "@ 2101955". The Sample Return Capsule can be accessed as object \'-64090\' ' 
        'Apophis mission trajectory as object \'2099942\'',

        'OSIRIS APEX': 'OSIRIS-APEX is a NASA mission that will study the asteroid Apophis.\n' 
        '* OSIRIS-REx\'s Legacy: OSIRIS-REx was a NASA mission that successfully traveled to the asteroid Bennu, collected a sample ' 
        'of its surface material, and returned it to Earth in September 2023. This was a landmark achievement in asteroid exploration.\n' 
        '* Spacecraft in Good Condition: After completing its primary mission, the OSIRIS-REx spacecraft was still in good working ' 
        'order and had plenty of fuel left.\n' 
        '* Extended Mission: Instead of retiring the spacecraft, NASA decided to extend the mission and send it to another asteroid, ' 
        'Apophis. This new mission was named OSIRIS-APEX (Origins, Spectral Interpretation, Resource Identification, and Security - ' 
        'Apophis Explorer).\n' 
        '* Repurposed Spacecraft: OSIRIS-APEX is essentially the same OSIRIS-REx spacecraft, but with a new target and new objectives.\n' 
        '* Connection to OSIRIS-REx: The most direct connection is that OSIRIS-APEX uses the exact same spacecraft that successfully ' 
        'explored Bennu. This means it inherits all the capabilities and instruments that were used on the OSIRIS-REx mission.\n' 
        '* Building on Knowledge: The knowledge and experience gained from the OSIRIS-REx mission are invaluable for OSIRIS-APEX. ' 
        'Scientists and engineers can apply what they learned about asteroid navigation, sample collection, and data analysis to the ' 
        'new mission.\n' 
        '* Study Apophis: OSIRIS-APEX will study the asteroid Apophis, which is a near-Earth asteroid that will make a very close ' 
        'approach to Earth in 2029. This close approach will allow scientists to observe how Earth\'s gravity affects the asteroid.\n' 
        '* Different Asteroid Type: Apophis is a different type of asteroid than Bennu. It\'s a "stony" asteroid rather than a ' 
        'carbonaceous one. This gives scientists an opportunity to compare and contrast different types of asteroids.\n' 
        '* Surface Changes: OSIRIS-APEX will observe Apophis before and after its close encounter with Earth to see how the encounter ' 
        'changes the asteroid\'s surface.\n'
        '* Not just a one-time flyby: While OSIRIS-APEX will indeed fly by Apophis, it\'s not just a quick pass-by like some ' 
        'traditional flyby missions. The spacecraft will actually enter a close orbit around Apophis and study it for an extended ' 
        'period.\n' 
        '  * Close Approach: Before entering orbit, OSIRIS-APEX will perform a close flyby of Apophis. This will allow the spacecraft ' 
        'to gather crucial data about the asteroid\'s shape, size, mass, and surface features. This information will help scientists ' 
        'plan the subsequent orbital phase of the mission. The close flyby is expected to happen shortly after Apophis makes its close ' 
        'approach to Earth in April 2029.\n' 
        '  * Purpose of the Flyby: The primary purpose of the flyby is to gather preliminary data about Apophis. This will help ' 
        'scientists select the best location for the spacecraft to enter orbit and conduct more detailed studies. By observing Apophis ' 
        'before and after its close approach to Earth, OSIRIS-APEX can study how the asteroid\'s surface and rotation are affected by ' 
        'Earth\'s gravity. This is a rare opportunity to observe such a phenomenon up close.\n' 
        '  * Orbital Phase: After the initial flyby, OSIRIS-APEX will enter orbit around Apophis. This will allow for long-term study ' 
        'of the asteroid, including mapping its surface, analyzing its composition, and observing any changes caused by the Earth flyby.\n' 
        '  * "Touch-and-Go" Maneuver: OSIRIS-APEX is also planned to perform a maneuver similar to the touch-and-go sample collection ' 
        'on Bennu. However, this time it won\'t be collecting a sample. Instead, it will use its thrusters to disturb Apophis\'s surface, ' 
        'allowing scientists to study the material beneath.',
        
        'Parker Solar Probe':
        'The Parker Solar Probe is studying the Sun\'s outer corona by flying closer to the Sun than any previous spacecraft.\n\n'
        'Operating Region:\n'
        '* Sun\'s surface (photosphere): ~0.00465 AU\n'
        '* Inner corona: extends to ~2 to 3 solar radii or 0.01 AU\n'
        '* Parker\'s closest approach: 3.8 million miles, 8.8 solar radii or 0.041 AU\n'
        '* Outer corona: extends to ~50 solar radii or 0.2 AU\n'
        '* For scale - Mercury\'s orbit: 0.387 AU\n\n'
        'The corona\'s temperature paradoxically increases from ~6,000K at the Sun\'s surface '
        'to over 2 million K in the inner corona. Parker Solar Probe is helping scientists '
        'understand this coronal heating mystery.\n\n'
        'Mission Timeline:\n'
        '* Launch: August 12, 2018\n'
        '* First perihelion: November 5, 2018\n'
        '* Final closest approach: 8.8 solar radii at 7AM EST on December 24, 2024\n\n'
        '* NOTE: To visualize the closest approach plot Paker on December 24, 2024, at 12 hours.',       
        
        'James Webb Space Telescope': 'The James Webb Space Telescope is NASA\'s flagship infrared space telescope, orbiting Lagrange point 2.',
        
        'Rosetta': 'European Space Agency mission that studied Comet 67p/Churyumov-Gerasimenko. The Rosetta mission significantly ' 
        'advanced our understanding of comets and their role in the early solar system. Its data continues to be analyzed, providing ' 
        'valuable information for planetary science.\n' 
        '* Key Dates:\n' 
        '  * Launch: March 2, 2004 - Rosetta launched from Kourou, French Guiana.\n' 
        '  * Flybys: Rosetta performed flybys to gain gravitational assists and adjust its trajectory.\n'
        '    * Earth Flyby 1: March 4, 2005\n' 
        '    * Mars Flyby: February 25, 2007\n' 
        '    * Earth Flyby 2: November 13, 2007\n' 
        '    * Steins, on September 5, 2008\n' 
        '    * Earth Flyby 3: November 12, 2009\n' 
        '    * Lutetia, on July 10, 2010\n' 
        '  * Deep Space Hibernation: From June 2011 to January 2014, Rosetta entered hibernation mode to conserve energy.\n' 
        '  * Comet Arrival: August 6, 2014 - Rosetta arrived at Comet 67P/Churyumov-Gerasimenko and began orbiting it.\n' 
        '  * Philae Lander Deployment: November 12, 2014 - The Philae lander was deployed and successfully landed on the comet\'s surface.\n' 
        '  * Perihelion Passage: August 13, 2015 - Comet 67P reached perihelion, and Rosetta observed its most active period.\n' 
        '  * Mission End: September 30, 2016 - The Rosetta mission concluded with a controlled impact onto the comet\'s surface.\n'
        '  * JPL Horizons data ends 2016-10-05.\n' 
        '* The Rosetta mission was a groundbreaking space exploration endeavor by the European Space Agency (ESA) to study Comet ' 
        '67P/Churyumov-Gerasimenko. Launched in 2004, the Rosetta spacecraft traveled for ten years to reach the comet.\n' 
        '* Firsts: Rosetta was the first mission to orbit a comet nucleus and deploy a lander, Philae, onto its surface.\n' 
        '* Long-term Observation: The mission provided unprecedented insights into cometary activity by accompanying 67P as it traveled ' 
        'closer to the Sun.\n' 
        '* Scientific Discoveries: Rosetta\'s data revealed the comet\'s composition, including organic molecules, and challenged existing ' 
        'theories about the origin of Earth\'s water.\n' 
        '* Mission Duration: Rosetta orbited Comet 67P from August 2014 to September 2016, witnessing the comet\'s most active period.\n' 
        '* Legacy: The Rosetta mission significantly advanced our understanding of comets and their role in the early solar system. ' 
        'Its data continues to be analyzed, providing valuable information for planetary science.', 

        'BepiColombo': 'BepiColombo is a mission to explore Mercury, the innermost and smallest planet in our solar system! ' 
        'It\'s a joint endeavor by the European Space Agency (ESA) and the Japan Aerospace Exploration Agency (JAXA).\n ' 
        '* The mission consists of two main spacecraft that journeyed to Mercury together: Mercury Planetary Orbiter (MPO) ' 
        'built by ESA, it will study Mercury\'s surface and internal composition. And Mercury Magnetospheric Orbiter (Mio) ' 
        'developed by JAXA, it will investigate Mercury\'s magnetic field and its interaction with the solar wind.\n ' 
        '* BepiColombo was launched in October 2018 and is using a combination of gravity assists: flybys of Earth, Venus, ' 
        'and Mercury itself to adjust its trajectory and slow down; solar electric propulsion: ion thrusters for fine-tuning ' 
        'its path.\n '
        '* Earth flyby: April 10, 2020\n* Venus flyby 1: October 15, 2020\n* Venus flyby 2: August 10, 2021\n' 
        '* Mercury flyby 1: October 1, 2021\n* Mercury flyby 2: June 23, 2022\n* Mercury flyby 3: June 20, 2023\n' 
        '* Mercury flyby 4: September 5, 2023\n* Mercury flyby 5: December 2, 2024\n* Mercury flyby 6: January 8, 2025\n' 
        '* Mercury Orbit Insertion: December 5, 2025\n' 
        'Each of these flybys has been essential in gradually slowing the spacecraft down enough to achieve Mercury orbit.\n ' 
        'The January 8th flyby is the final gravitational assist before the spacecraft prepares for its historic orbit\n ' 
        'insertion around Mercury later in 2025.'
        '* BepiColombo is scheduled to arrive at Mercury in December 2025. Once there, the two orbiters will separate and ' 
        'enter their respective orbits around Mercury.\n ' 
        '* Challenges: Mercury experiences scorching temperatures of over 400°C (750°F). The spacecraft needs special ' 
        'protection from the Sun\'s powerful radiation. Mercury\'s proximity to the Sun creates a strong gravitational pull.\n ' 
        '* BepiColombo is the most comprehensive mission to Mercury to date, with two orbiters providing a detailed view of ' 
        'the planet and its environment. It\'s a prime example of international cooperation in space exploration.\n ' 
        '* Timeline:\n ' 
        '  * According to this model, the closest flyby of Mercury by BepiColombo occurred on January 8th, 2025, 6 UTC. ' 
        'During this flyby, the spacecraft came within approximately 0.00001829 AU from Mercury\'s surface: 0.00001829 AU = 2,736 km ' 
        '(from Mercury\'s center), Mercury radius = 2,440 km, actual flyby altitude ≈ 296 km above Mercury\'s surface!\n ' 
        '  * This is the statement from ESA, \"On 8 January 2025, the ESA/JAXA BepiColombo mission will fly just 295 km above ' 
        'Mercury\'s surface, with a closest approach scheduled for 06:59 CET (05:59 UTC). It will use this opportunity to ' 
        'photograph Mercury, make unique measurements of the planet\'s environment, and fine-tune science instrument operations ' 
        'before the main mission begins. This sixth and final flyby will reduce the spacecraft\'s speed and change its direction, ' 
        'readying it for entering orbit around the tiny planet in late 2026.\"\n ' 
        '  * December 2025 - November 2026: After the flyby, BepiColombo will still be in a trajectory that takes it around ' 
        'the Sun, but it will be heavily influenced by Mercury\'s gravity. It will essentially be "captured" by Mercury, ' 
        'but not yet in a stable orbit.\n ' 
        '  * November 2026: Finally, after a series of maneuvers, BepiColombo will achieve a stable orbit around Mercury. ' 
        'The two orbiters (MPO and Mio) will then separate and begin their individual science missions.\n ' 
        '  * The BepiColombo mission has a planned duration of one Earth year of scientific observations at Mercury. This ' 
        'nominal mission is set to begin in April 2027, after the orbiters have settled into their final orbits and ' 
        'completed their commissioning phase.\n ' 
        '  * If the spacecraft remain in good health and there\'s continued scientific interest, the mission could be ' 
        'prolonged for another one to two years. This would allow scientists to gather even more data and further deepen ' 
        'our understanding of Mercury.\n '
        'It\'s a complex dance with gravity, but this intricate approach is necessary to get BepiColombo into the right ' 
        'position to study Mercury effectively!',
        
        'SOHO Solar Observatory': 'The Solar and Heliospheric Observatory is located at the L1 Lagrange point.',

        'Solar Orbiter': 'From JPL Horizons: Solar Orbiter ("Solo"), an ESA/NASA mission, was launched 2020-Feb-10 at 4:03 UTC from ' 
        'Cape Canaveral, Florida\n' 
        '* The 7-year mission will provide close-up, high-latitude observations of the Sun from a highly elliptic orbit that ranges ' 
        'between 0.28 au at perihelion (~60 solar radii, inside Mercury''s orbit) and 1.2 au at aphelion.\n' 
        '* It will reach its operational orbit ~22 months after launch by using gravity assist maneuvers (GAMs) at Earth and Venus.\n' 
        '* During closest approach (every ~5 months), Solar Orbiter will be positioned for several days over roughly the same region ' 
        'of the solar atmosphere, as the Sun rotates on its axis beneath the spacecraft. The spacecraft will thus effectively "hover" ' 
        'over the rotating surface, and therefore able to watch developing magnetic activity that can lead to flares and eruptions. ' 
        'The view of the solar poles from higher latitudes will help understand how dynamo processes generate the Sun\'s magnetic ' 
        'field. Observations will be coordinated as appropriate between Solar Orbiter and the Parker Solar Probe.\n' 
        '* Flybys:\n' 
        '  * 2020-Dec-26: Venus\n' 
        '  * 2021-Aug-08: Venus\n' 
        '  * 2021-Nov-27: Earth (end of cruise phase)\n' 
        '  * 2022-Sep-04: Venus\n' 
        '  * 2025-Feb-18: Venus\n' 
        '  * 2026-Dec-24: Venus\n' 
        '  * 2028-Mar-17: Venus\n' 
        '  * 2029-Jun-10: Venus\n' 
        '  * 2030-Sep-02: Venus',
        
        'Gaia': 'European Space Agency mission at L2 mapping the Milky Way.',
        
        'Hayabusa 2': 'Japan JAXA mission that returned samples from Ryugu.', 
        
        'Chang\'e': 'China\'s lunar exploration program.',
        
        'Perseverance Mars Rover': 'The Perseverance Rover is NASA\'s Mars rover and Ingenuity helicopter. The NASA Mars Perseverance mission ' 
        'is a robotic space mission currently underway, aimed at exploring the planet Mars and searching for signs of ancient ' 
        'microbial life.\n'
        '* Objective: To investigate the habitability of Mars in the ancient past, search for evidence of past microbial life, collect ' 
        '  and store Martian rock and soil samples for future return to Earth, and test technologies for future human exploration of Mars.\n' 
        '* Launch Date: July 30, 2020\n'
        '* Landing Date: February 18, 2021, at 20:55 UTC.\n'
        '* Perseverance\'s Journey: Perseverance, along with Ingenuity, was housed within a protective aeroshell during its journey ' 
        '  to Mars. This aeroshell helped protect the rover and helicopter during the high-speed entry into Mars\' atmosphere.\n' 
        '* Landing on Mars: During the landing process, the aeroshell separated, and Perseverance used a parachute and a "sky crane" ' 
        '  system to gently lower itself onto the Martian surface. The sky crane then detached and flew away to a safe distance before crashing.\n'
        '* Landing Site: Jezero Crater, a former lake basin believed to be a promising location for finding evidence of past life.\n'
        '* Landing elevation: Jezero Crater is located in a depression on Mars.\n' 
        '  * Its floor lies about 2,600 meters below the "Mars Areoid," which is a reference level similar to sea level on Earth.\n' 
        '  * Note: The elevation values after landing shown (-4200m) differ from published scientific values for Jezero Crater (-2600m) due to \n' 
        '    different Mars reference systems. JPL Horizons uses one elevation datum, while scientific publications often use the \n' 
        '    Mars Orbiter Laser Altimeter (MOLA) reference areoid (3396.19 km). The rover is correctly positioned relative to Mars, but the \n' 
        '    absolute elevation value has a systematic offset of approximately 1600m.\n' 
        '  * Jezero Crater is a 45.0 km diameter crater located in the Syrtis Major quadrangle of Mars. It sits within the larger \n' 
        '    Isidis Planitia region, where an ancient meteorite impact left behind a crater about 1,200 kilometers across. Nasa \n' 
        '    Jezero Crater was once a lake several hundred feet deep. The landing site for Perseverance was carefully chosen after \n' 
        '    examining more than 60 candidate locations, with Jezero being selected because of its ancient river delta which would \n' 
        '    be a prime location to search for signs of past microbial life.\n' 
        '  * According to the Mars geodetic parameters from MOLA (Mars Orbiter Laser Altimeter), the mean equatorial radius is \n' 
        '    3,396,200 meters (with an uncertainty of 160 meters), while the mean radius (volumetric) is 3,389,508 meters.\n'
        '* "Orbit": The apparent "orbit" around Mars in the plot is just the Perseverance lander rotating with Mars on the surface.\n' 
        '* Rover: Perseverance, a six-wheeled, car-sized rover equipped with advanced scientific instruments.\n' 
        '* Helicopter: Ingenuity, a small, experimental helicopter that demonstrated the first powered flight on another planet. ' 
        '  Ingenuity\'s mission has recently ended due to damage sustained during a landing.\n' 
        '* Search for past life: Perseverance is equipped with instruments designed to detect chemical and mineral biosignatures, ' 
        '  as well as examine the geological context of potential past life.\n' 
        '* Sample collection: The rover has a drill and sample caching system to collect and store samples of Martian rock and soil ' 
        '  for future return to Earth. These samples could provide invaluable insights into the history of Mars and the potential for ' 
        '  life beyond Earth.\n' 
        '* Technology demonstration: Perseverance is testing technologies that could be used for future human exploration of Mars, ' 
        '  such as a system for producing oxygen from the Martian atmosphere.\n' 
        '* Status: As of February 2025, Perseverance is still active on Mars, continuing its exploration of Jezero Crater and ' 
        '  collecting samples. The mission is expected to continue for several more years, and the collected samples are planned to ' 
        '  be returned to Earth in the 2030s through a joint mission with the European Space Agency.',
        
        'DART': 'The NASA DART mission to test asteroid deflection.\n* The DART mission ' 
        '(Double Asteroid Redirection Test) was a groundbreaking NASA project that made history in planetary defense! It was the ' 
        'first-ever mission to test a method of deflecting an asteroid by intentionally crashing a spacecraft into it.\n' 
        '* Planetary Defense: The primary goal was to demonstrate the kinetic impactor technique as a viable method for deflecting ' 
        'potentially hazardous asteroids that could pose a threat to Earth.\n'
        '* Didymos and Dimorphos: The target was a binary asteroid system consisting of Didymos (the larger asteroid) and its ' 
        'smaller moonlet Dimorphos.\n'
        '* Impactor: The DART spacecraft was relatively simple, essentially a box-shaped probe with solar panels and a navigation ' 
        'system.\n'
        '* LICIACube: It carried a small companion satellite called LICIACube (Light Italian CubeSat for Imaging of Asteroids) ' 
        'provided by the Italian Space Agency, to observe the impact and its aftermath.\n'
        '* Impact: September 26, 2022\n'
        '* Location: Dimorphos, the smaller asteroid in the Didymos system\n'
        '* Speed: Approximately 6.6 kilometers per second (14,760 miles per hour)\n'
        '* Successful Impact: DART successfully impacted Dimorphos, altering its orbital period around Didymos.\n' 
        '* Momentum Transfer: The impact demonstrated that a kinetic impactor can effectively transfer momentum to an asteroid, ' 
        'changing its trajectory.\n' 
        '* Deflection Measurement: Observations from ground-based telescopes and LICIACube confirmed that Dimorphos\'s orbit was ' 
        'shortened by about 32 minutes, exceeding expectations.\n'
        '* Planetary Protection: It demonstrated a viable technique for defending Earth from potentially hazardous asteroids.\n' 
        '* Technology Demonstration: It tested and validated new technologies for autonomous navigation and targeting of small ' 
        'celestial bodies.\n' 
        '* Scientific Research: The impact provided valuable data on the composition and structure of asteroids.',
        
        'Lucy': 'The NASA Lucy mission exploring Trojan asteroids around Jupiter.\n' 
        '* The Lucy mission is a groundbreaking NASA space probe that\'s on an ambitious journey to explore the Trojan asteroids, a \n' 
        '  unique population of asteroids that share Jupiter\'s orbit around the Sun. These "Trojan swarms" are like fossils of our \n' 
        '  early solar system, holding clues to the formation of the planets and the conditions that existed billions of years ago.\n' 
        '* Lucy will visit a total of eight asteroids. Main Belt Asteroids: 52246 Donaldjohanson; 152830 Dinkinesh. \n' 
        '  Trojan Asteroids: 3548 Eurybates (and its satellite Queta); 15094 Polymele; 11351 Leucus; 21900 Orus; 617 Patroclus \n' 
        '  (and its binary companion Menoetius).\n' 
        '  * Jupiter\'s Trojan asteroids orbit the Sun in two large "swarms" that lead (Greek) and trail (Trojan) Jupiter, at the same distance from \n' 
        '    the Sun as the gas giant. Scientists believe the Trojans are remnants of the primordial material that formed the outer \n' 
        '    planets, essentially "time capsules" from the early solar system. Studying them can provide vital clues to understanding \n' 
        '    the formation and evolution of our solar system and potentially even the origins of life on Earth.\n' 
        '  * Key objectives of the Lucy mission include: Understanding the early phases, conditions, and processes of solar system \n' 
        '    formation; determining the composition, structure, and geology of Trojan asteroids; investigating the possibility of \n' 
        '    changing orbits of the giant gas planets; looking for rings and satellites of the Trojan asteroids.\n' 
        '  * The Lucy spacecraft launched on October 16, 2021, and is on a 12-year journey to explore a record-breaking number of \n' 
        '    asteroids. While its primary targets are the Jupiter Trojans, Lucy also makes flybys of main belt asteroids, like \n' 
        '    Dinkinesh, to test its instruments and trajectory.\n'
        '  * Earth flyby occurred on October 16, 2022, exactly one year after its launch. This was the first of three planned Earth \n' 
        '    gravity assists for the Lucy spacecraft. These gravity assists are crucial for Lucy\'s trajectory, using Earth\'s \n' 
        '    gravitational pull to gain speed and adjust its course towards its distant targets in the asteroid belt and the Jupiter Trojans.\n'
        '  * The flyby of Dinkinesh on November 1, 2023, was an engineering test of Lucy\'s autonomous tracking system, which is \n' 
        '    crucial for precisely targeting its main scientific objectives. This successful encounter demonstrated Lucy\'s \n' 
        '    capabilities and delivered the unexpected discovery of Selam, adding to our understanding of asteroid systems.\n' 
        '  * December 12, 2024: Second Earth gravity assist (Earth flyby). This will send Lucy out towards the Trojan asteroids.\n'
        '  * April 20, 2025: Flyby of (52246) Donaldjohanson (main belt asteroid). This served as a rehearsal for the Trojan encounters.\n' 
        '  * August 12, 2027: Flyby of (3548) Eurybates (Trojan asteroid, Greek camp) and its satellite Queta.\n' 
        '  * September 15, 2027: Flyby of (15094) Polymele (Trojan asteroid, Greek camp) and its unnamed satellite.\n' 
        '  * April 18, 2028: Flyby of (11351) Leucus (Trojan asteroid, Greek camp).\n' 
        '  * November 11, 2028: Flyby of (21900) Orus (Trojan asteroid, Greek camp).\n' 
        '  * December 25, 2030: Third and final Earth gravity assist (Earth flyby). This will send Lucy to the second swarm of Trojan asteroids.\n' 
        '  * March 3, 2033: Flyby of the binary pair (617) Patroclus and Menoetius (Trojan asteroids, Trojan camp).',

        'Akatsuki': 'The Venus Climate Orbiter mission (PLANET-C), will study the atmospheric circulation of Venus over a nominal mission of 4.5 years.',

# Comets        
        'Ikeya-Seki': 'Comet Ikeya-Seki, formally designated C/1965 S1, was a stunning sungrazing comet that put on quite a show ' 
        'in 1965! It was one of the brightest comets of the 20th century and is a member of the Kreutz sungrazers, a family of ' 
        'comets believed to have originated from a larger comet that broke apart long ago. As a Kreutz sungrazer, it provided valuable ' 
        'information about these comets and their origins.\n  Key dates and information:\n ' 
        '* September 18, 1965: Kaoru Ikeya and Tsutomu Seki, two amateur astronomers in Japan, independently discovered the comet. ' 
        'It was initially a faint telescopic object.\n * October 21, 1965: Ikeya-Seki reached perihelion, its closest point to the Sun.' 
        'It passed incredibly close, a mere 450,000 km (280,000 mi) above the Sun\'s surface! This made it briefly visible in daylight. ' 
        'The intense heat caused the comet\'s nucleus to fragment into at least three pieces. The breakup of its nucleus offered ' 
        'scientists a rare opportunity to study the composition and behavior of comets.\n * Late October - November 1965: ' 
        'After perihelion, Ikeya-Seki developed a spectacularly long tail, stretching across the sky for millions of miles. ' 
        'It was a breathtaking sight for observers.\n * Post-1965: The comet faded from view as it moved away from the Sun. ' 
        'Though it\'s still out there, with an orbital period estimated to be roughly 880 years, we won\'t see it again for a ' 
        'very long time.',
        
        'West': 'Notable comet for its bright and impressive tail.',
        
        'Halley': 'Most famous comet, returns every 76 years. ' 
        '* Orbital Period and Characteristics: Halley\'s Comet has an average orbital period of 76 Earth years. However, this period ' 
        'can vary due to the gravitational influence of planets, particularly Jupiter and Saturn.  In fact, the gravitational pull ' 
        'of the major planets alters the orbital period from revolution to revolution. Measured from one perihelion passage to the ' 
        'next, Halley\'s period has been as short as 74.42 years (1835-1910) and as long as 79.25 years (451-530).\n' 
        '* Orbit Path: The comet\'s orbit is highly elliptical, with an eccentricity of ' 
        '0.967. This means its path around the Sun takes it from a point relatively close to the Sun (perihelion) to a point far ' 
        'beyond Neptune\'s orbit (aphelion).\n' 
        '* Orbit is Retrograde: Halley\'s Comet orbits the Sun in a retrograde direction, opposite to the direction of most planets. ' 
        'Its orbit is also inclined by 18 degrees to the ecliptic, the plane of Earth\'s orbit.\n' 
        '* History of Observations: Halley\'s Comet has been observed and recorded by astronomers for millennia. Before Halley\'s ' 
        'prediction of its return in 1705, these appearances were not recognized as being the same object. Ancient civilizations, ' 
        'particularly the Chinese, meticulously documented cometary appearances, providing valuable historical records.  It is a ' 
        'remarkable fact that observations made with the naked eye 2,000 years ago are still of value today. In the centuries ' 
        'leading up to Halley\'s prediction, observations from China, Babylon, and Europe helped to track the comet\'s appearances. ' 
        'These observations, even those made with the naked eye, have proven valuable for modern astronomers studying the comet\'s ' 
        'long-term behavior.\n' 
        '  * The comet\'s appearance in 1066, shortly before the Norman Conquest of England, is perhaps its most famous historical ' 
        'sighting. It was depicted in the Bayeux Tapestry, a significant historical artifact. It is said that William the Conqueror ' 
        'believed the comet heralded his success.\n' 
        '  * The 1910 apparition of Halley\'s Comet was also notable, as it was the first time the comet was captured on camera.\n' 
        '  * The 1986 apparition marked a turning point in our understanding of comets. For the first time, spacecraft were sent ' 
        'to encounter a comet, providing close-up images and data about its nucleus and composition. This included:\n' 
        '    * Giotto (European Space Agency), which provided the first close-up images of the nucleus.\n' 
        '    * Vega 1 and 2 (Soviet Union), which provided data and images.\n' 
        '    * Suisei and Sakigake (Japan). These probes studied the comet\'s coma and tail.\n' 
        '    * International Cometary Explorer (NASA).\n'
        '  * Halley\'s Comet reached perihelion on February 9th, 1986.\n' 
        '  * Halley reached its closest approach to Earth on April 11, 1986 at a distance of 0.42 AU or 62.4 million km.\n'  
        '  * Halley\'s Comet reached aphelion most recently on December 9, 2023.\n' 
        '  * It will reach perihelion next on July 28th, 2061 and then aphelion again on November 21st, 2097.\n'
        '* Halley\'s Meteor Showers: Each time Halley returns to the inner solar system, its nucleus sprays ice and rock into space. ' 
        'This debris stream results in two weak meteor showers each year: the Eta Aquarids in May and the Orionids in October.\n' 
        '* Physical Characteristics:\n' 
        '  * Halley\'s Comet is a relatively small object, with a nucleus measuring approximately 15 kilometers long, 8 kilometers ' 
        'wide, and 8 kilometers thick. Its shape has been likened to a peanut or a potato.\n' 
        '  * Its low density indicates that it is made of a large number of small pieces, held together very loosely, forming a ' 
        'structure known as a rubble pile.\n' 
        '  * The comet\'s nucleus is a dark, dusty conglomerate of ice and rock, often described as a "dirty snowball."\n' 
        '  * It reflects only 4% of the light that falls on it. This makes it one of the darkest objects in the solar system. This ' 
        'dark coloration is likely due to a layer of dust and complex organic molecules covering much of its surface.\n' 
        '* Tail or Coma: As Halley approaches the Sun, its volatile compounds, such as water, carbon monoxide, and carbon dioxide, begin to ' 
        'sublimate, forming a coma, or atmosphere, around the nucleus. This coma can extend up to 100,000 kilometers across. The ' 
        'sublimation process also releases dust particles, which contribute to the comet\'s tail.\n' 
        '* Next Predicted Perihelion Passage: Halley\'s Comet is expected to reach its next perihelion, or closest approach to the ' 
        'Sun, on July 28, 2061. During this apparition, Earth will be in a more favorable position for viewing the comet compared to ' 
        'its 1986 appearance. It is predicted to be as bright as some of the brightest stars in the sky (apparent magnitude -0.3). ' 
        'Even more exciting, in 2134, Halley\'s Comet will pass very close to the earth (0.09 AU, or about 13 million km) and should ' 
        'be much brighter than in 2061 (apparent magnitude -2).',
        
        'Hyakutake': 'Comet passed very close to Earth in 1996.',
        
        'Hale-Bopp': 'Comet Hale-Bopp: Visible to the naked eye for 18 months.',
        
        'McNaught': 'Known as the Great Comet of 2007. January 12, 2007.',
        
        'NEOWISE': 'Brightest comet visible from the Northern Hemisphere in decades.',

        'C/2025_K1': 'Comet C/2025 K1 (ATLAS) is a recently discovered comet that is expected to become a notable object for \n' 
        'observation in late 2025. Here\'s a breakdown of what we know:\n' 
        '* Discovery and Classification: It was discovered on May 25, 2025, by the Asteroid Terrestrial-impact Last Alert System (ATLAS) \n' 
        '  survey in Chile. It appears to be a dynamically new comet, meaning it\'s likely making its first close passage to the Sun.\n' 
        '* Orbital Characteristics: Perihelion (closest approach to the Sun): October 8, 2025, at a distance of approximately 0.33 AU, \n' 
        '  which is closer than Mercury\'s orbit. This close approach to the Sun is significant and could lead to substantial brightening.\n' 
        '* Closest approach to Earth: November 24, 2025, at a distance of about 0.40 AU.\n' 
        '* Eccentricity (e): The orbit is highly eccentric, 1.000251464554613 (July 11, 2025), indicating an unbound or nearly parabolic orbit.\n' 
        '* Inclination (i): The orbital plane is highly inclined, 147.864867556013 degrees.\n' 
        '* Visibility and Brightness: As of early July 2025, it\'s around magnitude 14-15, requiring a telescope for observation.\n' 
        '* Predicted Peak Brightness: It\'s expected to brighten significantly as it approaches perihelion. Predictions suggest it could \n' 
        '  reach a magnitude of around 5.2 to 8 in early October 2025.\n' 
        '* Naked-eye visibility: While magnitude 5.2 is generally considered within naked-eye visibility under very dark skies, it\'s \n' 
        '  more likely to be a binocular object for most observers, especially at its peak brightness.\n' 
        '* Observing Locations: Early October (near perihelion), observers in northern latitudes will see it best in the morning sky. \n' 
        '  Observers in southern latitudes can spot it in both the evening and morning skies.\n' 
        '* August: It will be faint (around magnitude 13) and visible only from the Southern Hemisphere through large telescopes.',
        
        'Tsuchinshan-ATLAS': 'Comet Tsuchinshan-ATLAS was discovered independently by the Purple Mountain Observatory in China (Tsuchinshan) in January 2023 ' 
        'and the Asteroid Terrestrial-impact Last Alert System (ATLAS) in South Africa in February 2023.\n * It originates from the ' 
        'Oort cloud, meaning it takes tens of thousands of years to orbit the Sun.\n * It orbits the Sun in the opposite direction ' 
        'to most planets.\n * It reached its closest point to the Sun (perihelion) on September 27, 2024, at a distance of 0.39 AU\n ' 
        '* It still reached a peak magnitude of around -4.9 in early October 2024, making it the brightest comet in over 25 years!\n ' 
        '* It was easily visible to the naked eye and presented a stunning sight with its long, wispy tail.\n * It made its closest ' 
        'approach to Earth on October 12, 2024. At that time, it was about 0.47 AU from Earth.',
        
        '67P/Churyumov-Gerasimenko': 'Comet 67P/Churyumov-Gerasimenko visited by the Rosetta spacecraft.\n' 
        '* Discovered: In 1969 by Soviet astronomers Klim Churyumov and Svetlana Gerasimenko.\n' 
        '* Type: A Jupiter-family comet, meaning its orbit is influenced by Jupiter\'s gravity.\n' 
        '* Origin: Likely from the Kuiper Belt, a region beyond Neptune populated by icy bodies.\n' 
        '* Shape: A distinctive "rubber duck" shape, consisting of two lobes connected by a narrower neck. This shape is thought to be ' 
        'the result of a collision between two smaller objects.\n' 
        '* Size: Approximately 4.3 by 4.1 km at its longest and widest dimensions.\n' 
        '* Composition: A mixture of ice, dust, and organic materials.\n' 
        '* Key dates:\n' 
        '  * Perihelion Date: August 13, 2015 (TP from current Horizons ephemeris, epoch 2015-10-10)\n' 
        '  * Orbital Period (P): 6.44 years (approximately)\n' 
        '  * Calculate the Next Perihelion Date: August 13, 2015 + 6.44 years =  Approximately February 2022.\n' 
        '  * Calculate the Next Aphelion Date: This is half the orbital period. August 13, 2015 + 3.22 years = Approximately November 2018.\n' 
        '* The Rosetta Mission: A Historic Encounter\n' 
        '  * First mission to orbit a comet nucleus.\n' 
        '  * First mission to deploy a lander (Philae) onto a comet\'s surface.\n' 
        '  * Long-term Observation: Rosetta escorted 67P for over two years, from August 2014 to September 2016, witnessing the comet\'s ' 
        'activity as it approached the Sun. This provided invaluable data on how comets evolve.\n' 
        '* Scientific Discoveries:\n' 
        '  * Water: Rosetta found that the water vapor from 67P has a different isotopic composition than Earth\'s water, suggesting ' 
        'that comets like 67P may not be the primary source of Earth\'s water.\n' 
        '  * Organics: Rosetta detected a variety of organic molecules in the comet\'s coma, including some that are considered building ' 
        'blocks of life.\n' 
        '  * Surface Features: Rosetta\'s images revealed a diverse landscape on 67P, with cliffs, craters, and even dunes.\n' 
        '  * Cometary Activity: Rosetta observed how 67P\'s activity increased as it approached the Sun, with jets of gas and dust ' 
        'erupting from its nucleus.\n' 
        '* Key Events of the Rosetta Mission\n' 
        '  * Launch: March 2, 2004\n' 
        '  * Arrival at 67P: August 6, 2014\n' 
        '  * Philae Lander Deployment: November 12, 2014. Philae\'s landing was challenging, but it did manage to send back valuable data.\n' 
        '  * Mission End: September 30, 2016. Rosetta was deliberately crashed onto the comet\'s surface. Horizons data ends 2016-10-5.\n' 
        '* Legacy: The Rosetta mission provided a wealth of data that continues to be analyzed by scientists. It has significantly advanced ' 
        'our understanding of comets, their composition, and their role in the early solar system. The mission also demonstrated the ' 
        'feasibility of complex space maneuvers and the challenges of landing on a comet.',
        
        'Borisov': 'Second interstellar object detected.',
        
        'Oumuamua': 'First known interstellar object detected passing through the Solar System.',

        '3I/ATLAS': 'The third known interstellar object detected passing through the Solar System.\n' 
        'Here\'s a summary of what we know about 3I/ATLAS (C/2025 N1):\n' 
        '* Interstellar Object: It is the third confirmed interstellar object discovered, hence its "3I/" designation. This means it \n' 
        '  originated from outside our solar system and is currently just passing through.\n' 
        '* Designations: 3I/ATLAS, Its official interstellar object designation. C/2025 N1 (ATLAS), Its official comet designation, \n' 
        '  indicating it\'s a non-periodic comet discovered in the first half of July 2025 by the ATLAS survey. A11pl3Z, Its initial, \n' 
        '  temporary designation.\n' 
        '* Trajectory: It is on a hyperbolic trajectory, confirmed by its negative semi-major axis (A = -0.25996... au). This negative \n' 
        '  value mathematically signifies an unbound orbit, meaning it will make one pass through our solar system and then escape, never \n' 
        '  to return.\n' 
        '* Perihelion: Its closest approach to the Sun (perihelion) is predicted to be around October 29, 2025, when it will be approximately \n' 
        '  1.36 to 1.4 Astronomical Units (AU) from the Sun.\n' 
        '* Discovery Data: The orbital elements and predictions for 3I/ATLAS are based on an observational data arc from June 14, 2025, to \n' 
        '  July 3, 2025. This short observational period is sufficient for astronomers to calculate its orbit and predict future events \n' 
        '  like perihelion.',        

        'ATLAS': 'Comet C/2024 G3 (ATLAS) is creating quite a buzz in the Southern Hemisphere!',        

}

    # Define positions for stellar class labels with different x positions and fonts
stellar_class_labels = [
        {
            'text': 'Supergiants', 
            'x': 0.2, 
            'y': 5.5,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Supergiants', 
            'x': 0.66, 
            'y': 5.5,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Bright Giants', 
            'x': 0.22, 
            'y': 3.7,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Bright Giants', 
            'x': 0.857, 
            'y': 3.7,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Carbon Stars', 
            'x': 0.96, 
            'y': 3.0,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Giants', 
            'x': 0.25, 
            'y': 2.25,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Giants', 
            'x': 0.83, 
            'y': 2.25,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Subgiants', 
            'x': 0.2, 
            'y': 1.0,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Subgiants', 
            'x': 0.75, 
            'y': 1.0,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Main Sequence', 
            'x': 0.4, 
            'y': 0.2, 
            'rotation': 15,
            'font': dict(color='white', size=20, family='Arial', weight='bold')  # Making this one bold as an example
        },
                {
            'text': 'Dwarfs', 
            'x': 0.77, 
            'y': -1,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'White Dwarfs', 
            'x': 0.4, 
            'y': -4.5,
            'font': dict(color='white', size=14, family='Arial')
        }
    ]

spectral_subclass_temps = {
    'O': {0: 50000, 9: 30000},    # O0 to O9
    'B': {0: 30000, 9: 10000},    # B0 to B9
    'A': {0: 10000, 9: 7500},     # A0 to A9
    'F': {0: 7500, 9: 6000},      # F0 to F9
    'G': {0: 6000, 9: 5200},      # G0 to G9
    'K': {0: 5200, 9: 3700},      # K0 to K9
    'M': {0: 3700, 9: 2400},      # M0 to M9
    'L': {0: 2400, 9: 1300},      # L0 to L9
    'T': {0: 1300, 9: 600},       # T0 to T9 (optional)
}

# Mapping of Roman numerals to luminosity class descriptions
class_mapping = {
    '0': 'Hypergiant',
    'Ia+': 'Hypergiant',
    'Ia': 'Bright Supergiant',
    'Iab': 'Intermediate Supergiant',
    'Ib': 'Less Luminous Supergiant',
    'I': 'Supergiant. The largest and most luminous stars, often nearing the end of their lives.',
    'II': 'Bright giant. Luminous stars that are smaller and less massive than supergiants.',
    'III': 'Giant. Stars that have evolved off the main sequence and expanded significantly.',
    'IV': 'Subgiant. Stars that are transitioning between the main sequence and the giant phase.',
    'V': 'Main-sequence. Stars in the prime of their lives, fusing hydrogen into helium in their cores.',
    'VI': 'Subdwarf. Stars that are smaller and less luminous than main-sequence stars of the same temperature.',
    'VII': 'White dwarf. The small, dense remnants of low- to medium-mass stars after they have exhausted their nuclear fuel.',
    'sd': 'Subdwarf',
    'D': 'White Dwarf',
}




