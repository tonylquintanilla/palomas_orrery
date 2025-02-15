# Constants Module

# Import necessary libraries

import numpy as np
from datetime import datetime, timedelta

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit

# Orbital parameters for planets and dwarf planets
# https://ssd.jpl.nasa.gov/sats/elem/

planetary_params = {
    'Mercury': {
        'a': 0.387098,  # semi-major axis in AU
        'e': 0.205630,  # eccentricity
        'i': 7.005,     # inclination in degrees
        'omega': 29.124, # argument of perihelion in degrees
        'Omega': 48.331  # longitude of ascending node in degrees
    },
    'Venus': {
        'a': 0.723332,
        'e': 0.006772,
        'i': 3.39471,
        'omega': 54.884,
        'Omega': 76.680
    },
    'Earth': {
        'a': 1.000000,
        'e': 0.016710,
        'i': 0.00005,
        'omega': 114.207,
        'Omega': -11.26064
    },
    'Mars': {
        'a': 1.523679,
        'e': 0.093400,
        'i': 1.850,
        'omega': 286.502,
        'Omega': 49.558
    },
    'Jupiter': {
        'a': 5.204267,
        'e': 0.048498,
        'i': 1.303,
        'omega': 273.867,
        'Omega': 100.464
    },
    'Saturn': {
        'a': 9.582486,
        'e': 0.054150,
        'i': 2.485,
        'omega': 339.392,
        'Omega': 113.665
    },
    'Uranus': {
        'a': 19.191263,
        'e': 0.047318,
        'i': 0.773,
        'omega': 96.998857,
        'Omega': 74.006
    },
    'Neptune': {
        'a': 30.068963,
        'e': 0.008678,
        'i': 1.770,
        'omega': 276.336,
        'Omega': 131.784
    },
    'Pluto': {
        'a': 39.482117,
        'e': 0.248808,
        'i': 17.16,
        'omega': 113.834,
        'Omega': 110.299
    },
    
    # Dwarf Planets
    'Ceres': {
        'a': 2.7675,
        'e': 0.076,
        'i': 10.593,
        'omega': 73.597,
        'Omega': 80.393
    },
    'Haumea': {
        'a': 43.13,
        'e': 0.191,
        'i': 28.20,
        'omega': 240.20,
        'Omega': 122.10
    },
    'Makemake': {
        'a': 45.79,
        'e': 0.159,
        'i': 28.01,
        'omega': 294.834,
        'Omega': 79.382
    },
    'Eris': {
        'a': 67.78,
        'e': 0.441,
        'i': 44.03,
        'omega': 150.977,
        'Omega': 35.873
    },
    'Quaoar': {
        'a': 43.325,
        'e': 0.0392,
        'i': 8.34,
        'omega': 157.631,
        'Omega': 188.809
    },
    'Sedna': {
        'a': 506.0,
        'e': 0.854,
        'i': 12.0,
        'omega': 311.286,
        'Omega': 144.546
    },
    'OR10': {  # 2007 OR10, now officially named Gonggong
        'a': 67.485,     # semi-major axis in AU
        'e': 0.503828,   # eccentricity
        'i': 30.942,     # inclination in degrees
        'omega': 207.669, # argument of perihelion in degrees
        'Omega': 336.864  # longitude of ascending node in degrees
    },

    'Orcus': {
        'a': 39.419,     # semi-major axis in AU
        'e': 0.226701,   # eccentricity
        'i': 20.573,     # inclination in degrees
        'omega': 72.400,  # argument of perihelion in degrees
        'Omega': 268.457  # longitude of ascending node in degrees
    },

    'Ixion': {
        'a': 39.648,     # semi-major axis in AU
        'e': 0.242419,   # eccentricity
        'i': 19.636,     # inclination in degrees
        'omega': 300.273, # argument of perihelion in degrees
        'Omega': 71.031   # longitude of ascending node in degrees
    },

    'MS4': {  # 2002 MS4
        'a': 41.987,     # semi-major axis in AU
        'e': 0.145843,   # eccentricity
        'i': 17.698,     # inclination in degrees
        'omega': 158.428, # argument of perihelion in degrees
        'Omega': 113.499  # longitude of ascending node in degrees
    },

    'Varuna': {
        'a': 42.947,     # semi-major axis in AU
        'e': 0.051739,   # eccentricity
        'i': 17.200,     # inclination in degrees
        'omega': 97.286,  # argument of perihelion in degrees
        'Omega': 97.286   # longitude of ascending node in degrees
    },

    'GV9': {  # 2004 GV9
        'a': 41.837,     # semi-major axis in AU
        'e': 0.083043,   # eccentricity
        'i': 21.963,     # inclination in degrees
        'omega': 292.562, # argument of perihelion in degrees
        'Omega': 173.559  # longitude of ascending node in degrees
    },

    # Asteroids
    'Vesta': {
        'a': 2.3617,
        'e': 0.089,
        'i': 7.155,
        'omega': 151.216,
        'Omega': 103.851
    },
    'Bennu': {
        'a': 1.126391,    # semi-major axis in AU
        'e': 0.203745,    # eccentricity
        'i': 6.035,       # inclination in degrees
        'omega': 66.223,  # argument of perihelion in degrees
        'Omega': 2.061    # longitude of ascending node in degrees
    },
    'Šteins': {
        'a': 2.363,      # semi-major axis in AU
        'e': 0.146,      # eccentricity
        'i': 9.944,      # inclination in degrees
        'omega': 250.97,  # argument of perihelion in degrees
        'Omega': 55.39    # longitude of ascending node in degrees
    },
    'Lutetia': {                  # Epoch 2017-10-12, heliocentric
        'a': 2.434591597038037,   # Horizons: A, semi-major axis in AU
        'e': .1644174522633922,   # Horizons: EC, eccentricity
        'i': 3.063715677953934,      # Horizons: IN, inclination in degrees
        'omega': 249.980528664283, # Horizons: W, argument of perihelion in degrees
        'Omega': 80.87713180326485   # Horizons: OM, longitude of ascending node in degrees
    },
    'Apophis': {
        'a': 0.922583,   # semi-major axis in AU
        'e': 0.191481,   # eccentricity
        'i': 3.331,      # inclination in degrees
        'omega': 126.394, # argument of perihelion in degrees
        'Omega': 204.061  # longitude of ascending node in degrees
    },    
    'Eros': {
        'a': 1.458040,   # semi-major axis in AU
        'e': 0.222868,   # eccentricity
        'i': 10.829,     # inclination in degrees
        'omega': 178.817, # argument of perihelion in degrees
        'Omega': 304.435  # longitude of ascending node in degrees
    },

    'Ryugu': {
        'a': 1.189562,   # semi-major axis in AU
        'e': 0.190349,   # eccentricity
        'i': 5.884,      # inclination in degrees
        'omega': 211.421, # argument of perihelion in degrees
        'Omega': 251.617  # longitude of ascending node in degrees
    },

    'Itokawa': {
        'a': 1.324163,   # semi-major axis in AU
        'e': 0.280164,   # eccentricity
        'i': 1.622,      # inclination in degrees
        'omega': 162.767, # argument of perihelion in degrees
        'Omega': 69.095   # longitude of ascending node in degrees
    },

    # Comets
    'Churyumov': {                  # Epoch 2015-10-10, heliocentric (500@10) and geocentric (500)
        'a': 3.462249489765068,   # Horizons: A, semi-major axis in AU
        'e': .6409081306555051,   # Horizons: EC, eccentricity
        'i': 7.040294906760007,      # Horizons: IN, inclination in degrees
        'omega': 12.79824973415729, # Horizons: W, argument of perihelion in degrees
        'Omega': 50.13557380441372   # Horizons: OM, longitude of ascending node in degrees
    },

    'Halley_geocentric': {         # Epoch 2017-10-13, geocentric -- not accurate for our plot
        'a': 3.170639037258039,   # Horizons: A, semi-major axis in AU
        'e': .1433170784128717,   # Horizons: EC, eccentricity
        'i': 3.449227641924809,      # Horizons: IN, inclination in degrees
        'omega': 188.324777427583, # Horizons: W, argument of perihelion in degrees
        'Omega': 95.24615579501011   # Horizons: OM, longitude of ascending node in degrees
    },

    'Halley': {                  # Epoch 2068-02-21, heliocentric
        'a': 17.93003431157555,   # Horizons: A, semi-major axis in AU
        'e': .9679221169240834,   # Horizons: EC, eccentricity
        'i': 162.1951462980701,      # Horizons: IN, inclination in degrees
        'omega': 112.2128395742619, # Horizons: W, argument of perihelion in degrees
        'Omega': 59.07198712310091   # Horizons: OM, longitude of ascending node in degrees
    },

#    'Moon': {                  # Epoch 2000-1-1, geocentric
#        'a': 0.002569,   # Horizons: A, semi-major axis in AU
#        'e': 0.05490,   # Horizons: EC, eccentricity
#        'i': 5.145,      # Horizons: IN, inclination in degrees
#        'omega': 318.15, # Horizons: W, argument of perihelion in degrees
#        'Omega': 125.08   # Horizons: OM, longitude of ascending node in degrees
#    },

}  

