# Constants Module

# Import necessary libraries

import numpy as np
from datetime import datetime, timedelta

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit

# Orbital parameters for planets and dwarf planets
planetary_params = {
    # Planets
    'Mercury': {'a': 0.387, 'e': 0.2056, 'i': np.radians(7.005)},
    'Venus': {'a': 0.723, 'e': 0.0068, 'i': np.radians(3.39471)},
    'Earth': {'a': 1.000000, 'e': 0.016710, 'i': np.radians(0.00005)},
    'Mars': {'a': 1.523679, 'e': 0.0934, 'i': np.radians(1.850)},
    'Jupiter': {'a': 5.204, 'e': 0.0489, 'i': np.radians(1.303)},
    'Saturn': {'a': 9.537, 'e': 0.0565, 'i': np.radians(2.485)},
    'Uranus': {'a': 19.191, 'e': 0.0472, 'i': np.radians(0.773)},
    'Neptune': {'a': 30.07, 'e': 0.0086, 'i': np.radians(1.770)},
    'Pluto': {'a': 39.48, 'e': 0.2488, 'i': np.radians(17.16)},
    
    # Dwarf Planets
    'Ceres': {'a': 2.7675, 'e': 0.076, 'i': np.radians(10.593)},
    'Haumea': {'a': 43.13, 'e': 0.191, 'i': np.radians(28.20)},
    'Makemake': {'a': 45.79, 'e': 0.159, 'i': np.radians(28.01)},
    'Eris': {'a': 67.78, 'e': 0.441, 'i': np.radians(44.03)},
    'Quaoar': {'a': 43.325, 'e': 0.0002, 'i': np.radians(8.34)},
    'Sedna': {'a': 506, 'e': 0.854, 'i': np.radians(12.0)},

        # Asteroids
    'Vesta': {'a': 2.3617, 'e': 0.089, 'i': np.radians(7.155)},
    'Pallas': {'a': 2.7726, 'e': 0.231, 'i': np.radians(34.792)},
    'Hygiea': {'a': 3.1386, 'e': 0.176, 'i': np.radians(3.100)},
    'Eunomia': {'a': 2.665, 'e': 0.185, 'i': np.radians(11.834)},

    # Moons
    'Moon': {'a': 0.00257, 'e': 0.0549, 'i': np.radians(5.145)},  # Earth's Moon
    'Phobos': {'a': 0.000062, 'e': 0.0151, 'i': np.radians(1.093)},  # Mars' Phobos
    'Deimos': {'a': 0.000156, 'e': 0.0002, 'i': np.radians(0.93)},  # Mars' Deimos
    'Io': {'a': 0.00282, 'e': 0.0041, 'i': np.radians(0.036)},  # Jupiter's Io
    'Europa': {'a': 0.00449, 'e': 0.0094, 'i': np.radians(0.466)},  # Jupiter's Europa
    'Ganymede': {'a': 0.00716, 'e': 0.0013, 'i': np.radians(0.177)},  # Jupiter's Ganymede
    'Callisto': {'a': 0.01258, 'e': 0.0074, 'i': np.radians(0.192)},  # Jupiter's Callisto
    'Titan': {'a': 0.00817, 'e': 0.0288, 'i': np.radians(0.348)},  # Saturn's Titan
    'Enceladus': {'a': 0.00124, 'e': 0.0047, 'i': np.radians(0.0003)},  # Saturn's Enceladus
    'Rhea': {'a': 0.00354, 'e': 0.0014, 'i': np.radians(0.001)},  # Saturn's Rhea
    'Dione': {'a': 0.00219, 'e': 0.0013, 'i': np.radians(0.002)},  # Saturn's Dione
    'Tethys': {'a': 0.00195, 'e': 0.0002, 'i': np.radians(0.002)},  # Saturn's Tethys
    'Mimas': {'a': 0.00098, 'e': 0.0002, 'i': np.radians(0.007)},  # Saturn's Mimas
    'Phoebe': {'a': 0.02602, 'e': 0.0964, 'i': np.radians(179.73)},  # Saturn's Phoebe (retrograde)
    'Oberon': {'a': 0.00177, 'e': 0.0015, 'i': np.radians(0.157)},  # Uranus' Oberon
    'Umbriel': {'a': 0.00128, 'e': 0.0012, 'i': np.radians(0.162)},  # Uranus' Umbriel
    'Ariel': {'a': 0.00091, 'e': 0.0003, 'i': np.radians(0.037)},  # Uranus' Ariel
    'Miranda': {'a': 0.00048, 'e': 0.0014, 'i': np.radians(0.009)},  # Uranus' Miranda
    'Titania': {'a': 0.00275, 'e': 0.0016, 'i': np.radians(0.011)},  # Uranus' Titania
    'Triton': {'a': 0.00361, 'e': 0.0001, 'i': np.radians(157.86)},  # Neptune's Triton (retrograde)
    'Charon': {'a': 0.00121, 'e': 0.0003, 'i': np.radians(0.0)},  # Pluto's Charon    
    
    # Comets
#    'Halley': {'a': 17.834, 'e': 0.96714, 'i': np.radians(162.26)},
#    'Oumuamua': {'a': -1.275, 'e': 1.2, 'i': np.radians(122.7)},  # Hyperbolic orbit
#    'Churyumov-Gerasimenko': {'a': 3.463, 'e': 0.6405, 'i': np.radians(7.0405)},
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
    'Oberon': 'Uranus',
    'Umbriel': 'Uranus',
    'Ariel': 'Uranus',
    'Miranda': 'Uranus',
    'Titania': 'Uranus',
    'Triton': 'Neptune',
    'Charon': 'Pluto'
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
    "to plot actual positions of objects. Idealized orbits of the planets are calculated from orbital data from Horizons, " 
    "but are only approximate. Explore! \n\n" 

    "In addition to the solar system, you can also create 2D and 3D plots of our stellar neighborhood. There are four ways to do this: "
    "by distance in light-years or by brightness as apparent magnitude, and in both modes in a 2D or a 3D plot.\n\n"

    "You can plot our stellar neighborhood up to 100 light-years away in 2D and 3D, with a user defined entry in light-years.\n\n" 

    "The other way of selecting stars is by apparent magnitude. This "
    "method also plots 2D or 3D, but the star selection is quite different. Instead of seeing all stars within a certain distance from the Sun "
    "you see all stars visible to the unaided eye up to a certain apparent, or visual magnitude, meaning how bright they appear, which " 
    "is a function of how luminous they are and their distance from us.\n\n" 

    "The 3D plot is just that, you will "
    "see stars plotted relative to the Sun in their actual positions, up to the selected distance in light-years, or up to the selected "
    "apparent magnitude, regardless of the distance. In fact, you will begin to see the shape and tilt of the galaxy! You can also " 
    "use a drop down menu of bright stars and Messier Objects that are plotted, which will allow you to point to that object!\n\n"
    
    "You can also see in all plots the hovertext with the stars' information, in some cases in detail as I add it.\n\n"  
    
    "The 2D plot is the classic Hertzprung-Russell diagram of stars plotted by "
    "luminosity, or absolute magnitude, meaning how intrinsically bright the star is, and temperature, which is related to the star's "
    "spectral class and color. This is a more scientific plot that reveals a lot about the "
    "kind of stars they are, and their place in stellar evolution.\n\n" 

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
    "While nearer, fainter stars, may not be plotted at all, for example White Dwarfs. In fact, the greater the apparent magnitude " 
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
    "Obviously it's not the Sun's actual color, which is in the yellow-orange range.\n\n"

    "Solar System Objects:\nThe Solar sytem object selection menu is scrollable. Select the objects to plot.\n\n"  

    "Data availability is limited for space missions and comets. "
    "Objects will only be plotted on dates the data is available. "
    "For space missions and comets, be careful to enter a start date and number of days, weeks, months or years to plot that are " 
    "within the timeframes of all the objects to plot to avoid plotting errors. "
    "For dates beyond 2199-12-29, the Horizons system does not provide data for most objects. " 
    "Objects like Dwarf Planet Sedna have orbital periods that are thousands of years long so the orbit will only plot partially. " 
    "This is also the case for Dwarf Planet Pluto!\n\n"

    "Idealized orbits are only displayed where representative of actual positions, that is, only for the planets. " 
    "Smaller objects tend to have actual orbits that do not follow idealized orbits due to gravitational perturbations, " 
    "so are not plotted.\n\n"

    "The Sun is visualized in detail with all its structural sections, core, radiative zone, convective zone and photosphere, "
    "chromosphere, inner corona, outer corona, and solar wind and heliopause -- the edge of the solar atmosphere, manually " 
    "select 123 AU to see this.\n\n" 
    
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

    "Python programming by Tony Quintanilla with assistance from Claude, ChatGPT and Gemini (my AI friends!), December 2024. "
    "Contact info: \"tony quintanilla (one word) at gmail dot com\"."
)


