import numpy as np
import math
import plotly.graph_objs as go
from shared_utilities import create_sun_direction_indicator
from planet_visualization_utilities import (create_sphere_points, SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, CHROMOSPHERE_RADII,
                                            INNER_CORONA_RADII, OUTER_CORONA_RADII, TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
                                            INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU, 
                                            GRAVITATIONAL_INFLUENCE_AU)

#####################################
# Sun Visualization Functions
#####################################

gravitational_influence_info = (
            "SELECT A MANUAL SCALE OF AT LEAST 160,000 AU TO VISUALIZE.\n\n"
            
            "Sun: Outer Limit of Gravitational Influence:\n\n" 

            "The Solar System\'s extent is actually defined in multiple ways. The Heliopause (120-123 AU):\n" 
            "Where the solar wind meets interstellar space.\n\n" 

            "Gravitational influence extends much further, including, Sedna\'s orbit (936 AU), the Hills Cloud/Inner\n" 
            "Oort Cloud (2,000-20,000 AU), and the Outer Oort Cloud (20,000-100,000 AU). The Sun's gravitational influence\n" 
            "extends to about 2 light-years (~126,000 AU).\n\n" 
            
            "While the Heliopause marks where the Sun\'s particle influence ends, its gravitational influence extends much\n" 
            "further. Sedna and other distant objects remain gravitationally bound to the Sun despite being well beyond\n" 
            "the Heliopause. This is why astronomers generally consider the Oort Cloud (and objects like Sedna) to be part\n" 
            "of our Solar System, even though we've never directly observed the Oort Cloud. The distinction comes down to\n" 
            "different types of influence:\n" 
            "* Particle/plasma influence (solar wind) → ends at Heliopause;\n" 
            "* gravitational influence → extends much further, including Sedna and the theoretical Oort Cloud.\n\n" 
            
            "So the Solar System is generally considered to extend at least as far as these gravitationally bound objects,\n" 
            "even beyond the Heliopause. Sedna is one of our first glimpses into this very distant region that may connect\n" 
            "to the Oort Cloud population."
        )

outer_oort_info = (
            "Oort Cloud: Outer Limit of Outer Oort Cloud:\n\n"
            
            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.\n\n"

            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            "Oort Cloud's Outer Edge: At 100,000 AU, it's about 1.58 light-years from the Sun, placing it just\n" 
            "beyond the nearest star systems and marking the boundary between the Solar System and interstellar space.\n\n" 

            "The Outer Oort Cloud is the primary source of long-period comets. Objects here are more loosely bound and more\n" 
            "susceptible to external gravitational perturbations."
        )

