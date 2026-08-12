# Blind Source Lookup — Batch 1 Final Resolution

**Prompt commit:** `2ccf6839c4278f01db00fbe2101440ab267a90c2`  
**Cross-checker:** GPT-5.6 Thinking  
**Date:** August 3, 2026

## Worksheet

| # | Source to check | Topic | What the source says | Resolution |
|---|---|---|---|---|
| BL-1A | Potter & Morgan (1985), “Discovery of sodium in the atmosphere of Mercury” | Mercury sodium-tail extent | The paper reports discovery of sodium emission and estimates sodium column abundance and near-surface density. Its abstract does not describe or quantify an anti-solar sodium tail. | **NOT ADDRESSED** |
| BL-1B | Baumgardner, Wilson & Mendillo (2008) | Mercury sodium-tail extent | The abstract states that the tail extends about **1.5°**, corresponding to nearly **1,400 Mercury radii**. The body converts this to about **3.4 × 10⁶ km**. | **CONFIRMED** |
| BL-1C | Schmidt et al. (2010), cited as “Observations of Mercury’s sodium tail,” *Icarus* 207, 9–16 | Mercury sodium-tail extent | The bibliographic combination appears to correspond to **“Orbital effects on Mercury’s escaping sodium exosphere,”** not the title in the prompt. The accessible abstract discusses a 7° field of view but does not publish a single maximum extent. | **SOURCE TITLE MISMATCH; MAXIMUM EXTENT NOT FOUND** |
| BL-2 | “The Internal Structure of Eris Inferred from Its Spin and Orbit Evolution” | Eris present central temperature | The paper estimates a present central temperature of about **875 K**, assuming present chondritic radiogenic heating, thermal conductivity **3 W m⁻¹ K⁻¹**, and surface temperature **30 K**. | **CONFIRMED** |
| BL-3A | Margot et al. (2012) | Mercury internal dimensions | The paper constrains moment of inertia and supports a large liquid core. It does not state a unique core radius, inner-core radius, outer-core thickness, mantle thickness, or crustal thickness as its dimensional result. | **DIMENSIONS NOT DIRECTLY STATED** |
| BL-3B | Hauck et al. (2013) | Mercury internal dimensions | The paper estimates the **top of the liquid core at 2,020 ± 30 km radius**. The solid shell above it is **420 ± 30 km thick** and includes mantle, crust, and possibly a solid FeS-rich layer. It does not give a 1,074 km outer-core thickness. | **CONFIRMED** |
| BL-4A | Bertaux et al. (2007) | Venus atmospheric structure | The paper explicitly calls **60–100 km the mesosphere** and places the thermosphere **above 100 km**. It reports a warm nightside layer at **90–120 km**. It does not give a general dayside thermosphere temperature of 300 K or an ionospheric peak altitude. | **PARTLY CONFIRMED; OTHER ITEMS NOT ADDRESSED** |
| BL-4B | Seiff et al. (1985), VIRA | Venus atmospheric structure | The model covers the atmosphere from the surface to **100 km**. It does not address the thermosphere above 100 km or ionospheric peak electron density. I could not verify a specific mesosphere lower boundary or 300 K dayside thermosphere value from accessible text. | **THERMOSPHERE/IONOSPHERE NOT ADDRESSED; OTHER DETAILS NOT VERIFIED** |
| BL-5A | Williams (2007), “A scheme for lunar inner core detection” | Lunar core temperatures | The paper concerns detecting an inner core through rotational effects. The accessible source does not state inner-core temperature **1,600–1,700 K** or outer-core/CMB temperature **1,300–1,600 K**. | **NOT ADDRESSED** |
| BL-5B | Laneuville et al., lunar thermal-evolution paper | Lunar core temperatures | The likely paper is Laneuville, Taylor & Wieczorek (2018), not 2014. It models core energy balance and plots CMB temperature evolution, but the accessible text does not state the requested fixed temperature ranges. | **EXPECTED RANGES NOT FOUND** |
| BL-6 | Bierson, Nimmo & Stern (2020) | Pluto formation and present internal temperature | The representative cold-start model uses about **300 K in silicates and 200 K in ice**. The paper argues that rapid final accretion, under about **30 kyr**, could yield a hot start and early ocean. It supports a present subsurface ocean but does not publish a single present core temperature such as 1,000 K in accessible text. | **FORMATION CONDITIONS ADDRESSED; SINGLE PRESENT CORE TEMPERATURE NOT STATED** |
| BL-7 | Gladstone et al. (2016) | Pluto surface temperature | The initial New Horizons analysis reports approximately **37 ± 3 K**. Later full REX analysis gives **38.9 ± 2.1 K** at entry and **51.6 ± 3.8 K** at exit. | **CONFIRMED: ~37 ± 3 K IN GLADSTONE ET AL.** |
| BL-8 | Standard Hill-sphere treatment for binaries | Primary mass or total system mass? | For the Hill sphere of a bound binary orbiting the Sun, use the **combined system mass** and the heliocentric orbit of the barycenter. At distances large compared with binary separation, the external gravitational field is set by total mass. JPL lists separate GMs that should be summed. For Pluto–Charon, Pluto GM is 869.3 and Charon GM is 106.1 km³/s², giving system GM about 975.4 km³/s². | **USE TOTAL BINARY-SYSTEM MASS** |

## Detailed notes

Potter & Morgan (1985) is a sodium-atmosphere discovery paper, not a sodium-tail-extent paper. Baumgardner et al. (2008) is the direct large-scale source for approximately 1,400 Mercury radii or 3.4 million km. No checked source gives 10,000 Mercury radii.

Hauck et al. (2013) gives Mercury’s liquid-core radius and overlying solid-shell thickness directly. Neither Hauck nor Margot supports a 1,074 km outer-core thickness.

Bertaux et al. (2007) provides the clearest Venus layer language: 60–100 km mesosphere, thermosphere above 100 km, and a warm nightside layer at 90–120 km. The “warm layer” should not be equated with the entire cryosphere.

The proposed lunar core-temperature references remain unresolved. The Williams paper does not address those temperatures, and the identifiable Laneuville paper does not expose the requested fixed ranges in accessible text.

Bierson et al. supports a hot-start interpretation and early ocean formation, not a single present-day 1,000 K Pluto core temperature.

For binary Hill spheres, the standard approximation is:

\[
r_H \simeq a_{bary}\left(\frac{m_1+m_2}{3M_\odot}\right)^{1/3}
\]

For Pluto–Charon, using Pluto alone understates the system Hill radius by roughly 3.8%.
