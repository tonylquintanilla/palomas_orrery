import numpy as np
import math
import plotly.graph_objs as go
from shared_utilities import create_sun_direction_indicator

from planet_visualization_utilities import (create_sphere_points, SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, CHROMOSPHERE_RADII,
                                            INNER_CORONA_RADII, OUTER_CORONA_RADII, STREAMER_BELT_RADII,
                                            ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
                                            TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
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
            "* Particle/plasma influence (solar wind) [OK] ends at Heliopause;\n" 
            "* gravitational influence [OK] extends much further, including Sedna and the theoretical Oort Cloud.\n\n" 
            
            "So the Solar System is generally considered to extend at least as far as these gravitationally bound objects,\n" 
            "even beyond the Heliopause. Sedna is one of our first glimpses into this very distant region that may connect\n" 
            "to the Oort Cloud population."
        )

outer_oort_info = (
            "Oort Cloud: Outer Limit of Outer Oort Cloud:\n\n"
            
            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.\n\n"

            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.\n" 
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
            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.\n" 
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
            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            "Inner Oort Cloud (Hills Cloud): Extends from about 2,000 AU to 20,000 AU. More tightly bound to the\n" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an\n" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

hills_cloud_torus_info = (
            "Oort Cloud: Hills Cloud Torus:\n\n"

            "Based on dynamical models showing the inner Oort Cloud is more disk-like due to galactic tides.\n"

            "Structure:\n" 
            "* Hills Cloud (Inner Oort): 2,000-20,000 AU, disk-like/toroidal\n"
            "* Outer Oort Cloud: 20,000-100,000+ AU, roughly spherical but clumpy\n" 
            "Key Characteristics:\n" 
            "* Not uniform shells but complex, structured regions\n" 
            "* Density varies significantly throughout\n" 
            "* Influenced by galactic tides and stellar encounters\n" 
            "* Contains an estimated 1-100 trillion objects >1km<br>\n" 
            "Scientific Evidence:\n" 
            "* Comet orbital inclinations suggest spherical outer region\n" 
            "* Jupiter-family comets indicate inner disk-like region\n" 
            "* Computer simulations show tidal sculpting effects\n" 
            "* Stellar encounter models predict clumpy structure\n" 
            "Recent Discoveries:\n" 
            "* Objects like Sedna may be inner Oort Cloud members\n" 
            "* 2012 VP113 provides evidence for inner Oort population\n" 
            "* NEOWISE survey improving population estimates"
        )

outer_oort_clumpy_info = (
            "Oort Cloud: Clumpy Oort Cloud:\n\n"

            "Reflects N-body simulations showing stellar encounters create density variations.\n"

            "Structure:\n" 
            "* Hills Cloud (Inner Oort): 2,000-20,000 AU, disk-like/toroidal\n"
            "* Outer Oort Cloud: 20,000-100,000+ AU, roughly spherical but clumpy\n" 
            "Key Characteristics:\n" 
            "* Not uniform shells but complex, structured regions\n" 
            "* Density varies significantly throughout\n" 
            "* Influenced by galactic tides and stellar encounters\n" 
            "* Contains an estimated 1-100 trillion objects >1km<br>\n" 
            "Scientific Evidence:\n" 
            "* Comet orbital inclinations suggest spherical outer region\n" 
            "* Jupiter-family comets indicate inner disk-like region\n" 
            "* Computer simulations show tidal sculpting effects\n" 
            "* Stellar encounter models predict clumpy structure\n" 
            "Recent Discoveries:\n" 
            "* Objects like Sedna may be inner Oort Cloud members\n" 
            "* 2012 VP113 provides evidence for inner Oort population\n" 
            "* NEOWISE survey improving population estimates"
        )

galactic_tide_info = (
            "Oort Cloud: Galactic Tide Influenced Oort:\n\n"

            "Shows how the Milky Way's gravity creates asymmetries.\n"

            "Structure:\n" 
            "* Hills Cloud (Inner Oort): 2,000-20,000 AU, disk-like/toroidal\n"
            "* Outer Oort Cloud: 20,000-100,000+ AU, roughly spherical but clumpy\n" 
            "Key Characteristics:\n" 
            "* Not uniform shells but complex, structured regions\n" 
            "* Density varies significantly throughout\n" 
            "* Influenced by galactic tides and stellar encounters\n" 
            "* Contains an estimated 1-100 trillion objects >1km<br>\n" 
            "Scientific Evidence:\n" 
            "* Comet orbital inclinations suggest spherical outer region\n" 
            "* Jupiter-family comets indicate inner disk-like region\n" 
            "* Computer simulations show tidal sculpting effects\n" 
            "* Stellar encounter models predict clumpy structure\n" 
            "Recent Discoveries:\n" 
            "* Objects like Sedna may be inner Oort Cloud members\n" 
            "* 2012 VP113 provides evidence for inner Oort population\n" 
            "* NEOWISE survey improving population estimates"
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
    "Sun: Extended Corona (F-corona / Outer):\n\n"

    "This shell marks the extended outer solar corona at ~50 solar radii (~0.23 AU).\n"
    "At this distance the corona is extremely tenuous -- the F-corona (dust-scattered\n"
    "sunlight showing Fraunhofer absorption lines) dominates over the electron K-corona.\n\n"

    "* The visible structured corona (helmet streamers) extends to ~4-6 R_sun.\n"
    "* The Alfven surface -- the true corona/solar wind boundary -- is ~10-20 R_sun.\n"
    "  Parker Solar Probe measured this at 18.8 R_sun on April 28, 2021.\n"
    "* Beyond the Alfven surface, plasma is solar wind, not corona.\n"
    "* This 50 R_sun shell represents the faint, extended F-corona envelope.\n\n"

    "* Temperature: ~1-2 million K (the coronal heating paradox -- hotter than the surface)\n"
    "* The corona merges gradually into the solar wind beyond ~15-20 R_sun.\n"
    "* Parker Solar Probe's closest approach: ~8.8 R_sun as of 2024.\n"
    "* The corona radiates at ~1.159 nm average wavelength (extreme ultraviolet to X-ray)."
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
            "* It radiates at an average wavelength of 1.93 nm, within the extreme ultraviolet to soft X-ray regions."
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
            "* Particle/plasma influence (solar wind) [OK] ends at Heliopause;<br>" 
            "* gravitational influence [OK] extends much further, including Sedna and the theoretical Oort Cloud.<br><br>" 
            
            "So the Solar System is generally considered to extend at least as far as these gravitationally bound objects,<br>" 
            "even beyond the Heliopause. Sedna is one of our first glimpses into this very distant region that may connect<br>" 
            "to the Oort Cloud population."
        )

outer_oort_info_hover = (
            "Oort Cloud: Outer Limit of Outer Oort Cloud:<br><br>"
            
            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the<br>" 
            "Solar System at distances ranging from approximately 2,000 AU to 100,000 AU from the Sun.<br><br>"

            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.<br>" 
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
            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.<br>" 
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
            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.<br>" 
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
    "Sun: Extended Corona (F-corona / Outer):<br><br>"

    "Extended outer solar corona at ~50 solar radii (~0.23 AU).<br>"
    "F-corona (dust-scattered sunlight with Fraunhofer lines) dominates at this distance.<br><br>"

    "Layer hierarchy within this shell:<br>"
    "* Visible streamer belt: 4-6 R_sun (see Streamer Belt shell)<br>"
    "* Alfven surface (corona/solar wind boundary): ~15-20 R_sun (see Alfven Surface shell)<br>"
    "  Parker Solar Probe first crossing: 18.8 R_sun, April 28, 2021<br>"
    "* F-corona (dust-scattered): 3-50+ R_sun -- this shell's extent<br><br>"

    "* Temperature: ~1-2 million K (coronal heating paradox)<br>"
    "* Beyond the Alfven surface, plasma is solar wind, not true corona<br>"
    "* Parker Solar Probe closest approach: ~8.8 R_sun (2024)<br>"
    "* Radiates at ~1.159 nm (extreme ultraviolet to X-ray)<br><br>"

    "MAPS C/2026 A1 entered SOHO/LASCO C3 field (~33 R_sun) on April 2, 2026,<br>"
    "already inside this shell and approaching the Alfven surface."
)

streamer_belt_info = (
    "Sun: Streamer Belt / Visible Corona:\n\n"

    "The streamer belt is the brightest, most structured region of the visible solar corona,\n"
    "extending from the inner corona out to about 4-6 solar radii. This is the corona that\n"
    "observers see during total solar eclipses as a pearly white halo around the Sun.\n\n"

    "Three components of white-light corona:\n"
    "* K-corona (kontinuierlich): Sunlight scattered off free electrons. Dominates within 2-3 R_sun.\n"
    "  Spectrum is continuous (blurred absorption lines) -- electrons move too fast to preserve them.\n"
    "* F-corona (Fraunhofer): Sunlight scattered off dust particles. Shows Fraunhofer absorption lines.\n"
    "  Dominates beyond ~3 R_sun and extends to ~15 R_sun. Has an oval shape.\n"
    "* E-corona (emission): Line emission from highly ionized Fe, Ni, Ca atoms. Visible to ~2 R_sun.\n\n"

    "* Helmet streamers: Bottle-shaped, dense magnetic structures extending to 4-6 R_sun.\n"
    "  Source of slow solar wind. Visible in coronagraphs and at eclipse.\n"
    "* Temperature: ~1-2 million K\n"
    "* MAPS C/2026 A1 was first detected in SOHO/LASCO C3 at ~0.15 AU (~33 R_sun) on April 2, 2026.\n"
    "  By April 3-4 it was passing through this visible streamer belt region."
)

streamer_belt_info_hover = (
    "Sun: Streamer Belt / Visible Corona:<br><br>"

    "The streamer belt is the brightest, most structured region of the visible solar corona,<br>"
    "extending from the inner corona out to about 4-6 solar radii. This is the corona that<br>"
    "observers see during total solar eclipses as a pearly white halo around the Sun.<br><br>"

    "Three components of white-light corona:<br>"
    "* K-corona (kontinuierlich): Sunlight scattered off free electrons. Dominates within 2-3 R_sun.<br>"
    "  Spectrum is continuous -- electrons move too fast to preserve absorption lines.<br>"
    "* F-corona (Fraunhofer): Sunlight scattered off dust. Shows Fraunhofer absorption lines.<br>"
    "  Dominates beyond ~3 R_sun, extends to ~15 R_sun. Has an oval shape.<br>"
    "* E-corona (emission): Line emission from ionized Fe, Ni, Ca. Visible to ~2 R_sun.<br><br>"

    "* Helmet streamers: Dense magnetic structures extending 4-6 R_sun. Source of slow solar wind.<br>"
    "* Temperature: ~1-2 million K<br><br>"
    "MAPS C/2026 A1 context:<br>"
    "MAPS was detected in SOHO/LASCO C3 (~33 R_sun field) from April 2, 2026.<br>"
    "It passed through this visible streamer belt on April 3-4 before perihelion."
)

roche_limit_info = (
    "Sun: Roche Limit (Fluid Body / Comet):\n\n"

    "The Roche limit is the distance within which a fluid body held together only by\n"
    "self-gravity will be torn apart by the Sun's tidal forces.\n\n"

    "Formula: d = 2.44 x R_sun x (rho_sun / rho_comet)^(1/3)\n"
    "Solar density: 1,408 kg/m^3 | Comet density: ~500 kg/m^3\n"
    "Result: ~3.45 solar radii = ~2,400,165 km from Sun center\n"
    "  = ~1,704,465 km from photosphere (~0.0114 AU)\n\n"

    "Key physics:\n"
    "* The Roche limit is NOT absolute. It marks where tidal forces overcome SELF-GRAVITY\n"
    "  only. Tensile strength -- the material bonds holding the nucleus together -- can\n"
    "  allow survival well inside the formal Roche limit.\n"
    "* Ikeya-Seki (C/1965 S1, ~5 km nucleus) survived at 1.66 R_sun (0.008 AU).\n"
    "* Great Comet of 1843 survived at 1.19 R_sun (0.006 AU) -- deepest ever recorded.\n"
    "* Comet Lovejoy (C/2011 W3, ~500 m) survived perihelion briefly at ~1.2 R_sun.\n"
    "* Size and structural coherence are decisive: larger nuclei have both stronger\n"
    "  self-gravity AND stronger material bonds to resist tidal disruption.\n\n"

    "MAPS C/2026 A1 context:\n"
    "* MAPS disintegrated at ~8.33 R_sun (0.039 AU) -- OUTSIDE the Roche limit.\n"
    "* Primary destruction mechanisms: thermal ablation (1-2 million K corona) and\n"
    "  rotational spin-up from outgassing jets. Tidal forces never acted on MAPS.\n"
    "* The debris swept THROUGH the Roche limit (3.45 R_sun, 0.016 AU) to perihelion\n"
    "  at 1.23 R_sun -- but the nucleus was already gone."
)

roche_limit_info_hover = (
    "Sun: Roche Limit (Fluid Body / Comet):<br><br>"

    "The Roche limit marks where tidal forces overcome a body's self-gravity.<br>"
    "It is NOT absolute -- tensile strength can allow survival inside it.<br><br>"

    "Formula: d = 2.44 x R_sun x (rho_sun / rho_comet)^(1/3)<br>"
    "Solar density: 1,408 kg/m^3 | Comet density: ~500 kg/m^3<br>"
    "Result: ~3.45 R_sun (~0.016 AU) from Sun center<br><br>"

    "Key physics:<br>"
    "* Roche limit depends on DENSITY RATIO only -- not on nucleus mass or size<br>"
    "* Tensile strength can allow survival inside the limit:<br>"
    "  Ikeya-Seki (~5 km) survived at 1.66 R_sun (0.008 AU)<br>"
    "  Great Comet of 1843 survived at 1.19 R_sun (0.006 AU)<br>"
    "  Lovejoy (C/2011 W3, ~500 m) survived briefly at ~1.2 R_sun<br>"
    "* Larger nuclei: stronger self-gravity + stronger material bonds<br><br>"

    "MAPS C/2026 A1 context:<br>"
    "* Disintegrated at 8.33 R_sun (0.039 AU) -- OUTSIDE the Roche limit<br>"
    "* Killed by thermal ablation and rotational spin-up, not tidal forces<br>"
    "* Debris swept through this shell to perihelion at 1.23 R_sun (0.006 AU)<br>"
    "* The nucleus never reached the Roche limit intact"
)

alfven_surface_info = (
    "Sun: Alfven Surface:\n\n"

    "The Alfven surface is the true outer boundary of the solar corona -- the point where\n"
    "the solar wind accelerates past the local Alfven speed and plasma can no longer\n"
    "communicate back to the Sun. Beyond it, the corona becomes the solar wind.\n\n"

    "* Location: ~10-20 solar radii, measured directly by NASA's Parker Solar Probe.\n"
    "  On April 28, 2021, Parker Solar Probe crossed inward at 18.8 R_sun (13 million km),\n"
    "  spending ~5 hours inside the corona -- the first spacecraft to 'touch the Sun.'\n"
    "* This is not a smooth sphere: it has spikes and valleys shaped by solar magnetic activity.\n"
    "  At polar coronal holes: ~12-15 R_sun. In the streamer belt: ~17-19 R_sun.\n\n"

    "Why it matters:\n"
    "* Inside the Alfven surface: plasma is magnetically connected to the Sun.\n"
    "  Perturbations (like a passing comet) can propagate back to the solar surface.\n"
    "* Outside it: plasma becomes the solar wind, causally disconnected from the Sun.\n"
    "* This boundary governs the Sun's angular momentum loss and spin-down over time.\n\n"

    "MAPS C/2026 A1 context:\n"
    "* MAPS crossed the Alfven surface approximately April 3, ~18:00 UTC --\n"
    "  about 20 hours before its nucleus disintegrated.\n"
    "* Inside this boundary, the comet was immersed in magnetically connected coronal plasma\n"
    "  at temperatures of 1-2 million K, subject to intense tidal and thermal stresses.\n"
    "* The corona it entered here is physically different from the visible outer corona --\n"
    "  this is where the Sun 'feels' the comet and vice versa."
)

alfven_surface_info_hover = (
    "Sun: Alfven Surface:<br><br>"

    "The true outer boundary of the solar corona. Beyond this point, plasma can no longer<br>"
    "communicate back to the Sun -- the corona becomes the solar wind.<br><br>"

    "* Measured directly: Parker Solar Probe, April 28, 2021 at 18.8 R_sun (13 million km)<br>"
    "  First spacecraft to enter the corona -- 'touching the Sun' for ~5 hours.<br>"
    "* Not a smooth sphere: spikes and valleys from solar magnetic activity.<br>"
    "  Polar coronal holes: ~12-15 R_sun | Streamer belt: ~17-19 R_sun<br><br>"

    "Why it matters:<br>"
    "* Inside: plasma magnetically connected to the Sun. Alfven waves propagate inward.<br>"
    "* Outside: solar wind -- causally disconnected, flowing outward at 300-800 km/s.<br>"
    "* Governs the Sun's angular momentum loss and spin-down rate over billions of years.<br><br>"

    "MAPS C/2026 A1 context:<br>"
    "* MAPS crossed inward ~April 3, 18:00 UTC -- ~20 hours before disintegration.<br>"
    "* Inside this surface the comet was in magnetically connected 1-2 million K plasma.<br>"
    "* The corona paradox: hotter farther from surface -- still unexplained (Alfven waves,<br>"
    "  nanoflares, and magnetic reconnection are leading candidate mechanisms)."
)

inner_corona_info_hover = (
    "Sun: Inner Corona (K-corona):<br><br>"

    "The solar inner corona closest to the surface. Dominated by the K-corona --<br>"
    "sunlight scattered off free electrons. Extends to ~2-3 solar radii.<br><br>"

    "* Temperature: 1-3 million K (increases with altitude -- the coronal heating paradox)<br>"
    "* K-corona dominates within ~2.3 R_sun; F-corona (dust) takes over beyond ~3 R_sun<br>"
    "* Density: much denser than outer corona, but still far less than photosphere<br>"
    "* Magnetic structures: coronal loops, coronal holes, streamers<br>"
    "* Solar flares and CMEs originate here<br><br>"

    "Roche limit proximity:<br>"
    "* The fluid Roche limit for comets (~3.45 R_sun) lies just outside this shell.<br>"
    "* Any Kreutz sungrazer penetrating the inner K-corona is at or inside the tidal<br>"
    "  disruption threshold. MAPS C/2026 A1 perihelion reached 1.23 R_sun --<br>"
    "  deep inside both the inner corona and the Roche limit simultaneously.<br><br>"

    "* Solar Inner Corona (extends to 2-3 solar radii, ~0.014 AU)<br>"
    "* Temperature: 1-2M K, or an average of about 1.5M K<br>"
    "* Radiates at an average wavelength of 1.93 nm, extreme ultraviolet to soft X-ray."
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
            "  radiative zone almost unimpeded. By detecting and analyzing these neutrinos, scientists can gain information about<br>" 
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
    'Five corona/boundary layers now visualized separately:<br>'
    '* Inner Corona (K-corona): 1-3 R_sun, ~1-3 million K<br>'
    '* Roche Limit: 3.45 R_sun -- tidal disruption threshold for comets<br>'
    '* Streamer Belt (Visible Corona): 4-6 R_sun -- eclipse white-light corona<br>'
    '* Alfven Surface: ~18.8 R_sun -- true corona/solar wind boundary<br>'
    '  (Parker Solar Probe first crossing: April 28, 2021)<br>'
    '* Extended Corona (F-corona): ~50 R_sun -- faint dust-scattered envelope<br><br>'
    'Parker Solar Probe closest approach: ~8.8 R_sun (2024)<br><br>'
    'The coronal heating paradox: the corona is 200x hotter than the photosphere<br>'
    'despite being farther from the energy source. Leading theories: Alfven waves,<br>'
    'nanoflares, and magnetic reconnection -- still actively debated.<br><br>'
    'MAPS C/2026 A1 (April 2026) crossed each boundary in sequence:<br>'
    'Extended F-corona (April 2, ~33 R_sun, ~0.153 AU) -><br>'
    'Alfven Surface (April 3 ~18:00, 18.8 R_sun, 0.087 AU) -><br>'
    '<b>DISINTEGRATION (April 4 08:15, 8.33 R_sun, 0.039 AU)</b> -><br>'
    'Streamer Belt / Roche Limit / Inner K-corona: crossed by DEBRIS ONLY -><br>'
    'Perihelion (April 4 14:22, 1.23 R_sun, 0.006 AU) as a ghost.<br>'
    'Ghost tracked by SOHO/LASCO ~36-40 hours outbound; dispersed by April 6.<br>'
    'Parker Solar Probe closest approach: 8.8 R_sun (0.041 AU) --<br>'
    'MAPS disintegrated at 8.33 R_sun (0.039 AU), just inside Parker\'s record.'
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
    return {
        'photosphere': (
            'Solar Photosphere<br>'
            'Temperature: ~6,000K<br>'
            'Radius: 0.00465 AU (1.0 R_sun)'
        ),
        'inner_corona': (
            'Inner Corona (K-corona)<br>'
            'Temperature: 1-3 million K<br>'
            'Extends to: 2-3 solar radii (~0.014 AU)<br>'
            'Roche limit at 3.45 R_sun just beyond this shell'
        ),
        'roche_limit': (
            'Roche Limit (Comets)<br>'
            '~3.45 solar radii (~0.016 AU)<br>'
            'Inside: tidal forces exceed cometary self-gravity<br>'
            'NOT absolute -- tensile strength allows survival inside it'
        ),
        'streamer_belt': (
            'Streamer Belt / Visible Corona<br>'
            'Temperature: ~1-2 million K<br>'
            'Extends to: ~6 solar radii -- eclipse white-light corona'
        ),
        'alfven_surface': (
            'Alfven Surface<br>'
            '~18.8 R_sun -- true corona/solar wind boundary<br>'
            'Parker Solar Probe first crossing: April 28, 2021'
        ),
        'outer_corona': (
            'Extended Corona (F-corona)<br>'
            'Temperature: ~1-2 million K<br>'
            'Extends to: ~50 solar radii (~0.23 AU)'
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

# ============================================================================
# SHELL DESIGN PATTERN (applied to all 15 sphere shells):
#
# Two-trace structure per shell:
#   1. Shell sphere  -- n_points=20 (outer/boundary) or 25 (inner sun),
#                       hoverinfo='skip' (no hover on cloud points)
#   2. Info marker   -- single cross symbol at north pole, 5% above shell
#                       radius, carries the full hover text for that shell.
#
# Benefits:
#   * Eliminates hover clutter from 400-3600 identical hover popups
#   * Reduces export file size by ~17 MB (hover text serialized once, not N^2)
#   * One predictable hover target per shell -- user learns where to look
#   * Cross symbol is visually distinct from all object markers (circle,
#     diamond, square are used elsewhere)
#
# Info marker position: (0, 0, r * 1.05) -- north pole of shell, 5% above
# surface so it floats clear of the shell dot cloud.
#
# Module updated: April 2026 with Anthropic's Claude Sonnet 4.6
# ============================================================================

# Individual Sun shell creation functions

def create_sun_gravitational_shell():
    """Creates the Sun's gravitational influence shell."""
    x, y, z = create_sphere_points(GRAVITATIONAL_INFLUENCE_AU, n_points=20)
    r_info = GRAVITATIONAL_INFLUENCE_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(102, 187, 106)', opacity=0.3),
        name='Sun\'s Gravitational Influence',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(102, 187, 106)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[gravitational_influence_info_hover],
        customdata=['Sun\'s Gravitational Influence'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_outer_oort_shell():
    """Creates the Sun's outer Oort cloud shell."""
    x, y, z = create_sphere_points(OUTER_OORT_CLOUD_AU, n_points=20)
    r_info = OUTER_OORT_CLOUD_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='white', opacity=0.3),
        name='Outer Oort Cloud',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='white', opacity=0.9,
                    symbol='cross', line=dict(color='gray', width=1)),
        name='',
        text=[outer_oort_info_hover],
        customdata=['Outer Oort Cloud'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_inner_oort_shell():
    """Creates the Sun's inner Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_OORT_CLOUD_AU, n_points=20)
    r_info = INNER_OORT_CLOUD_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='white', opacity=0.35),
        name='Inner Oort Cloud',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='white', opacity=0.9,
                    symbol='cross', line=dict(color='gray', width=1)),
        name='',
        text=[inner_oort_info_hover],
        customdata=['Inner Oort Cloud'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_inner_oort_limit_shell():
    """Creates the inner limit of the Sun's Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_LIMIT_OORT_CLOUD_AU, n_points=20)
    r_info = INNER_LIMIT_OORT_CLOUD_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='white', opacity=0.35),
        name='Inner Limit of Oort Cloud',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='white', opacity=0.9,
                    symbol='cross', line=dict(color='gray', width=1)),
        name='',
        text=[inner_limit_oort_info_hover],
        customdata=['Inner Limit of Oort Cloud'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_heliopause_shell():
    """Creates the Sun's heliopause shell."""
    x, y, z = create_sphere_points(HELIOPAUSE_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = HELIOPAUSE_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(135, 206, 250)', opacity=0.4),
        name='Solar Wind Heliopause',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(135, 206, 250)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[solar_wind_info_hover],
        customdata=['Solar Wind Heliopause'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_termination_shock_shell():
    """Creates the Sun's termination shock shell."""
    x, y, z = create_sphere_points(TERMINATION_SHOCK_AU, n_points=20)
    r_info = TERMINATION_SHOCK_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(240, 244, 255)', opacity=0.4),
        name='Solar Wind Termination Shock',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(240, 244, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='gray', width=1)),
        name='',
        text=[termination_shock_info_hover],
        customdata=['Solar Wind Termination Shock'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_outer_corona_shell():
    """Creates the Sun's extended outer corona (F-corona) shell."""
    x, y, z = create_sphere_points(OUTER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = OUTER_CORONA_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.5, color='rgb(25, 25, 112)', opacity=0.5),
        name='Sun: Outer Corona',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(25, 25, 112)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[outer_corona_info_hover],
        customdata=['Sun: Outer Corona'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_inner_corona_shell():
    """Creates the Sun's inner corona (K-corona) shell."""
    x, y, z = create_sphere_points(INNER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = INNER_CORONA_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(0, 0, 255)', opacity=0.45),
        name='Sun: Inner Corona',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(0, 0, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[inner_corona_info_hover],
        customdata=['Sun: Inner Corona'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_streamer_belt_shell():
    """
    Visible white-light corona / helmet streamer belt: ~4-6 solar radii.
    This is the corona seen during total solar eclipses. Distinct from the
    Alfven surface (plasma boundary) and the extended F-corona (dust-scattered).
    """
    x, y, z = create_sphere_points(STREAMER_BELT_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = STREAMER_BELT_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(255, 200, 80)', opacity=0.45),
        name='Sun: Streamer Belt (Visible Corona)',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 200, 80)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[streamer_belt_info_hover],
        customdata=['Sun: Streamer Belt (Visible Corona)'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_roche_limit_shell():
    """
    Fluid Roche limit for cometary bodies: ~3.45 solar radii (~0.016 AU).
    d = 2.44 * R_sun * (rho_sun / rho_comet)^(1/3)
    rho_sun=1408, rho_comet=500 kg/m^3.
    Inside this shell tidal forces overcome a fluid body's self-gravity --
    but tensile strength allows survival inside it (Ikeya-Seki, Great Comet of 1843).
    MAPS C/2026 A1 disintegrated at 8.33 R_sun (0.039 AU) -- OUTSIDE this shell.
    """
    x, y, z = create_sphere_points(ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(200, 60, 60)', opacity=0.5),
        name='Sun: Roche Limit (Comets)',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(200, 60, 60)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[roche_limit_info_hover],
        customdata=['Sun: Roche Limit (Comets)'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_alfven_surface_shell():
    """
    Alfven surface: the true outer boundary of the solar corona (~18.8 solar radii,
    ~0.087 AU). Beyond this surface, plasma can no longer communicate back to the Sun --
    the corona becomes the solar wind.
    Measured directly by NASA's Parker Solar Probe on April 28, 2021.
    MAPS C/2026 A1 crossed inward ~April 3, 2026 -- ~20 hours before disintegration.
    """
    x, y, z = create_sphere_points(ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.5, color='rgb(0, 200, 200)', opacity=0.35),
        name='Sun: Alfven Surface',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(0, 200, 200)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[alfven_surface_info_hover],
        customdata=['Sun: Alfven Surface'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_chromosphere_shell():
    """Creates the Sun's chromosphere shell."""
    x, y, z = create_sphere_points(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU, n_points=25)
    r_info = CHROMOSPHERE_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(30, 144, 255)', opacity=0.5),
        name='Sun: Chromosphere',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(30, 144, 255)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[chromosphere_info_hover],
        customdata=['Sun: Chromosphere'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_photosphere_shell():
    """Creates the Sun's photosphere shell (the visible solar surface)."""
    x, y, z = create_sphere_points(SOLAR_RADIUS_AU, n_points=25)
    r_info = SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=7.0, color='rgb(255, 244, 214)', opacity=1.0),
        name='Sun: Photosphere',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 244, 214)', opacity=0.95,
                    symbol='cross', line=dict(color='gray', width=1)),
        name='',
        text=[photosphere_info_hover],
        customdata=['Sun: Photosphere'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_radiative_shell():
    """Creates the Sun's radiative zone shell."""
    x, y, z = create_sphere_points(RADIATIVE_ZONE_AU, n_points=25)
    r_info = RADIATIVE_ZONE_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=7, color='rgb(30, 144, 255)', opacity=1.0),
        name='Sun: Radiative Zone',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(30, 144, 255)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[radiative_zone_info_hover],
        customdata=['Sun: Radiative Zone'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_core_shell():
    """Creates the Sun's core shell."""
    x, y, z = create_sphere_points(CORE_AU, n_points=25)
    r_info = CORE_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=10, color='rgb(70, 130, 180)', opacity=1.0),
        name='Sun: Core',
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(70, 130, 180)', opacity=0.95,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[core_info_hover],
        customdata=['Sun: Core'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


# ============================================================================
# PARTICLE CLOUD FUNCTIONS
# These are not sphere shells -- they use random point generation for visual
# effect. Same pattern applied: hoverinfo='skip' on all cloud points,
# single cross info marker at a representative north-pole position.
# Point density is unchanged (it defines the visual character of these objects).
# ============================================================================

import plotly.graph_objs as go
from planet_visualization_utilities import create_sphere_points, SOLAR_RADIUS_AU

def create_sun_hills_cloud_torus(inner_radius=2000, outer_radius=20000, thickness_ratio=0.3):
    """
    Create a toroidal (doughnut-shaped) Hills Cloud structure.
    FIXED VERSION - Returns proper Plotly trace objects.
    
    Parameters:
    - inner_radius: Inner boundary in AU (default: 2000)
    - outer_radius: Outer boundary in AU (default: 20000)
    - thickness_ratio: Ratio of torus thickness to major radius (default: 0.3)
    """
    major_radius = (inner_radius + outer_radius) / 2
    minor_radius = (outer_radius - inner_radius) / 2 * thickness_ratio
    
    n_points = 60
    u = np.linspace(0, 2*np.pi, n_points)
    v = np.linspace(0, 2*np.pi, n_points)
    u, v = np.meshgrid(u, v)
    
    noise_factor = 0.1
    radius_variation = 1 + noise_factor * np.random.normal(0, 1, u.shape)
    
    x = (major_radius + minor_radius * np.cos(u)) * np.cos(v) * radius_variation
    y = (major_radius + minor_radius * np.cos(u)) * np.sin(v) * radius_variation
    z = minor_radius * np.sin(u) * radius_variation * 0.5
    
    x_flat = x.flatten()
    y_flat = y.flatten()
    z_flat = z.flatten()

    hills_hover = (
        'Hills Cloud (Inner Oort): Disk-like structure<br>'
        '2,000-20,000 AU<br>'
        'More tightly bound to Solar System<br>'
        'Source of Jupiter-family comets<br>'
        'Toroidal shape due to galactic tides'
    )

    shell_trace = go.Scatter3d(
        x=x_flat, y=y_flat, z=z_flat,
        mode='markers',
        marker=dict(size=1.5, color='rgb(173, 216, 230)', opacity=0.4, symbol='circle'),
        name='Hills Cloud (Inner Oort - Toroidal)',
        hoverinfo='skip',
        showlegend=True
    )
    # Info marker at north pole of torus (z = minor_radius above major_radius)
    r_info = major_radius + minor_radius * 1.05
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(173, 216, 230)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[hills_hover],
        customdata=['Hills Cloud Torus'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_outer_oort_clumpy(radius_min=20000, radius_max=100000, n_clumps=15):
    """
    Create a clumpy, asymmetric outer Oort Cloud with density variations.
    FIXED VERSION - Returns proper Plotly trace objects.
    """
    points_x, points_y, points_z = [], [], []
    
    for i in range(n_clumps):
        clump_radius = np.random.uniform(radius_min, radius_max)
        theta = np.random.uniform(0, 2*np.pi)
        phi = np.random.uniform(-np.pi/2, np.pi/2)
        
        clump_center_x = clump_radius * np.cos(phi) * np.cos(theta)
        clump_center_y = clump_radius * np.cos(phi) * np.sin(theta)
        clump_center_z = clump_radius * np.sin(phi)
        
        n_points_in_clump = np.random.randint(50, 200)
        clump_size = np.random.uniform(5000, 15000)
        
        for j in range(n_points_in_clump):
            r = clump_size * np.random.beta(2, 5)
            theta_local = np.random.uniform(0, 2*np.pi)
            phi_local = np.random.uniform(-np.pi/2, np.pi/2)
            
            x = clump_center_x + r * np.cos(phi_local) * np.cos(theta_local)
            y = clump_center_y + r * np.cos(phi_local) * np.sin(theta_local)
            z = clump_center_z + r * np.sin(phi_local)
            
            distance = np.sqrt(x**2 + y**2 + z**2)
            if radius_min <= distance <= radius_max:
                points_x.append(x)
                points_y.append(y)
                points_z.append(z)
    
    x = np.array(points_x)
    y = np.array(points_y)
    z = np.array(points_z)

    clumpy_hover = (
        'Outer Oort Cloud: Clumpy, asymmetric structure<br>'
        '20,000-100,000+ AU<br>'
        'Source of long-period comets<br>'
        'Influenced by galactic tides and stellar encounters'
    )

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=1.0, color='rgb(255, 255, 255)', opacity=0.3, symbol='circle'),
        name='Outer Oort Cloud (Clumpy)',
        hoverinfo='skip',
        showlegend=True
    )
    r_info = radius_max * 1.05
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 255, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='gray', width=1)),
        name='',
        text=[clumpy_hover],
        customdata=['Outer Oort Cloud'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_sun_galactic_tide(radius=50000, n_points=2000):
    """
    Create Oort Cloud structure influenced by galactic tidal forces.
    The galactic plane creates asymmetry in the distribution.
    FIXED VERSION - Returns proper Plotly trace objects.
    """
    r = np.random.normal(radius, radius*0.3, n_points)
    r = np.clip(r, radius*0.5, radius*1.5)
    
    theta = np.random.uniform(0, 2*np.pi, n_points)
    
    phi_weights = np.linspace(-np.pi/2, np.pi/2, 100)
    weights = 1 + 0.5 * np.abs(np.sin(phi_weights))
    phi = np.random.choice(phi_weights, n_points, p=weights/weights.sum())
    
    x = r * np.cos(phi) * np.cos(theta)
    y = r * np.cos(phi) * np.sin(theta)
    z = r * np.sin(phi)

    tide_hover = (
        'Galactic Tide Influenced Objects<br>'
        'Asymmetric distribution due to Milky Way\'s gravity<br>'
        'Objects avoid galactic plane<br>'
        '~50,000 AU typical distance'
    )

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=0.8, color='rgb(255, 182, 193)', opacity=0.2, symbol='circle'),
        name='Galactic Tide Region',
        hoverinfo='skip',
        showlegend=True
    )
    r_info = radius * 1.5 * 1.05
    info_trace = go.Scatter3d(
        x=[0], y=[0], z=[r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 182, 193)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        text=[tide_hover],
        customdata=['Galactic Tide Region'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]


def create_enhanced_oort_cloud_visualization():
    """
    Create a more scientifically accurate Oort Cloud visualization.
    """
    traces = []
    
    # 1. Hills Cloud (Inner Oort) - Toroidal structure
    if True:  # Replace with your checkbox logic
        x_hills, y_hills, z_hills = create_sun_hills_cloud_torus()
        
        traces.append(go.Scatter3d(
            x=x_hills, y=y_hills, z=z_hills,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(173, 216, 230)',  # Light blue
                opacity=0.4,
                symbol='circle'
            ),
            name='Hills Cloud (Inner Oort - Toroidal)',
            text=['Hills Cloud: Disk-like structure, 2,000-20,000 AU<br>More tightly bound to Solar System<br>Source of Jupiter-family comets'] * len(x_hills),
            customdata=['Hills Cloud'] * len(x_hills),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
    
    # 2. Outer Oort Cloud - Clumpy structure
    if True:  # Replace with your checkbox logic
        x_outer, y_outer, z_outer = create_sun_outer_oort_clumpy()
        
        traces.append(go.Scatter3d(
            x=x_outer, y=y_outer, z=z_outer,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(255, 255, 255)',  # White
                opacity=0.3,
                symbol='circle'
            ),
            name='Outer Oort Cloud (Clumpy)',
            text=['Outer Oort Cloud: Clumpy, asymmetric structure<br>20,000-100,000+ AU<br>Source of long-period comets<br>Influenced by galactic tides and stellar encounters'] * len(x_outer),
            customdata=['Outer Oort Cloud'] * len(x_outer),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
    
    # 3. Galactic tide influenced region
    if True:  # Replace with your checkbox logic
        x_tide, y_tide, z_tide = create_sun_galactic_tide()
        
        traces.append(go.Scatter3d(
            x=x_tide, y=y_tide, z=z_tide,
            mode='markers',
            marker=dict(
                size=0.8,
                color='rgb(255, 182, 193)',  # Light pink
                opacity=0.2,
                symbol='diamond'
            ),
            name='Galactic Tide Region',
            text=['Galactic Tide Influenced Objects<br>Asymmetric distribution due to Milky Way\'s gravity<br>Objects avoid galactic plane<br>~50,000 AU typical distance'] * len(x_tide),
            customdata=['Galactic Tide Region'] * len(x_tide),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
    
    return traces

def create_oort_cloud_density_visualization():
    """
    Alternative approach: Show Oort Cloud as density gradients rather than discrete shells.
    """
    traces = []
    
    radii = [5000, 10000, 20000, 40000, 70000, 100000]
    densities = [0.8, 0.6, 0.5, 0.3, 0.2, 0.1]
    
    for i, (radius, density) in enumerate(zip(radii, densities)):
        n_points = int(500 * density)
        
        theta = np.random.uniform(0, 2*np.pi, n_points)
        phi = np.random.uniform(-np.pi/2, np.pi/2, n_points)
        r = np.random.normal(radius, radius*0.1, n_points)
        
        x = r * np.cos(phi) * np.cos(theta)
        y = r * np.cos(phi) * np.sin(theta)
        z = r * np.sin(phi)
        
        traces.append(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=max(0.5, 2.0 * density),
                color=f'rgba(255, 255, 255, {density})',
                opacity=density,
            ),
            name=f'Oort Density Layer {i+1}',
            text=[f'Oort Cloud Density Layer<br>Distance: ~{radius:,} AU<br>Relative density: {density:.1f}'] * len(x),
            customdata=[f'Density Layer {i+1}'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ))
    
    return traces

# Updated hover text with current scientific understanding
enhanced_oort_hover_text = """
<b>The Oort Cloud: Current Scientific Understanding</b><br><br>

<b>Structure:</b><br>
* <b>Hills Cloud (Inner Oort):</b> 2,000-20,000 AU, disk-like/toroidal<br>
* <b>Outer Oort Cloud:</b> 20,000-100,000+ AU, roughly spherical but clumpy<br><br>

<b>Key Characteristics:</b><br>
* Not uniform shells but complex, structured regions<br>
* Density varies significantly throughout<br>
* Influenced by galactic tides and stellar encounters<br>
* Contains an estimated 1-100 trillion objects >1km<br><br>

<b>Scientific Evidence:</b><br>
* Comet orbital inclinations suggest spherical outer region<br>
* Jupiter-family comets indicate inner disk-like region<br>
* Computer simulations show tidal sculpting effects<br>
* Stellar encounter models predict clumpy structure<br><br>

<b>Recent Discoveries:</b><br>
* Objects like Sedna may be inner Oort Cloud members<br>
* 2012 VP113 provides evidence for inner Oort population<br>
* NEOWISE survey improving population estimates
"""