inner_oort_info = (
            "Oort Cloud: Outer Limit of Inner Oort Cloud:\n\n"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.\n" 
            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the\n" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an\n" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

inner_limit_oort_info = (
            "Oort Cloud: Inner Limit:\n\n"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.\n" 
            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the\n" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an\n" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

solar_wind_info = (
            "Solar Wind: Heliopause:\n\n"

            "The heliosphere is a vast, bubble-like region of space that surrounds the Sun and its planets. It's created by the\n" 
            "solar wind, a constant stream of charged particles flowing out from the Sun.\n" 
            "* Solar Wind: The solar wind is the driving force behind the heliosphere. It consists mostly of protons and electrons,\n" 
            "  along with heavier elements in smaller numbers. These particles are accelerated to high speeds by the Sun's heat and\n" 
            "  then escape its gravity, flowing out into space.\n" 
            "* Shape: The heliosphere isn't perfectly spherical. It's more like a long, teardrop shape with a rounded head and a\n" 
            "  flowing tail. This shape is due to the Sun's movement through the interstellar medium, the gas and dust that fills the\n" 
            "  space between stars.\n\n" 
            
            "Boundaries: The heliosphere has a few distinct boundaries:\n" 
            "* Termination Shock: This is where the solar wind abruptly slows down as it encounters the interstellar medium.\n" 
            "* Heliosheath: This is the turbulent region beyond the termination shock, where the solar wind mixes with the interstellar medium.\n" 
            "* Heliopause: This is the outermost boundary of the heliosphere, where the solar wind's pressure is balanced by the pressure of\n" 
            "  the interstellar medium. It's considered the true \"edge\" of our solar system.\n" 
            "* Protective Shield: The heliosphere acts as a protective bubble, shielding the planets within it from harmful galactic cosmic\n" 
            "  radiation. This radiation comes from outside our solar system and can be dangerous to life.\n" 
            "* Influence on Planets: The heliosphere also influences the planets within it. It interacts with planetary magnetic fields,\n" 
            "  creating phenomena like auroras. It can also affect the atmospheres of planets without strong magnetic fields.\n\n"   
                         
            "Voyager Missions: Our most valuable information about the heliosheath comes from the Voyager 1 and Voyager 2 spacecraft,\n" 
            "which have been traveling through space since 1977. Both probes have crossed the termination shock and are currently\n" 
            "exploring the heliosheath, sending back valuable data about this mysterious region. Voyager 1 encountered the Heliopause\n" 
            "at ~123 AU. This is considered the end of the Sun's influence and the start of interstellar space.\n\n" 
            
            "* The heliosheath extends from ~120 to 150 AU at the Heliopause.\n"
            "* Temperature: ~1,000,000K on average.\n"
            "* Black body radiation at 2.897 nm falls within the X-ray region of the electromagnetic spectrum, which is invisible to the human eye."
        )

termination_shock_info = (
            "Solar Wind: Termination Shock:\n\n"

            "The Solar Wind Termination Shock extends from about 75 to 100 AU.\n\n"

            "The Termination Shock is the region where the solar wind slows down from\n"
            "supersonic to subsonic speeds due to interaction with the interstellar\n"
            "medium. The kinetic energy transfers into heat, increasing abruptly.\n\n"

            "Voyager 1 encountered the Termination Shock at 94 AU, while Voyager 2 at 84 AU.\n"
            "After the Termination Shock the speeds slow down to ~100 to 200 km/s."
        )

outer_corona_info = (
            "Sun: Outer Corona:\n\n"

            "Solar Outer Corona extends to 50 solar radii or more,  about 0.2 AU. It is the most tenuous and expansive layer of\n" 
            "the solar atmosphere. The solar Corona generates the solar wind, a stream of electrons, protons, and Helium travelling\n" 
            "at supersonic speeds between 300 and 800 km/s, and temperatures to 2M K. The high temperature of the corona causes these\n" 
            "particles to escape the Sun's gravity. This extreme heat is a bit of a mystery, as it's much hotter than the Sun's surface.\n"
            "Scientists believe that magnetic fields and nanoflares, small explosions on the Sun's surface, play a role in heating the corona.\n\n"   

            "The outer corona is characterized by various structures, including streamers, loops, and plumes, which are shaped by the\n" 
            "Sun's magnetic field. These structures are constantly changing and evolving. The outer corona plays a crucial role in\n" 
            "space weather. Solar flares and coronal mass ejections, which originate in the corona, can disrupt Earth's magnetic field\n" 
            "and affect satellites, communication systems, and power grids.\n\n"

            "* Temperature: ~2-3M K, or an average of 2.5M K.\n" 
            "* The Outer Corona radiates at an average wavelength of 1.159 nm, which falls within the extreme ultraviolet to X-ray\n" 
            "  regions of the electromagnetic spectrum."
        )

inner_corona_info = (
            "Sun: Inner Corona:\n\n"

            "The solar inner corona is the region of the Sun's atmosphere that lies closest to its surface. It's a dynamic and complex\n" 
            "environment, with temperatures reaching millions of degrees Celsius and a variety of fascinating features:\n"
            "* Temperature: While still incredibly hot (around 1-3 million Kelvin), the inner corona is slightly cooler\n" 
            "than the outer corona. This temperature difference is one of the factors that drives the solar wind.\n"
            "* Density: The inner corona is denser than the outer corona, but still much less dense than the Sun's surface,\n" 
            "the photosphere. This low density makes it difficult to observe directly, except during a solar eclipse or\n" 
            "with specialized instruments.\n\n" 
            
            "Magnetic field: The inner corona is dominated by the Sun's magnetic field, which shapes and controls the\n" 
            "plasma in this region. The magnetic field lines create a variety of structures, including:\n" 
            "* Coronal loops: These are closed loops of magnetic flux that trap hot plasma, forming bright arcs that\n" 
            "  can be seen in ultraviolet and X-ray images.\n" 
            "* Coronal holes: These are areas where the magnetic field lines are open, allowing plasma to escape into\n" 
            "  space and contribute to the solar wind.\n" 
            "* Streamers: These are large, elongated structures that extend outward from the Sun, often associated with\n" 
            "  active regions and coronal mass ejections (CMEs).\n" 
            "* Dynamic activity: The inner corona is a constantly changing environment, with features evolving and erupting\n" 
            "  on different timescales. This activity is driven by the interplay between the magnetic field and the plasma,\n" 
            "  leading to phenomena like:\n" 
            "  * Solar flares: These are sudden, intense bursts of energy and radiation caused by the release of magnetic energy.\n" 
            "  * CMEs: These are massive eruptions of plasma and magnetic field from the corona, which can travel through space\n" 
            "    and impact Earth, disrupting satellites, communication systems, and power grids.\n\n"
            
            "* Solar Inner Corona (extends to 2-3 solar radii, ~0.014 AU)\n"
            "* Temperature: 1-2M K, or an average of about 1.5M K\n"
            "* It radiates at an average wavelenght of 1.93 nm, within the extreme ultraviolet to soft X-ray regions."
        )

chromosphere_info = (
            "Sun: Chromosphere:\n\n"

            "The chromosphere is a dynamic and visually stunning layer of the Sun's atmosphere, sandwiched between the\n" 
            "photosphere (the visible surface) and the corona (the outermost layer). It's a region of dramatic temperature\n" 
            "changes, intricate structures, and energetic events.\n\n"
             
            "* The chromosphere is relatively thin, extending only about 2,000 kilometers (1,200 miles) above the photosphere.\n" 
            "  It's also much less dense than the photosphere.\n" 
            "* The temperature in the chromosphere increases dramatically with altitude, from around 4,000 Kelvin at the\n" 
            "  photosphere to about 20,000 Kelvin at the inner corona.\n" 
            "* The chromosphere gets its name from the Greek word \"chroma,\" meaning color, because of its reddish appearance.\n" 
            "  This color is primarily due to the strong emission of light from hydrogen atoms\n" 
            "* The chromosphere is a constantly changing environment, with a variety of features that evolve and erupt on\n" 
            "  different timescales:\n" 
            "  * Spicules: These are jet-like eruptions of plasma that rise and fall like geysers, covering the chromosphere\n" 
            "    in a dynamic, \"grass-like\" pattern.\n" 
            "  * Filaments and prominences: These are large, cool, dense structures of plasma suspended in the chromosphere\n" 
            "    and corona by magnetic fields. When seen against the bright disk of the Sun, they appear as dark filaments.\n" 
            "    When seen extending beyond the Sun's edge, they appear as bright prominences.\n" 
            "  * Plages: These are bright regions in the chromosphere associated with active regions, where magnetic fields\n" 
            "    are concentrated.\n\n" 
             
            "* Radius: from Photosphere to 1.5 Solar radii or ~0.00465 - 0.0070 AU\n"
            "* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K\n"
            "* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible."
        )

photosphere_info = (
            "Sun: Photosphere\n\n"

            "Solar Convective Zone and Photosphere, the visible surface.\n"
            "* The photosphere is the visible surface of the Sun. It's a relatively thin layer, only about 500 kilometers thick.\n" 
            "* Including both the Convective Zone and the Photosphere, the radius is from 0.7 to 1 Solar radii, or about 0.00465 AU.\n"
            "* Temperature: from 2M K at the Radiative Zone to ~5,500K at the Photosphere.\n"
            "* Convection transports energy to the visible \"surface\" of the Sun. The convection process starts at the Radiative Zone\n"
            "* At the Photosphere, the energy is radiated as visible light. Radiation emits at a peak wavelength at 527.32 nm, which\n" 
            "  is in the green spectrum. The Sun's emitted light is a combination of all visible wavelengths, resulting in a yellowish-white color.\n\n"
             
            "* The photosphere is cooler than the Sun's core and the layers above it, but still hot enough to make the photosphere glow brightly.\n" 
            "* To the naked eye, the photosphere appears as a smooth, yellow disk. However, closer observations reveal a variety of features, including:\n" 
            "  * Granulation: This is a pattern of small, bright cells surrounded by darker boundaries, caused by convection\n" 
            "    currents bringing hot plasma up from the Sun's interior.\n" 
            "  * Sunspots: These are dark, cooler regions on the photosphere caused by strong magnetic fields. They can be\n" 
            "    larger than Earth and last for days or weeks.\n" 
            "  * Faculae: These are bright regions surrounding sunspots, also associated with magnetic fields.\n" 
            "  * Energy transport: The photosphere is where the Sun's energy, generated in its core through nuclear fusion,\n" 
            "    is finally released as light. This energy has traveled outward through the Sun's interior in the form of\n" 
            "    radiation and convection, and it's in the photosphere that it transitions to primarily radiation, allowing it\n" 
            "    to escape into space.\n" 
            "  * Spectrum: The photosphere emits a continuous spectrum of light, which includes all colors of the rainbow.\n" 
            "  * Solar activity: The photosphere is also where many solar activity events originate, such as:\n" 
            "    * Solar flares: These are sudden, intense bursts of energy and radiation caused by the release of magnetic\n" 
            "      energy in the solar atmosphere.\n" 
            "    * Coronal mass ejections (CMEs): These are massive eruptions of plasma and magnetic field from the Sun's corona,\n" 
            "      often associated with flares.\n"
            "    * Solar activity events originating in the photosphere can affect Earth's magnetic field and disrupt satellites,\n" 
            "      communication systems, and power grids.\n\n"
        )

radiative_zone_info = (
            "Sun: Radiative Zone\n\n"

            "The Solar Radiative Zone extends from about 0.2 to 0.7 solar radii, about 0.00325 AU. Temperature ranges from about\n" 
            "7M K near the core to about 2M K near the convective zone. Energy is transported by radiative diffusion, through photon\n" 
            "absorption and re-emission.\n\n"

            "The radiative zone is a vast region within the Sun, located between the core and the convective zone. It's a place\n" 
            "of intense heat and density, where energy generated in the core slowly makes its way outward in the form of photons.\n"  
            "* Density: The density also decreases with distance from the core, but it remains much denser than the convective zone above it.\n\n" 
            "* Energy transport: The primary mode of energy transport in the radiative zone is radiative diffusion. Photons\n" 
            "  generated in the core through nuclear fusion undergo countless absorptions and re-emissions as they interact\n" 
            "  with the dense plasma. This process is incredibly slow, and it can take millions of years for a photon to travel\n" 
            "  from the core to the outer edge of the radiative zone.\n" 
            "* Opacity: The radiative zone is highly opaque, meaning that photons can only travel a short distance before being\n" 
            "  absorbed or scattered. This high opacity is due to the high density and the presence of heavy elements, which are\n" 
            "  more efficient at absorbing and scattering radiation.\n" 
            "* Energy transfer: The radiative zone plays a crucial role in transferring energy from the Sun's core to its outer\n" 
            "  layers. Without it, the Sun would not be able to shine.\n" 
            "* Stability: The slow and gradual energy transport in the radiative zone helps to maintain the Sun's overall stability.\n" 
            "* Helioseismology: This technique uses observations of sound waves traveling through the Sun to probe its interior\n" 
            "  structure, including the radiative zone. By analyzing the frequencies and patterns of these waves, scientists can\n" 
            "  infer the temperature, density, and composition of the radiative zone.\n" 
            "* Neutrino observations: Neutrinos are subatomic particles produced in the Sun's core that can pass through the\n" 
            "  radiative zone almost unimpeded. By detecting and analyzing these neutrinos, scientists can gain information about\n" 
            "  the nuclear reactions taking place in the core and the conditions in the radiative zone."
            )

core_info = (
            "Sun: Solar Core\n\n"

            "The Sun's core is where the Sun's energy is generated through nuclear fusion, providing the light and heat that sustain life on Earth:\n" 
            "* Location: The core is located at the very center of the Sun, extending outward to about 25% of the Sun's radius.\n" 
            "* Size: While relatively small compared to the Sun's overall size, the core contains about 34% of the Sun's total mass.\n" 
            "* Temperature: The core is the hottest place in the solar system, with temperatures reaching 15 million Kelvin\n" 
            "* Density: The core is incredibly dense, about 150 times denser than water. This extreme density is due to the\n" 
            "  immense pressure exerted by the Sun's outer layers.\n" 
            "* Composition: The core is primarily composed of hydrogen (about 34% by mass) and helium (about 64% by mass).\n" 
            "  Trace amounts of heavier elements are also present.\n\n"
              
            "The dominant fusion process in the Sun's core is the proton-proton chain reaction:\n" 
            "* Two protons, hydrogen nuclei, collide and fuse to form a deuterium nucleus releasing a positron and a neutrino.\n" 
            "* The deuterium nucleus collides with another proton to form a helium-3 nucleus, releasing a gamma ray.\n" 
            "* Two helium-3 nuclei collide to form a helium-4 nucleus, releasing two protons.\n" 
            "* This process converts a small amount of mass into a tremendous amount of energy\n\n" 
            
            "The energy generated in the core is transported outward through the Sun in two ways:\n"
            "* Radiative zone: The energy first travels through the radiative zone, where it is carried by photons that undergo\n" 
            "  countless absorptions and re-emissions. This process is very slow, taking millions of years for energy to travel\n" 
            "  from the core to the outer edge of the radiative zone.\n" 
            "* Convective zone: Once the energy reaches the convective zone, it is transported by convection currents, where hot\n" 
            "  plasma rises and cooler plasma sinks. This is a much faster process, taking only a few weeks for energy to reach\n" 
            "  the Sun's surface.\n\n" 
            
            "* Helioseismology: By analyzing sound waves traveling through the Sun, scientists can infer the conditions in the core,\n" 
            "  such as its temperature, density, and composition.\n" 
            "* Neutrino observations: Neutrinos produced in the core can pass through the Sun almost unimpeded, providing direct\n" 
            "  information about the nuclear reactions taking place there." 
            )

gravitational_influence_info_hover = (
            "Sun: Outer Limit of Gravitational Influence:<br><br>" 

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

outer_oort_info_hover = (
            "Oort Cloud: Outer Limit of Outer Oort Cloud:<br><br>"
            
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

inner_oort_info_hover = (
            "Oort Cloud: Outer Limit of Inner Oort Cloud:<br><br>"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the<br>" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.<br>" 
            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.<br>" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital<br>" 
            "periods exceeding 200 years.<br><br>" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the<br>" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an<br>" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

inner_limit_oort_info_hover = (
            "Oort Cloud: Inner Limit:<br><br>"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the<br>" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.<br>" 
            "Predominantly composed of cometary nuclei—small, icy bodies made of water ice, ammonia, and methane.<br>" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital<br>" 
            "periods exceeding 200 years.<br><br>" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the<br>" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an<br>" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

solar_wind_info_hover = (
            "Solar Wind: Heliopause:<br><br>"

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

termination_shock_info_hover = (
            "Solar Wind: Termination Shock:<br><br>"

            "The Solar Wind Termination Shock extends from about 75 to 100 AU.<br><br>"

            "The Termination Shock is the region where the solar wind slows down from<br>"
            "supersonic to subsonic speeds due to interaction with the interstellar<br>"
            "medium. The kinetic energy transfers into heat, increasing abruptly.<br><br>"

            "Voyager 1 encountered the Termination Shock at 94 AU, while Voyager 2 at 84 AU.<br>"
            "After the Termination Shock the speeds slow down to ~100 to 200 km/s."
        )

outer_corona_info_hover = (
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

inner_corona_info_hover = (
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

chromosphere_info_hover = (
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

photosphere_info_hover = (
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

radiative_zone_info_hover = (
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
            "  radiative zone almost unimpeded. By detecting and analyzing these neutrinos, scientists can gain info_hoverrmation about<br>" 
            "  the nuclear reactions taking place in the core and the conditions in the radiative zone."
            )

core_info_hover = (
            "Sun: Solar Core<br><br>"

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
        '* Plotting marker size: 12 px '
)


def create_sun_hover_text():
    """
    Creates hover text for the Sun visualization with information about each layer.
    Future expansion could include dynamic temperature and size data.
    
    Returns:
        dict: Hover text for each layer of the Sun
    """
    return {
        'photosphere': (
            'Solar Photosphere<br>'
            'Temperature: ~6,000K<br>'
            'Radius: 0.00465 AU'
        ),
        'inner_corona': (
            'Inner Corona<br>'
            'Temperature: >2,000,000K<br>'
            'Extends to: 2-3 solar radii (~0.014 AU)'
        ),
        'outer_corona': (
            'Outer Corona<br>'
            'Temperature: ~1,000,000K<br>'
            'Extends to: ~50 solar radii (~0.2 AU)'
        )
    }

# In the create_corona_sphere function, increase the number of points
def create_corona_sphere(radius, n_points=100):  # Increased from 50 to 100 points
    """Create points for a sphere surface to represent corona layers."""
    phi = np.linspace(0, 2*np.pi, n_points)
    theta = np.linspace(-np.pi/2, np.pi/2, n_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    return x.flatten(), y.flatten(), z.flatten()

# Individual Sun shell creation functions

def create_sun_gravitational_shell():
    """Creates the Sun's gravitational influence shell."""
    x, y, z = create_sphere_points(GRAVITATIONAL_INFLUENCE_AU, n_points=40)
    
    text_array = [gravitational_influence_info_hover for _ in range(len(x))]
    customdata_array = ["Sun's Gravitational Influence" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(102, 187, 106)', 
                opacity=0.3
            ),
            name='Sun\'s Gravitational Influence',
            text=text_array,             
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    """
    sun_traces = create_sun_direction_indicator(
        center_position=(0, 0, 0), 
        shell_radius=GRAVITATIONAL_INFLUENCE_AU
    )
    for trace in sun_traces:
        traces.append(trace) 
    """

    return traces

def create_sun_outer_oort_shell():
    """Creates the Sun's outer Oort cloud shell."""
    x, y, z = create_sphere_points(OUTER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [outer_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Outer Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.2
            ),
            name='Outer Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    """
    sun_traces = create_sun_direction_indicator(
        center_position=(0, 0, 0), 
        shell_radius=OUTER_OORT_CLOUD_AU
    )
    for trace in sun_traces:
        traces.append(trace) 
    """

    return traces

def create_sun_inner_oort_shell():
    """Creates the Sun's inner Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    """
    sun_traces = create_sun_direction_indicator(
        center_position=(0, 0, 0), 
        shell_radius=INNER_OORT_CLOUD_AU
    )
    for trace in sun_traces:
        traces.append(trace)
    """
    
    return traces

def create_sun_inner_oort_limit_shell():
    """Creates the inner limit of the Sun's Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_LIMIT_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_limit_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Limit of Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Limit of Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    """
    sun_traces = create_sun_direction_indicator(
        center_position=(0, 0, 0), 
        shell_radius=INNER_LIMIT_OORT_CLOUD_AU
    )
    for trace in sun_traces:
        traces.append(trace)
    """

    return traces

def create_sun_heliopause_shell():
    """Creates the Sun's heliopause shell."""
    x, y, z = create_sphere_points(HELIOPAUSE_RADII * SOLAR_RADIUS_AU, n_points=40)
    
    text_array = [solar_wind_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Heliopause" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(135, 206, 250)',
                opacity=0.3
            ),
            name='Solar Wind Heliopause',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    """
    sun_traces = create_sun_direction_indicator(
        center_position=(0, 0, 0), 
        shell_radius=HELIOPAUSE_RADII * SOLAR_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)
    """

    return traces

def create_sun_termination_shock_shell():
    """Creates the Sun's termination shock shell."""
    x, y, z = create_sphere_points(TERMINATION_SHOCK_AU, n_points=40)
    
    text_array = [termination_shock_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Termination Shock" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(240, 244, 255)',
                opacity=0.3
            ),
            name='Solar Wind Termination Shock',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    """
    sun_traces = create_sun_direction_indicator(
        center_position=(0, 0, 0), 
        shell_radius=TERMINATION_SHOCK_AU
    )
    for trace in sun_traces:
        traces.append(trace)
    """

    return traces

def create_sun_outer_corona_shell():
    """Creates the Sun's outer corona shell."""
    x, y, z = create_sphere_points(OUTER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=50)
    
    text_array = [outer_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Outer Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.75,
                color='rgb(25, 25, 112)',
                opacity=0.5
            ),
            name='Sun: Outer Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_corona_shell():
    """Creates the Sun's inner corona shell."""
    x, y, z = create_sphere_points(INNER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [inner_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Inner Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1,
                color='rgb(0, 0, 255)',
                opacity=0.2
            ),
            name='Sun: Inner Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_chromosphere_shell():
    """Creates the Sun's chromosphere shell."""
    x, y, z = create_sphere_points(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [chromosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Chromosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.25,
                color='rgb(30, 144, 255)',
                opacity=0.2
            ),
            name='Sun: Chromosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_photosphere_shell():
    """Creates the Sun's photosphere shell."""
    x, y, z = create_sphere_points(SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [photosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Photosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7.0,
                color='rgb(255, 244, 214)',
                opacity=1.0
            ),
            name='Sun: Photosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_radiative_shell():
    """Creates the Sun's radiative zone shell."""
    x, y, z = create_sphere_points(RADIATIVE_ZONE_AU, n_points=60)
    
    text_array = [radiative_zone_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Radiative Zone" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7,
                color='rgb(30, 144, 255)',
                opacity=1.0
            ),
            name='Sun: Radiative Zone',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_core_shell():
    """Creates the Sun's core shell."""
    x, y, z = create_sphere_points(CORE_AU, n_points=60)
    
    text_array = [core_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Core" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=10,
                color='rgb(70, 130, 180)',
                opacity=1.0
            ),
            name='Sun: Core',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces