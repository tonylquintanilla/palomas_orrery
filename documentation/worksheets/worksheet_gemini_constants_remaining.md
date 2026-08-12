Here is the completed citation verification worksheet for the final six constants in constants\_new.py.

### **Worksheet: constants\_new.py Remaining Items**

| \# | Constant | Value | Cited source | Citation correct? | Notes |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | CORE\_AU | 0.2 $R\_{\\odot}$ | Standard solar model (Bahcall et al.) | Yes (with clarification) | 0.2 $R\_{\\odot}$ represents the boundary within which \>95% of solar fusion occurs. |
| 2 | RADIATIVE\_ZONE\_AU | 0.7 $R\_{\\odot}$ | Standard solar model | Yes (as approximation) | 0.7 is a widely used rounded value for the radiative-convective boundary. |
| 3 | INNER\_CORONA\_RADII | 3 | Golub & Pasachoff, "The Solar Corona" (2010) | Yes | The K-corona dominates scattering out to roughly 2.5–3 $R\_{\\odot}$. |
| 4 | STREAMER\_BELT\_RADII | 6.0 | Golub & Pasachoff (2010); DeForest et al. (2018) | Yes | Helmet streamer stalks can remain coherent up to 4–6 $R\_{\\odot}$. |
| 5 | MOON\_RADIUS\_KM | 1737.4 | NASA Fact Sheet | Yes | Volumetric mean radius is exactly 1737.4 km. |
| 6 | Group D header (Chromosphere) | 1.5 $R\_{\\odot}$ (prior) / 1.1 $R\_{\\odot}$ (current) | Carroll & Ostlie (2017) | No | The text strictly defines the chromosphere as \~2,000 km thick (\~1.003 $R\_{\\odot}$). |

### **Detailed Findings & Source Notes**

**1\. Solar core boundary**

* **Source Verification:** The standard solar model places the energy-generating core roughly between 0.2 and 0.25 $R\_{\\odot}$.  
* **Defensibility:** 0.2 $R\_{\\odot}$ is the generally accepted lower bound defining the region where nearly all nuclear fusion occurs; beyond 0.2, the energy generation rate drops toward zero. The most authoritative specific reference to cite for this exact standard model boundary is Bahcall, Pinsonneault, & Basu (2001).  
* **Carroll & Ostlie:** Yes, Chapter 11 of Carroll & Ostlie also describes the core as encompassing the inner \~0.2 to 0.25 radii of the Sun.

**2\. Radiative zone boundary**

* **Source Verification:** Helioseismology, specifically the foundational work by Christensen-Dalsgaard et al. (1991), locates the base of the convection zone (the tachocline) at $0.713 \\pm 0.003 R\_{\\odot}$.  
* **Defensibility:** The cited value of 0.7 is a well-established and perfectly defensible rounded approximation used in textbook standard solar models (including Carroll & Ostlie).  
* **Citation Fix:** Update the code citation from "Standard solar model" to "Christensen-Dalsgaard et al. (1991) / Standard solar model approximation".

**3\. Inner corona boundary**

* **Source Verification:** Golub & Pasachoff's *The Solar Corona* identifies the physical transition where the K-corona (electron-scattered white light) gives way to the F-corona (dust-scattered light).  
* **Defensibility:** This transition generally occurs around 2.5 to 3 $R\_{\\odot}$. Calling it a "visualization boundary" is fair because there is no hard physical wall, but the 3 $R\_{\\odot}$ mark represents a legitimate photometric and physical transition in the coronal medium.

**4\. Streamer belt extent**

* **Source Verification:** Both Golub & Pasachoff (2010) and DeForest et al. (2018) observe coronal structures extending deeply into the heliosphere.  
* **Defensibility:** Helmet streamers taper into stalks that are routinely measured maintaining coherence out to 4 to 6 $R\_{\\odot}$ before fully transitioning into the solar wind. Using 6.0 as the upper bound is entirely defensible based on these sources.

**5\. Moon radius**

* **Source Verification:** The NASA NSSDCA Moon Fact Sheet precisely lists the volumetric mean radius of the Moon as 1737.4 km. (For reference, the equatorial radius is 1738.1 km and the polar radius is 1736.0 km).

**6\. Solar photospheric radius citation (Group D header)**

* **Source Verification:** Carroll & Ostlie (Chapter 11\) definitively states that the chromosphere is a very thin layer, approximately 2,000 km deep (which is less than 1% of the solar radius, yielding a physical boundary of \~1.003 $R\_{\\odot}$).  
* **Defensibility of 1.5 $R\_{\\odot}$:** The textbook does *not* support a 1.5 $R\_{\\odot}$ boundary for the chromosphere. It is highly likely the previous code conflated the chromosphere with the extended lower corona or the transition region, or simply utilized an arbitrary visualization scale and mistakenly attributed it to the book. The current updated shell value of 1.1 $R\_{\\odot}$ is much closer to reality, but still functions strictly as a visualization shell rather than a physical boundary supported by the text.