parent_planets = {
    'Moon': 'Earth',
    'Phobos': 'Mars',
    'Deimos': 'Mars',
    'Io': 'Jupiter',
    'Europa': 'Jupiter',
    'Ganymede': 'Jupiter',
    'Callisto': 'Jupiter',
    'Titan': 'Saturn',
    'Enceladus': 'Saturn',
    'Rhea': 'Saturn',
    'Dione': 'Saturn',
    'Tethys': 'Saturn',
    'Mimas': 'Saturn',
    'Phoebe': 'Saturn',
    'Miranda': 'Uranus',
    'Ariel': 'Uranus',
    'Umbriel': 'Uranus',
    'Titania': 'Uranus',
    'Oberon': 'Uranus',
    'Triton': 'Neptune',
    'Charon': 'Pluto',
    'Nix': 'Pluto',
    'Hydra': 'Pluto',
    'Dysnomia': 'Eris'
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

hover_text_sun_and_corona = (
        '<b>The Sun and Its Atmosphere</b><br><br>'
        'Visualization shows three main layers:<br>'
        '* Photosphere (surface): radius 0.00465 AU, ~6,000K<br>'
        '* Inner Corona: extends to 1.3 to 3 solar radii, >2,000,000K<br>'
        '* Outer Corona: extends to 10 to 50 solar radii, ~1,000,000K<br><br>'
        'Parker Solar Probe\'s closest approach: 8.8 solar radii<br><br>'
        'The solar corona\'s range, especially in terms of solar radii, varies significantly between periods of low and maximum<br>' 
        'solar activity. Here\'s a breakdown of the inner and outer corona\'s extent:<br>'
        '* The inner corona is the region closest to the Sun\'s surface, extending outward from the photosphere or chromosphere.<br>' 
        '  It\'s characterized by high temperatures, intense magnetic fields, and dense plasma. The inner corona typically<br>' 
        '  extends to about 1.3 to 3 solar radii (Rs) from the center of the Sun. This is a relatively consistent range that<br>' 
        '  doesn\'t change dramatically with solar activity. However, the structures within the inner corona, such as coronal<br>' 
        '  loops and streamers, will vary in size, shape, and number.<br>' 
        '* The outer corona is the very extended, tenuous region of the solar atmosphere that gradually merges with the solar<br>' 
        '  wind. It\'s less dense and cooler than the inner corona, but still incredibly hot compared to the Sun\'s surface.<br>' 
        '  The outer corona is much more variable. During solar minimum, the Sun\'s magnetic field is relatively simpler and<br>' 
        '  more dipole-like. The outer corona is less extended, typically reaching out to around 5-10 Rs. It is often<br>' 
        '  characterized by large, dark coronal holes at the poles and bright, elongated streamers near the equator. During<br>' 
        '  solar maximum, the Sun\'s magnetic field is highly complex and dynamic. The outer corona becomes much more extended<br>' 
        '  structured, reaching out to 20 Rs or even further in some cases. It is filled with numerous complex loops, streamers,<br>' 
        '  and active regions.'
        'The corona exhibits an unusual temperature inversion, with the outer atmosphere being much hotter '
        'than the surface.<br>This "coronal heating problem" is one of the key mysteries being studied by '
        'Parker Solar Probe.<br><br>'
        'Marker sizes and transparencies are scaled to represent the actual extent of each layer.'
    )

hover_text_sun = (
        '<b>Sun</b><br>'
        'Note: The Sun, our very own star, is a massive ball of hot plasma that sits at the center of our solar system.<br> ' 
        'It\'s the source of all life and energy on Earth, so I\'ve colored it chlorophyll green in our plot!<br> ' 
        '* Type: A yellow dwarf star (G-type main-sequence star).<br> ' 
        '* Age: About 4.6 billion years old, and is expected to continue its current phase for about 5 billion years<br> ' 
        'more, then evolve into a Red Giant.<br> '
        '* Diameter: Roughly 1.4 million kilometers (865,000 miles), about 109 times the diameter of Earth.<br> '
        '* Mass: About 333,000 times the mass of Earth<br> '
        '* Composition: Primarily hydrogen (about 73%) and helium (about 25%), with trace amounts of other elements.<br> '
        '* Surface Temperature: 5778 K, around 5,500 degrees Celsius, or 10,000 degrees Fahrenheit<br> '
        '* Core Temperature: Around 15 million degrees Celsius (27 million degrees Fahrenheit)<br> '
        '* Stellar Class: Main-sequence. Stars in the prime of their lives, fusing hydrogen into helium in their cores.<br> '
        '* Absolute Magnitude: 4.83<br> '
        '* Spectral Type: G2V<br> '
        '* Object Type: Star<br> '
        'The Sun is composed of several layers:<br> '
        '* Core: The innermost region where nuclear fusion occurs, converting hydrogen into helium and releasing energy.<br> '
        '* Radiative Zone: Energy from the core travels outward through this zone via radiation.<br> '
        '* Convective Zone: Energy is transported through this zone via convection (the movement of hot plasma).<br> '
        '* Photosphere: The visible surface of the Sun.<br> '
        '* Chromosphere: A thin layer above the photosphere.<br> '
        '* Corona: The outermost layer, a very hot and tenuous plasma that extends millions of kilometers into space.<br> '
        'Standard for comparison to other stars:<br> '
        '* Luminosity: 1.000000 Lsun<br> '
        '* Mass: 1.00 Msun<br> '
        '* Distance: 0 pc (0 ly)<br> '
        '* Plotting marker size: 14 px '
)

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
        'Saturn': 'rgb(210, 180, 140)',
        'Titan': 'rgb(255, 215, 0)',
        'Enceladus': 'rgb(192, 192, 192)',
        'Rhea': 'rgb(211, 211, 211)',
        'Dione': 'rgb(255, 182, 193)',
        'Tethys': 'rgb(173, 216, 230)',
        'Mimas': 'rgb(105, 105, 105)',
        'Phoebe': 'rgb(0, 0, 139)',
        'Uranus': 'rgb(173, 216, 230)',
        'Titania': 'rgb(221, 160, 221)',         
        'Oberon': 'rgb(128, 0, 128)',
        'Umbriel': 'rgb(148, 0, 211)',    
        'Ariel': 'rgb(144, 238, 144)',
        'Miranda': 'rgb(0, 128, 0)',
        'Neptune': 'rgb(0, 0, 255)',
        'Triton': 'rgb(0, 255, 255)',
        'Pluto': 'rgb(205, 92, 92)',
        'Charon': 'rgb(105, 105, 105)',
        'Haumea': 'rgb(128, 0, 128)',
        'Makemake': 'rgb(255, 192, 203)',
        'Eris': 'rgb(144, 238, 144)',
        'Voyager 1': 'white',
        'Voyager 2': 'gold',
        'Cassini': 'green',
        'Horizons': 'cyan',
        'Arrokoth': 'red',
        'Juno': 'cyan',
        'Galileo': 'white',
        'Pioneer10': 'red',
        'Pioneer11': 'green',
        'Europa': 'red',
        'OSIRIS': 'cyan',
        'Parker': 'white',
        'JWST': 'gold',
        'Rosetta': 'white',
        'Bepi': 'red',
        'Akatsuki': 'cyan',
        'Oumuamua': 'gold',
        '2024 PT5': 'green',
        'Apophis': 'red',
        'Vesta': 'cyan',
        'Bennu': 'white',
        'Lutetia': 'green',
        'Šteins': 'red',  
        'IkeyaSeki': 'green',
        'West': 'red',
        'Halley': 'cyan',
        'Hyakutake': 'white',
        'Hale-Bopp': 'gold',
        'McNaught': 'green',
        'NEOWISE': 'red',
        'Tsuchinsh': 'cyan',
        'ATLAS': 'white',
        'Churyumov': 'gold',
        'Borisov': 'red',
        'SOHO': 'white',
        'JamesWebb': 'gold',
        'Ryugu': 'gold',
        'Eros': 'green',
        'Itokawa': 'red',
        'Chang\'e': 'cyan',
        'MarsRover': 'white',
        'DART': 'gold',
        'Lucy': 'green',
        'Gaia': 'red',
        'Hayabusa2': 'cyan', 
        'Nix': 'white',        
        'Hydra': 'rgb(218, 165, 32)',  
        'Quaoar': 'rgb(244, 164, 96)',
        'Dysnomia': 'white',
        'Sedna': 'rgb(135, 206, 235)',
        'Orcus': 'rgb(0, 100, 0)',
        'Varuna': 'rgb(218, 165, 32)',
        'Ixion': 'rgb(218, 165, 32)',
        'GV9': 'rgb(128, 0, 128)',
        'MS4': 'rgb(255, 0, 0)',  
        'OR10': 'rgb(255, 255, 255)',           
    }
    return colors.get(planet, 'goldenrod')