# Function to map celestial objects to colors
def color_map(planet):
    colors = {
        'Sun': 'rgb(255, 249, 240)',  # Slightly warm white to represent 6000K at the Sun's surface. The inner corona is 2M K.
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
        'Voyager 1 to heliopause': 'white',
        'Voyager 2': 'white',
        'Cassini-Huygens': 'white',
        'New Horizons': 'white',
        'Juno': 'white',
        'Galileo': 'white',
        'Pioneer 10': 'white',
        'Pioneer 11': 'white',
        'Europa Clipper': 'white',
        'OSIRIS-REx': 'white',
        'Parker Solar Probe': 'white',
        'James Webb Space Telescope': 'white',
        'Rosetta': 'white',
        'Oumuamua': 'rgb(218, 165, 32)',
        'Apophis': 'rgb(255, 140, 0)',
        'Vesta': 'rgb(240, 128, 128)',
        'Bennu': 'rgb(255, 255, 224)',
        'Šteins': 'rgb(30, 144, 255)',  # Added Šteins' color
        'Ikeya-Seki': 'rgb(218, 165, 32)',
        'West': 'rgb(218, 165, 32)',
        'Halley': 'rgb(218, 165, 32)',
        'Hyakutake': 'rgb(218, 165, 32)',
        'Hale-Bopp': 'rgb(218, 165, 32)',
        'McNaught': 'rgb(218, 165, 32)',
        'NEOWISE': 'rgb(218, 165, 32)',
        'Tsuchinshan-ATLAS': 'rgb(218, 165, 32)',
        'ATLAS': 'rgb(218, 165, 32)',
        'Churyumov-Gerasimenko': 'rgb(32, 178, 170)',
        'Borisov': 'rgb(64, 224, 208)',
        'SOHO: Solar and Heliospheric Observatory': 'white',
        'Ryugu': 'white',
        'Eros': 'white',
        'Itokawa': 'white',
        'Chang\'e': 'white',
        'Perseverance Rover': 'white',
        'DART Mission': 'white',
        'Lucy Mission': 'white',
        'Eris\' Moon Dysnomia': 'white',
        'Pluto\'s Moons Nix and Hydra': 'white',
        'Gaia': 'white',
        'Hayabusa2': 'white', 
        'Nix': 'white',        
        'Hydra': 'rgb(218, 165, 32)',  
        'Quaoar': 'rgb(244, 164, 96)',
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
        'Moon': 'Earth\'s only natural satellite.',
        'Mars': 'Known as the Red Planet, fourth planet from the Sun.',
        'Phobos': 'The larger and closer of Mars\'s two moons, spiraling inward towards Mars.',
        'Deimos': 'The smaller and more distant moon of Mars, with a stable orbit.',
        'Ceres': 'The largest object in the asteroid belt, considered a dwarf planet.',
        'Apophis': 'Near-Earth asteroid with a close approach in 2029.',
        'Vesta': 'Asteroid visited by NASA\'s Dawn mission.',
        'Bennu': 'A near-Earth asteroid studied by the OSIRIS-REx mission.',
        'Šteins': 'A main-belt asteroid visited by the Rosetta spacecraft.', 
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
        'it. https://voyager.jpl.nasa.gov/mission/',

        'Voyager 1 to heliopause': 'The farthest human-made object from Earth, exploring interstellar space. Voyager 1 is a space probe that was launched ' 
        'by NASA on September 5, 1977, to study the outer Solar System and interstellar space. It is the farthest human-made object from ' 
        'Earth, at a distance of 165.2 AU (24.7 billion km; 15.4 billion mi) as of October 2024.\n Here are some key dates in the ' 
        'Voyager 1 mission:\n * September 5, 1977, launched from Cape Canaveral, Florida.\n * March 5, 1979, reaches Jupiter.\n ' 
        '* November 12, 1980, reaches Saturn.\n * February 14, 1990, takes the \'Pale Blue Dot\' photograph of Earth from a distance of ' 
        '6 billion kilometers (3.7 billion miles).\n * February 17, 1998, overtakes Pioneer 10 to become the most distant human-made object ' 
        'from Earth.\n * August 25, 2012, crosses the heliopause and enters interstellar space, becoming the first spacecraft to do so. ' 
        'Voyager 1: Crossed the heliopause in August 2012 at a distance of roughly 121 AU (astronomical units). That\'s about 18 billion ' 
        'kilometers (11 billion miles) from the Sun\n ' 
        'Voyager 1 is still operational and continues to send data back to Earth. It is expected to continue operating until at least 2025, ' 
        'when its radioisotope thermoelectric generators will no longer be able to provide enough power to operate its scientific instruments.\n '
        'Voyager 1 mission was the first spacecraft to visit Jupiter and Saturn. It discovered active volcanoes on Jupiter\'s moon Io. ' 
        'It revealed the complexity of Saturn\'s rings. It was the first spacecraft to cross the heliopause and enter interstellar space. ' 
        'It is the farthest human-made object from Earth. It is a testament to the ingenuity and perseverance of the scientists and ' 
        'engineers who designed, built, and operate it. https://voyager.jpl.nasa.gov/mission/',

        'Voyager 2': 'The only spacecraft to visit all four gas giants: Jupiter, Saturn, Uranus, and Neptune. ' 
        'https://voyager.jpl.nasa.gov/mission/',

        'Cassini-Huygens': 'Explored Saturn, its rings, and moons, and delivered the Huygens probe to Titan. ' 
        'https://solarsystem.nasa.gov/missions/cassini/overview/',

        'New Horizons': 'Flew past Pluto in 2015, now exploring the Kuiper Belt. ' 
        'https://www.nasa.gov/mission_pages/newhorizons/main/index.html',

        'Juno': 'Currently orbiting Jupiter, studying its atmosphere and magnetic field. ' 
        'https://www.nasa.gov/mission_pages/juno/main/index.html',

        'Galileo': 'Studied Jupiter and its major moons, including Europa and Ganymede. https://solarsystem.nasa.gov/missions/galileo/overview/',
        
        'Pioneer 10': 'The first spacecraft to travel through the asteroid belt and make direct observations ' 
        'of Jupiter. https://www.nasa.gov/centers/ames/missions/archive/pioneer.html',
        
        'Pioneer 11': 'The first spacecraft to encounter Saturn and study its rings. ' 
        'https://www.nasa.gov/centers/ames/missions/archive/pioneer.html',
        
        'Europa Clipper': 'NASA\'s mission to explore Jupiter\'s moon Europa, launched October 14, 2024. No ephemeris available. ' 
        'https://europa.nasa.gov/',
        
        'OSIRIS-REx': 'NASA mission collected samples from asteroid Bennu and returned to Earth. ' 
        'Arrived 2018-12-03. Left 2021-05-10. Sample recovered 2023-09-24. Mission ongoing. https://www.asteroidmission.org/',
        
        'Parker Solar Probe':
        'Studying the Sun\'s outer corona by flying closer to the Sun than any previous spacecraft.\n\n'
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
        '* NOTE: To visualize the closest approach plot Paker on December 24, 2024, at 12 hours.'
        'Website: https://www.nasa.gov/content/goddard/parker-solar-probe',       
        
        'James Webb Space Telescope': 'NASA\'s flagship infrared space telescope. https://www.jwst.nasa.gov/',
        
        'Rosetta': 'European Space Agency, European Space Agency, mission that studied Comet ' 
        '67p/Churyumov-Gerasimenko. Flyby Asteroid Steins 2008-09-05. Arrives at 67p 2014-08-6. Deployed Philae lander 2014-11-12. ' 
        'Soft landing and termination 2016-09-30. https://rosetta.esa.int/', 
        
        'SOHO: Solar and Heliospheric Observatory': 'Observes the Sun and heliosphere from the L1 Lagrange point. ' 
        'https://sohowww.nascom.nasa.gov/',
        
        'Gaia': 'European Space Agency mission at L2 mapping the Milky Way. https://www.cosmos.esa.int/web/gaia',
        
        'Hayabusa2': 'Japan JAXA mission that returned samples from Ryugu. https://hayabusa2.jaxa.jp/en/', 
        
        'Chang\'e': 'China\'s lunar exploration program. http://www.clep.org.cn/',
        
        'Perseverance Rover': 'NASA Mars rover and Ingenuity helicopter. https://mars.nasa.gov/mars2020/',
        
        'DART Mission': 'NASA DART mission to test asteroid deflection. https://www.nasa.gov/dart \n* The DART mission ' 
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
        
        'Lucy Mission': 'NASA mission exploring Trojan asteroids around Jupiter. https://www.nasa.gov/lucy \n* The Lucy mission ' 
        'is a groundbreaking NASA space probe that\'s on an ambitious journey to explore the Trojan asteroids, a unique population ' 
        'of asteroids that share Jupiter\'s orbit around the Sun. These "Trojan swarms" are like fossils of our early solar system, ' 
        'holding clues to the formation of the planets and the conditions that existed billions of years ago. \n* Lucy will visit a ' 
        'total of eight asteroids. Main Belt Asteroids: 52246 Donaldjohanson; 152830 Dinkinesh. Trojan Asteroids: 3548 Eurybates ' 
        '(and its satellite Queta); 15094 Polymele; 11351 Leucus; 21900 Orus; 617 Patroclus (and its binary companion Menoetius).',

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
        
        'Halley': 'Most famous comet, returns every 76 years.',
        
        'Hyakutake': 'Comet passed very close to Earth in 1996.',
        
        'Hale-Bopp': 'Comet Hale-Bopp: Visible to the naked eye for 18 months.',
        
        'McNaught': 'Known as the Great Comet of 2007. January 12, 2007.',
        
        'NEOWISE': 'Brightest comet visible from the Northern Hemisphere in decades.',
        
        'Tsuchinshan-ATLAS': 'Comet expected to become bright in 2024.',
        
        'Churyumov-Gerasimenko': 'Comet visited by the Rosetta spacecraft.',
        
        'Borisov': 'Second interstellar object detected.',
        
        'Oumuamua': 'First known interstellar object detected passing through the Solar System.',
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