# Dictionary mapping celestial object names to their descriptions
INFO = {
# Celestial objects
        'Sun': 'The star at the center of our solar system.',
        'Mercury': 'The smallest planet and closest to the Sun.',
        'Venus': 'Second planet from the Sun, known for its thick atmosphere.',
        'Earth': 'Our home planet, the third from the Sun.',

        'Moon': 'Earth\'s only natural satellite. The Moon\'s orbit is actually inclined by about 5.145° to the ecliptic plane, ' 
        'but approximately 28.545° to Earth\'s equatorial plane (this variation comes from Earth\'s own axial tilt of 23.4°). '
        'The Moon\'s orbital parameters are not fixed but vary significantly over time due to precession of the nodes, ' 
        'perturbations from the Sun\'s gravity, Earth\'s non-spherical shape, and other gravitational influences.',

        '2024 PT5': 'In late September 2024, Earth temporarily captured a small asteroid into its orbit, leading to it being ' 
        'dubbed Earth\'s "second moon". The object\'s official designation is 2024 PT5, but it was also referred to as a ' 
        '"mini-moon" due to its small size. \n* Size: It\'s estimated to be only about 11 meters wide, making it incredibly ' 
        'small compared to our permanent Moon.\n* Origin: It belongs to the Arjuna asteroid belt, a group of asteroids that ' 
        'share similar orbits with Earth.\n* Temporary Capture: 2024 PT5 was only temporarily captured by Earth\'s gravity. ' 
        'It entered our orbit on September 29, 2024, and is expected to depart on November 25, 2024.\n* Visibility: Due to its ' 
        'small size, it\'s not visible to the naked eye and requires powerful telescopes to be observed.\n* While 2024 PT5 is ' 
        'not a permanent addition to our celestial neighborhood, its temporary presence provided scientists with a valuable ' 
        'opportunity to study near-Earth objects and learn more about the dynamics of our solar system.\n* Plot 2024 PT5 with' 
        'Earth as the center to see its close approach and also with the Sun as the center to see its orbit near Earth\'s.',

        'Mars': 'Known as the Red Planet, fourth planet from the Sun.',
        'Phobos': 'The larger and closer of Mars\'s two moons, spiraling inward towards Mars.',
        'Deimos': 'The smaller and more distant moon of Mars, with a stable orbit.',
        'Ceres': 'The largest object in the asteroid belt, considered a dwarf planet.',
        'Apophis': 'Near-Earth asteroid with a close approach in 2029.',
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
        'Itokawa': 'Asteroid visited by the original Hayabusa mission.',
        'Jupiter': 'The largest planet in our solar system, famous for its Great Red Spot.',
        'Io': 'Jupiter moon. The most volcanically active body in the Solar System.',
        'Europa': 'Jupiter moon. Covered with a smooth ice layer, potential subsurface ocean.',
        'Ganymede': 'Jupiter moon. The largest moon in the Solar System, bigger than Mercury.',
        'Callisto': 'Jupiter moon. Heavily cratered and geologically inactive.',
        'Saturn': 'Known for its beautiful ring system, the sixth planet from the Sun.',
        'Titan': 'Saturn moon. The second-largest moon in the Solar System, with a thick atmosphere.',
        'Enceladus': 'Saturn moon. Known for its geysers ejecting water ice and vapor.',
        'Rhea': 'Saturn moon. Saturn\'s second-largest moon, with extensive cratered surfaces.',
        'Dione': 'Saturn moon. Features wispy terrains and numerous craters.',
        'Tethys': 'Saturn moon. Notable for its large Ithaca Chasma canyon.',
        'Mimas': 'Saturn moon. Known for the large Herschel Crater, resembling the Death Star.',
        'Phoebe': 'Saturn moon. An irregular moon with a retrograde orbit around Saturn.',
        'Uranus': 'The ice giant with a unique tilt, orbits the Sun on its side.',
        'Titania': 'Uranus moon. The largest moon of Uranus, with a mix of heavily cratered and relatively younger regions.',    
        'Oberon': 'Uranus moon. The second-largest moon of Uranus, heavily cratered.',
        'Umbriel': 'Uranus moon. Features a dark surface with numerous impact craters.',  
        'Ariel': 'Uranus moon. Exhibits a mix of heavily cratered regions and younger surfaces.',
        'Miranda': 'Uranus moon. Known for its extreme geological features like canyons and terraced layers.',
        'Neptune': 'The eighth and farthest known planet in the solar system.',
        'Triton': 'Neptune\'s largest moon, has a retrograde orbit and geysers suggesting geological activity.',
        'Pluto': 'Once considered the ninth planet, now classified as a dwarf planet.',
        'Charon': 'Pluto\'s largest moon, forming a binary system with Pluto.',
        'Nix': 'One of Pluto\'s moons.',
        'Hydra': 'Another of Pluto\'s moons',
        'Haumea': 'A dwarf planet known for its elongated shape and fast rotation.',
        'Makemake': 'A dwarf planet located in the Kuiper Belt, discovered in 2005.',
        'Eris': 'A distant dwarf planet, more massive than Pluto.',
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

        'Varuna': 'A significant Kuiper Belt Object with a rapid rotation period.',
        'Ixion': 'A significant Kuiper Belt Object without a known moon.',
        'GV9': 'A binary Kuiper Belt Object providing precise mass measurements through its moon.',
        'MS4': 'A large unnumbered Kuiper Belt Object with no known moons.',  
        'OR10': 'One of the largest known Kuiper Belt Objects with a highly inclined orbit.',
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
        '* Arrokoth (2014 MU69) flyby on January 1, 2019, at 05:35 UTC, as close as 3561 km, or 0.0000238015 AU if you plot it.\n' 
        '* Scientific Instruments: New Horizons carries a suite of scientific instruments, including cameras, spectrometers, and ' 
        'plasma analyzers, to study the composition, atmosphere, and environment of Pluto and other Kuiper Belt objects.\n' 
        '* Continuing Mission: New Horizons is still traveling through the Kuiper Belt, and NASA may extend its mission to explore ' 
        'other distant objects in the future.',

        'Arrokoth': 'Arrokoth is the most distant object ever visited by a spacecraft, New Horizons, on January 1, 2019.\n' 
        '***NOTE: ARROKOTH DOES NOT PLOT WITH THE SUN AS THE CENTER BODY. TO VISUALIZE IT, SELECT ARROKOTH AS THE CENTER BODY AND PLOT ' 
        'ARROKOTH AND THE "NEW HORIZONS" CRAFT ON DATE 2019-1-1 5:35 UTC, THE TIME OF CLOSEST APPROACH. SEE JPL HORIZONS FOR AN ' 
        'EXPLANATION. TO VISUALIZE ITS LOCATION IN THE SOLAR SYSTEM, PLOT THE ABOVE WITH THE SUN AS THE CENTER BODY, YOU WILL SEE THE NEW ' 
        'HORIZONS CRAFT, BUT NOT ARROKOTH, HOWEVER, ON 2019-1-1, THIS IS THE LOCATION OF ARROKOTH.***\n'
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
        '  * Jupiter Arrival and Orbit Insertion on July 4, 2016\n'
        '  * Extended Mission Start on August 1, 2021\n' 
        '  * First Ganymede Flyby on June 7, 2021\n'
        '  * First Europa Flyby on September 29, 2022\n' 
        '  * First Io Flyby on December 30, 2023\n'
        '  * End of Mission on September 2025 or end of spacecraft life\n'
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
        
        'Gaia': 'European Space Agency mission at L2 mapping the Milky Way.',
        
        'Hayabusa 2': 'Japan JAXA mission that returned samples from Ryugu.', 
        
        'Chang\'e': 'China\'s lunar exploration program.',
        
        'Perseverance Mars Rover': 'The Perseverance Rover is NASA\'s Mars rover and Ingenuity helicopter. The NASA Mars Perseverance mission ' 
        'is a robotic space mission currently underway, aimed at exploring the planet Mars and searching for signs of ancient ' 
        'microbial life.\n'
        '* Objective: To investigate the habitability of Mars in the ancient past, search for evidence of past microbial life, collect ' 
        'and store Martian rock and soil samples for future return to Earth, and test technologies for future human exploration of Mars.\n' 
        '* Launch Date: July 30, 2020\n'
        '* Landing Date: February 18, 2021, at 20:55 UTC.\n'
        '* Perseverance\'s Journey: Perseverance, along with Ingenuity, was housed within a protective aeroshell during its journey ' 
        'to Mars. This aeroshell helped protect the rover and helicopter during the high-speed entry into Mars\' atmosphere.\n' 
        '* Landing on Mars: During the landing process, the aeroshell separated, and Perseverance used a parachute and a "sky crane" ' 
        'system to gently lower itself onto the Martian surface. The sky crane then detached and flew away to a safe distance before crashing.\n'
        '* Landing Site: Jezero Crater, a former lake basin believed to be a promising location for finding evidence of past life.\n'
        '* Landing elevation: Jezero Crater is located in a depression on Mars.\n' 
        '  * Its floor lies about 2,600 meters below the "Mars Areoid," which is a reference level similar to sea level on Earth.\n' 
        '  * Subtract Jezero\'s elevation from Mars\' average radius: 3,389,500 meters - 2,600 meters = 3,386,900 meters.\n' 
        '  * Convert to AU: Divide the distance to Jezero\'s center by the number of meters in 1 AU: 3,386,900 meters / 149,597,870,700 '
        'meters/AU ≈ 0.00002264 AU. This is very close to the "Distance from center" value reported by Horizons in the plot ' 
        '(0.00002267 AU) starting February 18, 21:00, which corresponds to the landing time of 20:55 UTC.\n'
        '* "Orbit": The apparent "orbit" around Mars in the plot is just the Perseverance lander rotating with Mars on the surface.\n' 
        '* Rover: Perseverance, a six-wheeled, car-sized rover equipped with advanced scientific instruments.\n' 
        '* Helicopter: Ingenuity, a small, experimental helicopter that demonstrated the first powered flight on another planet. ' 
        'Ingenuity\'s mission has recently ended due to damage sustained during a landing.\n' 
        '* Search for past life: Perseverance is equipped with instruments designed to detect chemical and mineral biosignatures, ' 
        'as well as examine the geological context of potential past life.\n' 
        '* Sample collection: The rover has a drill and sample caching system to collect and store samples of Martian rock and soil ' 
        'for future return to Earth. These samples could provide invaluable insights into the history of Mars and the potential for ' 
        'life beyond Earth.\n' 
        '* Technology demonstration: Perseverance is testing technologies that could be used for future human exploration of Mars, ' 
        'such as a system for producing oxygen from the Martian atmosphere.\n' 
        '* Status: As of February 2025, Perseverance is still active on Mars, continuing its exploration of Jezero Crater and ' 
        'collecting samples. The mission is expected to continue for several more years, and the collected samples are planned to ' 
        'be returned to Earth in the 2030s through a joint mission with the European Space Agency.',
        
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
        
        'Lucy': 'The NASA Lucy mission exploring Trojan asteroids around Jupiter.\n* The Lucy mission ' 
        'is a groundbreaking NASA space probe that\'s on an ambitious journey to explore the Trojan asteroids, a unique population ' 
        'of asteroids that share Jupiter\'s orbit around the Sun. These "Trojan swarms" are like fossils of our early solar system, ' 
        'holding clues to the formation of the planets and the conditions that existed billions of years ago. \n* Lucy will visit a ' 
        'total of eight asteroids. Main Belt Asteroids: 52246 Donaldjohanson; 152830 Dinkinesh. Trojan Asteroids: 3548 Eurybates ' 
        '(and its satellite Queta); 15094 Polymele; 11351 Leucus; 21900 Orus; 617 Patroclus (and its binary companion Menoetius).',

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
        'to encounter a comet, providing close-up images and data about its nucleus and composition. Halley\'s Comet reached perihelion on February 9th, 1986.\n'  
        '  * Halley\'s Comet reached aphelion most recently on December 9th, 2023.\n' 
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

gravitational_influence_info = (
            "The Sun's Gravitational Influence:<br><br>" 

            "The Solar System\'s extent is actually defined in multiple ways. The Heliopause (120-123 AU):<br>" 
            "Where the solar wind meets interstellar space.<br><br>" 

            "Gravitational influence extends much further, including, Sedna\'s orbit (936 AU), the Hills Cloud/Inner<br>" 
            "Oort Cloud (2,000-20,000 AU), and the Outer Oort Cloud (20,000-100,000 AU). The Sun's gravitational influence<br>" 
            "extends to about 2 light-years (~126,000 AU).<br><br>" 
            
            "While the Heliopause marks where the Sun\'s particle influence ends, its gravitational influence extends much<br>" 
            "further. Sedna and other distant objects remain gravitationally bound to the Sun despite being well beyond<br>" 
            "the Heliopause. This is why astronomers generally consider the Oort Cloud (and objects like Sedna) to be part<br>" 
            "of our Solar System, even though we've never directly observed the Oort Cloud. The distinction comes down to<br>" 
            "different types of influence:<br>" 
            "* Particle/plasma influence (solar wind) → ends at Heliopause;<br>" 
            "* gravitational influence → extends much further, including Sedna and the theoretical Oort Cloud.<br><br>" 
            
            "So the Solar System is generally considered to extend at least as far as these gravitationally bound objects,<br>" 
            "even beyond the Heliopause. Sedna is one of our first glimpses into this very distant region that may connect<br>" 
            "to the Oort Cloud population."
        )

outer_oort_info = (
            "Outer Oort Cloud:<br><br>"
            
            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the<br>" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.<br><br>"

            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.<br>" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital<br>" 
            "periods exceeding 200 years.<br><br>" 

            "Oort Cloud's Outer Edge: At 100,000 AU, it's about 1.58 light-years from the Sun, placing it just<br>" 
            "beyond the nearest star systems and marking the boundary between the Solar System and interstellar space.<br><br>" 

            "The Outer Oort Cloud is the primary source of long-period comets. Objects here are more loosely bound and more<br>" 
            "susceptible to external gravitational perturbations."
        )

inner_oort_info = (
            "Inner Oort Cloud:<br><br>"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the<br>" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.<br>" 
            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.<br>" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital<br>" 
            "periods exceeding 200 years.<br><br>" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the<br>" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an<br>" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

inner_limit_oort_info = (
            "Inner Limit of the Oort Cloud:<br><br>"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the<br>" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.<br>" 
            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.<br>" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital<br>" 
            "periods exceeding 200 years.<br><br>" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the<br>" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an<br>" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

solar_wind_info = (
            "Solar Wind Heliopause:<br><br>"

            "The heliosphere is a vast, bubble-like region of space that surrounds the Sun and its planets. It's created by the<br>" 
            "solar wind, a constant stream of charged particles flowing out from the Sun.<br>" 
            "* Solar Wind: The solar wind is the driving force behind the heliosphere. It consists mostly of protons and electrons,<br>" 
            "  along with heavier elements in smaller numbers. These particles are accelerated to high speeds by the Sun's heat and<br>" 
            "  then escape its gravity, flowing out into space.<br>" 
            "* Shape: The heliosphere isn't perfectly spherical. It's more like a long, teardrop shape with a rounded head and a<br>" 
            "  flowing tail. This shape is due to the Sun's movement through the interstellar medium, the gas and dust that fills the<br>" 
            "  space between stars.<br><br>" 
            
            "Boundaries: The heliosphere has a few distinct boundaries:<br>" 
            "* Termination Shock: This is where the solar wind abruptly slows down as it encounters the interstellar medium.<br>" 
            "* Heliosheath: This is the turbulent region beyond the termination shock, where the solar wind mixes with the interstellar medium.<br>" 
            "* Heliopause: This is the outermost boundary of the heliosphere, where the solar wind's pressure is balanced by the pressure of<br>" 
            "  the interstellar medium. It's considered the true \"edge\" of our solar system.<br>" 
            "* Protective Shield: The heliosphere acts as a protective bubble, shielding the planets within it from harmful galactic cosmic<br>" 
            "  radiation. This radiation comes from outside our solar system and can be dangerous to life.<br>" 
            "* Influence on Planets: The heliosphere also influences the planets within it. It interacts with planetary magnetic fields,<br>" 
            "  creating phenomena like auroras. It can also affect the atmospheres of planets without strong magnetic fields.<br><br>"   
                         
            "Voyager Missions: Our most valuable information about the heliosheath comes from the Voyager 1 and Voyager 2 spacecraft,<br>" 
            "which have been traveling through space since 1977. Both probes have crossed the termination shock and are currently<br>" 
            "exploring the heliosheath, sending back valuable data about this mysterious region. Voyager 1 encountered the Heliopause<br>" 
            "at ~123 AU. This is considered the end of the Sun's influence and the start of interstellar space.<br><br>" 
            
            "* The heliosheath extends from ~120 to 150 AU at the Heliopause.<br>"
            "* Temperature: ~1,000,000K on average.<br>"
            "* Black body radiation at 2.897 nm falls within the X-ray region of the electromagnetic spectrum, which is invisible to the human eye."
        )

termination_shock_info = (
            "Solar Wind Termination Shock:<br><br>"

            "The Solar Wind Termination Shock extends from about 75 to 100 AU.<br><br>"

            "The Termination Shock is the region where the solar wind slows down from<br>"
            "supersonic to subsonic speeds due to interaction with the interstellar<br>"
            "medium. The kinetic energy transfers into heat, increasing abruptly.<br><br>"

            "Voyager 1 encountered the Termination Shock at 94 AU, while Voyager 2 at 84 AU.<br>"
            "After the Termination Shock the speeds slow down to ~100 to 200 km/s."
        )

outer_corona_info = (
            "Sun: Outer Corona:<br><br>"

            "Solar Outer Corona extends to 50 solar radii or more,  about 0.2 AU. It is the most tenuous and expansive layer of<br>" 
            "the solar atmosphere. The solar Corona generates the solar wind, a stream of electrons, protons, and Helium travelling<br>" 
            "at supersonic speeds between 300 and 800 km/s, and temperatures to 2M K. The high temperature of the corona causes these<br>" 
            "particles to escape the Sun's gravity. This extreme heat is a bit of a mystery, as it's much hotter than the Sun's surface.<br>"
            "Scientists believe that magnetic fields and nanoflares, small explosions on the Sun's surface, play a role in heating the corona.<br><br>"   

            "The outer corona is characterized by various structures, including streamers, loops, and plumes, which are shaped by the<br>" 
            "Sun's magnetic field. These structures are constantly changing and evolving. The outer corona plays a crucial role in<br>" 
            "space weather. Solar flares and coronal mass ejections, which originate in the corona, can disrupt Earth's magnetic field<br>" 
            "and affect satellites, communication systems, and power grids.<br><br>"

            "* Temperature: ~2-3M K, or an average of 2.5M K.<br>" 
            "* The Outer Corona radiates at an average wavelength of 1.159 nm, which falls within the extreme ultraviolet to X-ray<br>" 
            "  regions of the electromagnetic spectrum."
        )

inner_corona_info = (
            "Sun: Inner Corona:<br><br>"

            "The solar inner corona is the region of the Sun's atmosphere that lies closest to its surface. It's a dynamic and complex<br>" 
            "environment, with temperatures reaching millions of degrees Celsius and a variety of fascinating features:<br>"
            "* Temperature: While still incredibly hot (around 1-3 million Kelvin), the inner corona is slightly cooler<br>" 
            "than the outer corona. This temperature difference is one of the factors that drives the solar wind.<br>"
            "* Density: The inner corona is denser than the outer corona, but still much less dense than the Sun's surface,<br>" 
            "the photosphere. This low density makes it difficult to observe directly, except during a solar eclipse or<br>" 
            "with specialized instruments.<br><br>" 
            
            "Magnetic field: The inner corona is dominated by the Sun's magnetic field, which shapes and controls the<br>" 
            "plasma in this region. The magnetic field lines create a variety of structures, including:<br>" 
            "* Coronal loops: These are closed loops of magnetic flux that trap hot plasma, forming bright arcs that<br>" 
            "  can be seen in ultraviolet and X-ray images.<br>" 
            "* Coronal holes: These are areas where the magnetic field lines are open, allowing plasma to escape into<br>" 
            "  space and contribute to the solar wind.<br>" 
            "* Streamers: These are large, elongated structures that extend outward from the Sun, often associated with<br>" 
            "  active regions and coronal mass ejections (CMEs).<br>" 
            "* Dynamic activity: The inner corona is a constantly changing environment, with features evolving and erupting<br>" 
            "  on different timescales. This activity is driven by the interplay between the magnetic field and the plasma,<br>" 
            "  leading to phenomena like:<br>" 
            "  * Solar flares: These are sudden, intense bursts of energy and radiation caused by the release of magnetic energy.<br>" 
            "  * CMEs: These are massive eruptions of plasma and magnetic field from the corona, which can travel through space<br>" 
            "    and impact Earth, disrupting satellites, communication systems, and power grids.<br><br>"
            
            "* Solar Inner Corona (extends to 2-3 solar radii, ~0.014 AU)<br>"
            "* Temperature: 1-2M K, or an average of about 1.5M K<br>"
            "* It radiates at an average wavelenght of 1.93 nm, within the extreme ultraviolet to soft X-ray regions."
        )

chromosphere_info = (
            "Sun: Chromosphere:<br><br>"

            "The chromosphere is a dynamic and visually stunning layer of the Sun's atmosphere, sandwiched between the<br>" 
            "photosphere (the visible surface) and the corona (the outermost layer). It's a region of dramatic temperature<br>" 
            "changes, intricate structures, and energetic events.<br><br>"
             
            "* The chromosphere is relatively thin, extending only about 2,000 kilometers (1,200 miles) above the photosphere.<br>" 
            "  It's also much less dense than the photosphere.<br>" 
            "* The temperature in the chromosphere increases dramatically with altitude, from around 4,000 Kelvin at the<br>" 
            "  photosphere to about 20,000 Kelvin at the inner corona.<br>" 
            "* The chromosphere gets its name from the Greek word \"chroma,\" meaning color, because of its reddish appearance.<br>" 
            "  This color is primarily due to the strong emission of light from hydrogen atoms<br>" 
            "* The chromosphere is a constantly changing environment, with a variety of features that evolve and erupt on<br>" 
            "  different timescales:<br>" 
            "  * Spicules: These are jet-like eruptions of plasma that rise and fall like geysers, covering the chromosphere<br>" 
            "    in a dynamic, \"grass-like\" pattern.<br>" 
            "  * Filaments and prominences: These are large, cool, dense structures of plasma suspended in the chromosphere<br>" 
            "    and corona by magnetic fields. When seen against the bright disk of the Sun, they appear as dark filaments.<br>" 
            "    When seen extending beyond the Sun's edge, they appear as bright prominences.<br>" 
            "  * Plages: These are bright regions in the chromosphere associated with active regions, where magnetic fields<br>" 
            "    are concentrated.<br><br>" 
             
            "* Radius: from Photosphere to 1.5 Solar radii or ~0.00465 - 0.0070 AU<br>"
            "* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K<br>"
            "* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible."
        )

photosphere_info = (
            "Sun: Photosphere<br><br>"

            "Solar Convective Zone and Photosphere, the visible surface.<br>"
            "* The photosphere is the visible surface of the Sun. It's a relatively thin layer, only about 500 kilometers thick.<br>" 
            "* Including both the Convective Zone and the Photosphere, the radius is from 0.7 to 1 Solar radii, or about 0.00465 AU.<br>"
            "* Temperature: from 2M K at the Radiative Zone to ~5,500K at the Photosphere.<br>"
            "* Convection transports energy to the visible \"surface\" of the Sun. The convection process starts at the Radiative Zone<br>"
            "* At the Photosphere, the energy is radiated as visible light. Radiation emits at a peak wavelength at 527.32 nm, which<br>" 
            "  is in the green spectrum. The Sun's emitted light is a combination of all visible wavelengths, resulting in a yellowish-white color.<br><br>"
             
            "* The photosphere is cooler than the Sun's core and the layers above it, but still hot enough to make the photosphere glow brightly.<br>" 
            "* To the naked eye, the photosphere appears as a smooth, yellow disk. However, closer observations reveal a variety of features, including:<br>" 
            "  * Granulation: This is a pattern of small, bright cells surrounded by darker boundaries, caused by convection<br>" 
            "    currents bringing hot plasma up from the Sun's interior.<br>" 
            "  * Sunspots: These are dark, cooler regions on the photosphere caused by strong magnetic fields. They can be<br>" 
            "    larger than Earth and last for days or weeks.<br>" 
            "  * Faculae: These are bright regions surrounding sunspots, also associated with magnetic fields.<br>" 
            "  * Energy transport: The photosphere is where the Sun's energy, generated in its core through nuclear fusion,<br>" 
            "    is finally released as light. This energy has traveled outward through the Sun's interior in the form of<br>" 
            "    radiation and convection, and it's in the photosphere that it transitions to primarily radiation, allowing it<br>" 
            "    to escape into space.<br>" 
            "  * Spectrum: The photosphere emits a continuous spectrum of light, which includes all colors of the rainbow.<br>" 
            "  * Solar activity: The photosphere is also where many solar activity events originate, such as:<br>" 
            "    * Solar flares: These are sudden, intense bursts of energy and radiation caused by the release of magnetic<br>" 
            "      energy in the solar atmosphere.<br>" 
            "    * Coronal mass ejections (CMEs): These are massive eruptions of plasma and magnetic field from the Sun's corona,<br>" 
            "      often associated with flares.<br>"
            "    * Solar activity events originating in the photosphere can affect Earth's magnetic field and disrupt satellites,<br>" 
            "      communication systems, and power grids.<br><br>"
        )

radiative_zone_info = (
            "Sun: Radiative Zone<br><br>"

            "The Solar Radiative Zone extends from about 0.2 to 0.7 solar radii, about 0.00325 AU. Temperature ranges from about<br>" 
            "7M K near the core to about 2M K near the convective zone. Energy is transported by radiative diffusion, through photon<br>" 
            "absorption and re-emission.<br><br>"

            "The radiative zone is a vast region within the Sun, located between the core and the convective zone. It's a place<br>" 
            "of intense heat and density, where energy generated in the core slowly makes its way outward in the form of photons.<br>"  
            "* Density: The density also decreases with distance from the core, but it remains much denser than the convective zone above it.<br><br>" 
            "* Energy transport: The primary mode of energy transport in the radiative zone is radiative diffusion. Photons<br>" 
            "  generated in the core through nuclear fusion undergo countless absorptions and re-emissions as they interact<br>" 
            "  with the dense plasma. This process is incredibly slow, and it can take millions of years for a photon to travel<br>" 
            "  from the core to the outer edge of the radiative zone.<br>" 
            "* Opacity: The radiative zone is highly opaque, meaning that photons can only travel a short distance before being<br>" 
            "  absorbed or scattered. This high opacity is due to the high density and the presence of heavy elements, which are<br>" 
            "  more efficient at absorbing and scattering radiation.<br>" 
            "* Energy transfer: The radiative zone plays a crucial role in transferring energy from the Sun's core to its outer<br>" 
            "  layers. Without it, the Sun would not be able to shine.<br>" 
            "* Stability: The slow and gradual energy transport in the radiative zone helps to maintain the Sun's overall stability.<br>" 
            "* Helioseismology: This technique uses observations of sound waves traveling through the Sun to probe its interior<br>" 
            "  structure, including the radiative zone. By analyzing the frequencies and patterns of these waves, scientists can<br>" 
            "  infer the temperature, density, and composition of the radiative zone.<br>" 
            "* Neutrino observations: Neutrinos are subatomic particles produced in the Sun's core that can pass through the<br>" 
            "  radiative zone almost unimpeded. By detecting and analyzing these neutrinos, scientists can gain information about<br>" 
            "  the nuclear reactions taking place in the core and the conditions in the radiative zone."
            )

core_info = (
            "Solar Core<br><br>"

            "The Sun's core is where the Sun's energy is generated through nuclear fusion, providing the light and heat that sustain life on Earth:<br>" 
            "* Location: The core is located at the very center of the Sun, extending outward to about 25% of the Sun's radius.<br>" 
            "* Size: While relatively small compared to the Sun's overall size, the core contains about 34% of the Sun's total mass.<br>" 
            "* Temperature: The core is the hottest place in the solar system, with temperatures reaching 15 million Kelvin<br>" 
            "* Density: The core is incredibly dense, about 150 times denser than water. This extreme density is due to the<br>" 
            "  immense pressure exerted by the Sun's outer layers.<br>" 
            "* Composition: The core is primarily composed of hydrogen (about 34% by mass) and helium (about 64% by mass).<br>" 
            "  Trace amounts of heavier elements are also present.<br><br>"
              
            "The dominant fusion process in the Sun's core is the proton-proton chain reaction:<br>" 
            "* Two protons, hydrogen nuclei, collide and fuse to form a deuterium nucleus releasing a positron and a neutrino.<br>" 
            "* The deuterium nucleus collides with another proton to form a helium-3 nucleus, releasing a gamma ray.<br>" 
            "* Two helium-3 nuclei collide to form a helium-4 nucleus, releasing two protons.<br>" 
            "* This process converts a small amount of mass into a tremendous amount of energy<br><br>" 
            
            "The energy generated in the core is transported outward through the Sun in two ways:<br>"
            "* Radiative zone: The energy first travels through the radiative zone, where it is carried by photons that undergo<br>" 
            "  countless absorptions and re-emissions. This process is very slow, taking millions of years for energy to travel<br>" 
            "  from the core to the outer edge of the radiative zone.<br>" 
            "* Convective zone: Once the energy reaches the convective zone, it is transported by convection currents, where hot<br>" 
            "  plasma rises and cooler plasma sinks. This is a much faster process, taking only a few weeks for energy to reach<br>" 
            "  the Sun's surface.<br><br>" 
            
            "* Helioseismology: By analyzing sound waves traveling through the Sun, scientists can infer the conditions in the core,<br>" 
            "  such as its temperature, density, and composition.<br>" 
            "* Neutrino observations: Neutrinos produced in the core can pass through the Sun almost unimpeded, providing direct<br>" 
            "  information about the nuclear reactions taking place there." 
            )